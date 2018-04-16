"""
:mod:`coinaddr.validation`
~~~~~~~~~~~~~~~~~~~~~~~~

Base/meta-classes for the currency and validation machinery.
"""

from weakref import WeakValueDictionary


class NamedInstanceContainerBase(type):
    """A Container for instances."""

    def __init__(cls, name, bases, idict):
        super(NamedInstanceContainerBase, cls).__init__(name, bases, idict)
        cls.instances = dict()

    def __getitem__(cls, name):
        return cls.instances[name]

    def __setitem__(cls, name, obj):
        cls.instances[name] = obj

    def __delitem__(cls, name):
        del cls.instances[name]

    def __contains__(cls, name):
        return name in cls.instances

    def __iter__(cls):
        return iter(cls.instances)

    def get(cls, name, default=None):
        """Returns instance by name."""
        return cls.instances.get(name, default)


class NamedSubclassContainerBase(type):
    """A Container for subclasses."""

    def __init__(cls, name, bases, idict):
        super(NamedSubclassContainerBase, cls).__init__(name, bases, idict)
        cls.subclasses = WeakValueDictionary()

    def __getitem__(cls, name):
        return cls.subclasses[name]

    def __setitem__(cls, name, obj):
        cls.subclasses[name] = obj

    def __delitem__(cls, name):
        del cls.subclasses[name]

    def __contains__(cls, name):
        return name in cls.subclasses

    def __iter__(cls):
        return iter(cls.subclasses)

    def get(cls, name, default=None):
        """Returns subclass by name."""
        return cls.subclasses.get(name, default)
