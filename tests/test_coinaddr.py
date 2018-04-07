import unittest

import coinaddr


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


class TestCoinAddr(unittest.TestCase):
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


if __name__ == '__main__':
    unittest.main()
