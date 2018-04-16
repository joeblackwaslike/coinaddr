"""
:mod:`coinaddr`
~~~~~~~~~~~

A crypto-currency address inspection/validation library for python.

Usage::

    >>> import coinaddr
    >>> coinaddr.validate('btc', b'1BoatSLRHtKNngkdXEeobR76b53LETtpyT')
    ValidationResult(name='bitcoin', ticker='btc',
    ...              address=b'1BoatSLRHtKNngkdXEeobR76b53LETtpyT', valid=True,
    ...              network='main')

:copyright: (c) 2018 by Joseph Black.
:license: MIT, see LICENSE for more details.
"""

__version__ = '1.0.1'

from . import interfaces, currency, validation
from .validation import validate
from .currency import Currency
from .validation import ValidatorBase, Base58CheckValidator, EthereumValidator
