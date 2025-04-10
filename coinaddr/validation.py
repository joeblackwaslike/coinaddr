# pylint: disable=no-member

"""
:mod:`coinaddr.validation`
~~~~~~~~~~~~~~~~~~~~~~~~

Various validation machinery for validating cryptocurrency addresses.
"""

import re
from hashlib import sha256
import functools
import operator

from zope.interface import implementer, provider
import attr
from zope.interface import providedBy
import base58check
from Crypto.Hash import keccak

from .interfaces import (
    INamedSubclassContainer,
    IValidator,
    IValidationRequest,
    IValidationResult,
    ICurrency,
)
from .base import NamedSubclassContainerBase
from . import currency
from .segwit_addr import bech32_decode


@provider(INamedSubclassContainer)
class Validators(metaclass=NamedSubclassContainerBase):
    """Container for all validators."""


class ValidatorMeta(type):
    """Register validator classes on Validators.validators."""

    def __new__(mcs, cls, bases, attrs):
        new = type.__new__(mcs, cls, bases, attrs)
        if new.name:
            Validators[new.name] = new
        return new


@attr.s(eq=False, slots=True)
class ValidatorBase(metaclass=ValidatorMeta):
    """Validator Interface."""

    name = None

    request = attr.ib(
        type="ValidationRequest",
        validator=[
            lambda i, a, v: type(v).__name__ == "ValidationRequest",
            lambda i, a, v: IValidationRequest in providedBy(v),
        ],
    )

    def validate(self):
        """Validate the address type, return True if valid, else False."""

    @property
    def network(self):
        """Return the network derived from the network version bytes."""


@attr.s(frozen=True, slots=True, eq=False)
@implementer(IValidator)
class Base58CheckValidator(ValidatorBase):
    """Validates Base58Check based cryptocurrency addresses."""

    name = "Base58Check"

    def validate(self):
        """Validate the address."""
        if len(self.request.address) < 25 or len(self.request.address) > 35:
            return False

        try:
            abytes = base58check.b58decode(self.request.address, **self.request.extras)
            if abytes[0] not in self.request.networks:
                return False

            checksum = sha256(sha256(abytes[:-4]).digest()).digest()[:4]
            if abytes[-4:] != checksum:
                return False

            return self.request.address == base58check.b58encode(
                abytes, **self.request.extras
            )
        except Exception:
            return False

    @property
    def network(self):
        """Return network derived from network version bytes."""
        try:
            abytes = base58check.b58decode(self.request.address, **self.request.extras)

            nbyte = abytes[0]
            for name, networks in self.request.currency.networks.items():
                if nbyte in networks:
                    return name
        except Exception:
            pass

        return ""


@attr.s(frozen=True, slots=True, eq=False)
@implementer(IValidator)
class EthereumValidator(ValidatorBase):
    """Validates ethereum based crytocurrency addresses."""

    name = "Ethereum"
    non_checksummed_pattern = re.compile(r"^(0x)?[0-9a-f]{40}$", flags=re.IGNORECASE)

    def validate(self):
        """Validate the address."""
        address = self.request.address.decode()

        if not self.non_checksummed_pattern.match(address):
            return False
        elif re.match(r"^(0x)?[0-9a-f]{40}$", address) or re.match(
            r"^(0x)?[0-9A-F]{40}$", address
        ):
            return True

        addr = address[2:] if address.startswith("0x") else address
        addr_hash = keccak.new(digest_bits=256)
        addr_hash.update(addr.lower().encode("utf-8"))
        addr_hash = addr_hash.hexdigest()

        return not any(
            any(
                [
                    int(addr_hash[i], 16) > 7 and addr[i].upper() != addr[i],
                    int(addr_hash[i], 16) <= 7 and addr[i].lower() != addr[i],
                ]
            )
            for i in range(len(addr))
        )

    @property
    def network(self):
        """Return network derived from network version bytes."""
        return "both"


@attr.s(frozen=True, slots=True, eq=False)
@implementer(IValidator)
class SegWitValidator(ValidatorBase):
    """Validates SegWit based cryptocurrency addresses."""

    name = "SegWitCheck"

    def validate(self):
        """Validate the address."""
        hrp, data = bech32_decode(self.request.address.decode())
        return bool(hrp) and bool(data)

    @property
    def network(self):
        """Return network derived from network version bytes."""
        hrp, data = bech32_decode(self.request.address.decode())
        return next(
            (
                name
                for name, networks in self.request.currency.networks.items()
                if hrp in networks
            ),
            "unknown",
        )


# @attr.s(frozen=True, slots=True, eq=False)


@attr.s(frozen=True, slots=True, eq=False)
@implementer(IValidationRequest)
class ValidationRequest:
    """Contain the data and helpers as an immutable request object."""

    currency = attr.ib(
        type=currency.Currency,
        converter=currency.Currencies.get,
        validator=[
            attr.validators.instance_of(currency.Currency),
            lambda i, a, v: ICurrency in providedBy(v),
        ],
    )
    address = attr.ib(
        type=bytes,
        converter=lambda a: a if isinstance(a, bytes) else a.encode("ascii"),
        validator=attr.validators.instance_of(bytes),
    )

    @property
    def extras(self):
        """Extra arguments for passing to decoder, etc."""
        extras = {}
        if self.currency.charset:
            extras.setdefault("charset", self.currency.charset)
        return extras

    @property
    def networks(self):
        """Concatenated list of all version bytes for currency."""
        networks = tuple(self.currency.networks.values())
        return functools.reduce(operator.concat, networks)

    def execute(self):
        """Execute this request and return the result."""
        validator = Validators.get(self.currency.validator)(self)
        return ValidationResult(
            name=self.currency.name,
            ticker=self.currency.ticker,
            address=self.address,
            valid=validator.validate(),
            network=validator.network,
        )


@attr.s(frozen=True, slots=True, eq=False)
@implementer(IValidationResult)
class ValidationResult:
    """Contains an immutable representation of the validation result."""

    name = attr.ib(type=str, validator=attr.validators.instance_of(str))
    ticker = attr.ib(type=str, validator=attr.validators.instance_of(str))
    address = attr.ib(type=bytes, validator=attr.validators.instance_of(bytes))
    valid = attr.ib(type=bool, validator=attr.validators.instance_of(bool))
    network = attr.ib(type=str, validator=attr.validators.instance_of(str))

    def __bool__(self):
        return self.valid


def validate(currency, address):
    """Validate the given address according to currency type.

    This is the main entrypoint for using this library.

    :param currency str: The name or ticker code of the cryptocurrency.
    :param address (bytes, str): The crytocurrency address to validate.
    :return: a populated ValidationResult object
    :rtype: :inst:`ValidationResult`

    Usage::

      >>> import coinaddr
      >>> coinaddr.validate('btc', b'1BoatSLRHtKNngkdXEeobR76b53LETtpyT')
      ValidationResult(name='bitcoin', ticker='btc',
      ...              address=b'1BoatSLRHtKNngkdXEeobR76b53LETtpyT',
      ...              valid=True, network='main')

    """
    request = ValidationRequest(currency, address)
    return request.execute()
