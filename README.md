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
pip3 install coinaddr
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
