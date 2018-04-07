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

## Changes
* [CHANGELOG](CHANGELOG.md)
