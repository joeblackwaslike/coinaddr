import unittest

from coinaddr.interfaces import (
    INamedSubclassContainer,
    IValidator,
    IValidationRequest,
    IValidationResult,
)
from coinaddr.validation import (
    Validators,
    ValidationRequest,
    ValidationResult,
    Base58CheckValidator,
    EthereumValidator,
    SegWitValidator,
)


class TestValidation(unittest.TestCase):
    def test_interfaces(self):
        self.assertTrue(INamedSubclassContainer.providedBy(Validators))

        validators = [Base58CheckValidator, EthereumValidator, SegWitValidator]
        for validator in validators:
            with self.subTest(validator=validator):
                self.assertTrue(IValidator.implementedBy(validator))

        self.assertTrue(IValidationRequest.implementedBy(ValidationRequest))
        self.assertTrue(IValidationResult.implementedBy(ValidationResult))


if __name__ == "__main__":
    unittest.main()
