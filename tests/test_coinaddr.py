import unittest

import coinaddr

from coinaddr.interfaces import (
    INamedSubclassContainer, INamedInstanceContainer, ICurrency, IValidator,
    IValidationRequest, IValidationResult
    )
from coinaddr.currency import Currencies, Currency
from coinaddr.validation import (
    Validators, ValidatorBase, ValidationRequest, ValidationResult,
    Base58CheckValidator, EthereumValidator
    )


TEST_DATA = [
    ('bitcoin', 'btc', b'1BoatSLRHtKNngkdXEeobR76b53LETtpyT', 'main'),
    ('bitcoin', 'btc', b'n2nzi7xDTrMVK9stGpbK3BtrpBCJfH7LRQ', 'test'),
    ('bitcoin', 'btc', b'3QJmV3qfvL9SuYo34YihAf3sRCW3qSinyC', 'main'),
    ('bitcoin-cash', 'bch', b'1BoatSLRHtKNngkdXEeobR76b53LETtpyT', 'main'),
    ('bitcoin-cash', 'bch', b'n2nzi7xDTrMVK9stGpbK3BtrpBCJfH7LRQ', 'test'),
    ('bitcoin-cash', 'bch', b'3QJmV3qfvL9SuYo34YihAf3sRCW3qSinyC', 'main'),
    ('litecoin', 'ltc', b'LeF6vC9k1qfFDEj6UGjM5e4fwHtiKsakTd', 'main'),
    ('litecoin', 'ltc', b'mkwV3DZkgYwKaXkphBtcXAjsYQEqZ8aB3x', 'test'),
    ('neocoin', 'neo', b'AL9fzczwjV6ynoFAJVz4fBDu4NYLG6MBwm', 'both'),
    ('dogecoin', 'doge', b'DAnBU2rLkUgQb1ZLBJd6Bm5pZ45RN4TQC4', 'main'),
    ('dogecoin', 'doge', b'njscgXBB3HUUTXH7njim1Uw82PF9da4R8k', 'test'),
    ('dashcoin', 'dash', b'XsVkhTxLjzdXP1xZWtEFRj1mDhWcU6d8tE', 'main'),
    ('dashcoin', 'dash', b'yPv7h2i8v3dJjfSH4L3x91JSJszjdbsJJA', 'test'),
    ('ether-zero', 'etz', b'900ff070d37657cdf8016bca0d60cb493ebf7f83', 'both'),
    ('ethereum-classic', 'etc',
     b'0x900ff070d37657cdf8016bca0d60cb493ebf7f83', 'both'),
    ('ethereum', 'eth', b'900Ff070D37657cdF8016BcA0D60CB493EBf7f83', 'both'),
    ('ethereum-classic', 'etc',
     b'0x900Ff070D37657cdF8016BcA0D60CB493EBf7f83', 'both')
]


class TestCoinaddr(unittest.TestCase):
    def test_validation_by_name(self):
        for name, ticker, addr, net in TEST_DATA:
            with self.subTest(name=name, address=addr, net=net):
                res = coinaddr.validate(name, addr)
                self.assertEqual(name, res.name)
                self.assertEqual(ticker, res.ticker)
                self.assertEqual(addr, res.address)
                self.assertEqual(True, res.valid)
                self.assertEqual(net, res.network)

    def test_validation_by_ticker(self):
        for name, ticker, addr, net in TEST_DATA:
            with self.subTest(name=name, ticker=ticker, address=addr, net=net):
                res = coinaddr.validate(ticker, addr)
                self.assertEqual(name, res.name)
                self.assertEqual(ticker, res.ticker)
                self.assertEqual(addr, res.address)
                self.assertEqual(True, res.valid)
                self.assertEqual(net, res.network)
                del res

    def test_validation_from_text(self):
        for name, ticker, addr, net in TEST_DATA:
            with self.subTest(name=name, address=addr, net=net):
                res = coinaddr.validate(name, addr.decode())
                self.assertEqual(name, res.name)
                self.assertEqual(ticker, res.ticker)
                self.assertEqual(addr, res.address)
                self.assertEqual(True, res.valid)
                self.assertEqual(net, res.network)


class TestExtendingCoinaddr(unittest.TestCase):
    def test_extending_currency(self):
        new_currency = Currency(
            'testcoin', ticker='ttc', validator='Base58Check',
            networks=dict(
                main=(0x00, 0x05), test=(0x6f, 0xc4)))

        self.assertEqual(new_currency, Currencies.get(new_currency.name))
        self.assertEqual(new_currency, Currencies.get(new_currency.ticker))

        test_data = [
            (new_currency.name, new_currency.ticker,
             b'1BoatSLRHtKNngkdXEeobR76b53LETtpyT', 'main')
            ]
        for name, ticker, addr, net in test_data:
            with self.subTest(name=name, ticker=ticker, address=addr, net=net):
                res = coinaddr.validate(name, addr)
                self.assertEqual(name, res.name)
                self.assertEqual(ticker, res.ticker)
                self.assertEqual(addr, res.address)
                self.assertEqual(True, res.valid)
                self.assertEqual(net, res.network)

            with self.subTest(name=name, ticker=ticker, address=addr, net=net):
                res = coinaddr.validate(ticker, addr)
                self.assertEqual(name, res.name)
                self.assertEqual(ticker, res.ticker)
                self.assertEqual(addr, res.address)
                self.assertEqual(True, res.valid)
                self.assertEqual(net, res.network)

    def test_extending_validator(self):
        class NewValidator(ValidatorBase):
            name = 'new'
            networks = 'testing'

            def validate(self):
                return True

        validator = Validators.get('new')
        self.assertEqual(NewValidator, validator)


if __name__ == '__main__':
    unittest.main()
