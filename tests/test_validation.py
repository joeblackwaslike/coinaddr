import unittest

from coinaddr.interfaces import (
    INamedSubclassContainer, IValidator, IValidationRequest, IValidationResult
    )
from coinaddr.validation import (
    Validators, ValidatorBase, ValidationRequest, ValidationResult,
    Base58CheckValidator, EthereumValidator
    )


class TestValidation(unittest.TestCase):
    def test_interfaces(self):
        self.assertTrue(INamedSubclassContainer.providedBy(Validators))

        validators = [Base58CheckValidator, EthereumValidator]
        for validator in validators:
            with self.subTest(validator=validator):
                self.assertTrue(IValidator.implementedBy(validator))

        self.assertTrue(
            IValidationRequest.implementedBy(ValidationRequest))
        self.assertTrue(
            IValidationResult.implementedBy(ValidationResult))


if __name__ == '__main__':
    unittest.main()
