# pylint: disable=inherit-non-class,no-self-argument,no-method-argument
# pylint: disable=unexpected-special-method-signature,arguments-differ

"""
:mod:`coinaddr.interfaces`
~~~~~~~~~~~~~~~~~~~~~~~~

Various zope compatible interfaces for the coinaddr package.
"""

from zope.interface import Interface, Attribute


class INamedInstanceContainer(Interface):
    """Contains all currencies instantiated."""

    instances = Attribute('Mapping of instance.name -> instance')

    def __getitem__(name):
        """Return the named instance"""

    def __setitem__(name, obj):
        """Add the named instance to the mapping of instances"""

    def __delitem__(name, obj):
        """Add the named instance to the mapping of instances"""

    def __contains__(name):
        """Return true if we contain the named instance"""

    def __iter__():
        """Return an iterable, iterating all instances"""

    def get(name, default=None):
        """Return the named instance if we contain it, else default"""


class INamedSubclassContainer(Interface):
    """Contains a weakvaluedict of subclasses."""

    subclasses = Attribute('Mapping of subclass.name -> subclass')

    def __getitem__(name):
        """Return the named subclass"""

    def __setitem__(name, obj):
        """Add the named subclass to the mapping of subclasses"""

    def __delitem__(name, obj):
        """Add the named subclass to the mapping of subclasses"""

    def __contains__(name):
        """Return true if we contain the named subclass"""

    def __iter__():
        """Return an iterable, iterating all subclasses"""

    def get(name, default=None):
        """Return the named subclass if we contain it, else default"""


class ICurrency(Interface):
    """A cryptocurrency address specification."""

    name = Attribute('Name of currency')
    ticker = Attribute('Ticker symbol for currency')
    validator = Attribute('Validator name for validation')
    networks = Attribute('The networks and version bytes for those networks')
    charset = Attribute('For base58Check based currencies, custom charset.')


class IValidator(Interface):
    """A cryptocurrency address validator."""

    name = Attribute('Name of validator')
    network = Attribute('Network name of address being validated')

    def validate():
        """Validate the address type, True if valid, else False."""


class IValidationRequest(Interface):
    """Contains the data and helpers for a given validation request."""

    currency = Attribute('The currency name or ticker being validated')
    address = Attribute('The address to be validated')
    extras = Attribute('Any extra attributes to be passed to decoder, etc')
    networks = Attribute(
        'Concatenated list of all network versions for currency')

    def execute():
        """Executes the request and returns a ValidationResult object"""


class IValidationResult(Interface):
    """Represents all data for a validation result."""

    name = Attribute('Name of currency for address validated')
    ticker = Attribute('Ticker of currency for address validated')
    address = Attribute('The address that was validated')
    valid = Attribute('Boolean representing whether the address is valid')
    network = Attribute(
        'Name of network the address belongs to if applicable')
