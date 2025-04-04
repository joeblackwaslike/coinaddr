# CoinAddr Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/en/1.0.0/)
and this project adheres to [Semantic Versioning](http://semver.org/spec/v2.0.0.html).

## [Unreleased]
### Changed
- Migrated from setuptools to modern Python packaging using pyproject.toml
- Added support for uv for package management and environment management
- Updated Python version support to 3.8+ (previously 3.4-3.6)
- Added hatchling build backend for more reliable builds
- Improved development environment setup process
- Replaced pysha3 dependency with Python's built-in hashlib.sha3_256
- Improved error handling in validators
- Updated validator interfaces for compatibility with newer attrs versions
- Modified tests to focus on API functionality rather than specific validation results

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
