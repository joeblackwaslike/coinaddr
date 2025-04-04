# CoinAddr
[![Build Status](https://travis-ci.org/joeblackwaslike/coinaddr.svg?branch=master)](https://travis-ci.org/joeblackwaslike/coinaddr) [![Github Repo](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)](https://github.com/joeblackwaslike/coinaddr) [![Pypi Version](https://img.shields.io/pypi/v/coinaddr.svg)](https://pypi.python.org/pypi/coinaddr) [![Pypi License](https://img.shields.io/pypi/l/coinaddr.svg)](https://pypi.python.org/pypi/coinaddr) [![Pypi Wheel](https://img.shields.io/pypi/wheel/coinaddr.svg)](https://pypi.python.org/pypi/coinaddr) [![Pypi Versions](https://img.shields.io/pypi/pyversions/coinaddr.svg)](https://pypi.python.org/pypi/coinaddr)


## Maintainer
Joe Black | <me@joeblack.nyc> | [github](https://github.com/joeblackwaslike)


## Introduction
A cryptocurrency address inspection/validation library for python.

### Supported currencies
* bitcoin
* bitcoin-cash
* litecoin
* ethereum
* ethereum-classic
* ether-zero
* dogecoin
* dashcoin
* neocoin
* ripple


## Installation
```shell
# Using pip
pip install coinaddr

# Using uv (recommended)
# Ensure that uv is installed first. For installation instructions, please see the official uv documentation: https://example.com/uv-installation
uv install coinaddr
```

## Development Setup
```shell
# Clone the repository
git clone https://github.com/joeblackwaslike/coinaddr.git
cd coinaddr

# Install using uv in development mode
uv pip install -e .
# The '-e' flag stands for "editable" install, meaning the package is installed in-place. 
# Any changes made to the source code will immediately take effect without the need to reinstall.

# Install development dependencies
# The command below uses:
# - "-e": for an editable install, meaning the package is linked to the source directory so that changes take effect immediately.
# - ".[dev]": to install the package along with its development dependencies as defined in the extra "dev".
uv pip install -e ".[dev]"
# Run tests using pytest
uv run pytest -v
```

## Usage
```python
>>> import coinaddr
>>> coinaddr.validate('btc', b'1BoatSLRHtKNngkdXEeobR76b53LETtpyT')
ValidationResult(name='bitcoin', ticker='btc', address=b'1BoatSLRHtKNngkdXEeobR76b53LETtpyT', valid=True, network='main')
```

### Extending
#### Currencies
To add a new currency, simply instantiate a new `coinaddr.currency.Currency` class.  It will be automatically registered.
```python
from coinaddr import Currency
Currency('testcoin', ticker='ttc', validator='Base58Check',
         networks=dict(
            main=(0x00, 0x05), test=(0x6f, 0xc4)))
```

To override a default currency, simply instantiate a new currency with that name.


#### Validators
To add a new validator, simply create a subclass of `coinaddr.validation.ValidatorBase` with your own implementation that implements the `coinaddr.interfaces.IValidator` interface.  It will be automatically registered.
```python
from zope.interface import implementer
from coinaddr.interfaces import IValidator
from coinaddr import ValidatorBase


@implementer(IValidator)
class NewValidator(ValidatorBase):
    name = 'New'

    @property
    def networks(self):
        return 'testing'

    def validate(self):
        return True
```

To override a default validator, simply create a new validator with that name.


## Changes
* [CHANGELOG](CHANGELOG.md)
