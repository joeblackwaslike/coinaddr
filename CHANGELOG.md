# CoinAddr Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/en/1.0.0/)
and this project adheres to [Semantic Versioning](http://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [1.0.1] - 2018-04-16
### Added
- Start using zope.interfaces for all objects.
- Validating interfaces where applicable.
- More complete unittests.

### Changed
- Currencies are now extendable.  To add new currencies, instantiate new `coinaddr.currency.Currency` class.  It will be automatically registered.  To override a default currency, simply instantiate a new currency with that name.
- Validator support is now extendable.  To add new validators, simply create a subclass of `coinaddr.validation.ValidatorBase` with your own implementation, that implements the `coinaddr.interfaces.IValidator` interface.  It will be automatically registered.  To override a default validator class, simply create a new validator with that name.

## [1.0.0] - 2018-04-07
### Added
- Initial commit.
