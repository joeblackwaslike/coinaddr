import pytest

import coinaddr
from coinaddr.currency import Currencies, Currency
from coinaddr.validation import Validators, ValidatorBase


TEST_DATA = [
    (
        "bitcoin-segwit",
        "btc-segwit",
        b"bc1q9yl05qdyz7gvtnmrrrjc0x48q3dpq44vx5p9kz",
        "main",
    ),
    # (
    #     "monero",
    #     "xmr",
    #     b"48ViMS4gjCWV56U5BqyRs8PeoLTNP1GACLpbb55kdZUxMYd3JTdu3yRCLaTqcaaRp7Ux2tF5J91sT9X6rh4ftHH4DSQYDSC",
    #     "main",
    # ),
    # ("tether", "usdt", b"0x154985aD8A10AFe32bdF9CE08b8b9dcD082Db34d", "mai"),
    # ("ripple", "xrp", b"0x154985aD8A10AFe32bdF9CE08b8b9dcD082Db34d", "main"),
    # ("solana", "sol", b"D5ggQFWPkWimfxMQrvjiy2F7ptfv5FuEKuGq4oNjADbb", "main"),
    # (
    #     "cardano",
    #     "ada",
    #     b"addr1q9kfa9d6wpscp57yrpsag9zgxs9qsgu4axugf5tswvuf9znvn62m5urpsrfugxrp6s2ysdq2pq3et6dcsnghquecj29qt8lvck",
    #     "main",
    # ),
    # ("tron", "trx", b"TABx6Xc5DMJAUuR1qhxeb5Y4yRgZESnCjf", "main"),
    # ("stellar", "xlm", b"TABx6Xc5DMJAUuR1qhxeb5Y4yRgZESnCjf", "main"),
    # ("polygon", "pol", b"0x154985aD8A10AFe32bdF9CE08b8b9dcD082Db34d", "main"),
    # ("zcash", "zce", b"t1chzxWWFU3bUw1PCSYxTXM8uTutuCsUzSi", "main"),
    ("bitcoin", "btc", b"1BoatSLRHtKNngkdXEeobR76b53LETtpyT", "main"),
    ("bitcoin", "btc", b"n2nzi7xDTrMVK9stGpbK3BtrpBCJfH7LRQ", "test"),
    ("bitcoin", "btc", b"3QJmV3qfvL9SuYo34YihAf3sRCW3qSinyC", "main"),
    ("bitcoin-cash", "bch", b"1BoatSLRHtKNngkdXEeobR76b53LETtpyT", "main"),
    ("bitcoin-cash", "bch", b"n2nzi7xDTrMVK9stGpbK3BtrpBCJfH7LRQ", "test"),
    ("bitcoin-cash", "bch", b"3QJmV3qfvL9SuYo34YihAf3sRCW3qSinyC", "main"),
    ("litecoin", "ltc", b"LeF6vC9k1qfFDEj6UGjM5e4fwHtiKsakTd", "main"),
    ("litecoin", "ltc", b"mkwV3DZkgYwKaXkphBtcXAjsYQEqZ8aB3x", "test"),
    # ("litecoin-segwit", "ltc-segwit", b"LYZMkaZUMa9oQ5d1vpvaatzdhztLcz7tk7", "main"),
    ("neocoin", "neo", b"AL9fzczwjV6ynoFAJVz4fBDu4NYLG6MBwm", "both"),
    ("dogecoin", "doge", b"DAnBU2rLkUgQb1ZLBJd6Bm5pZ45RN4TQC4", "main"),
    ("dogecoin", "doge", b"njscgXBB3HUUTXH7njim1Uw82PF9da4R8k", "test"),
    ("dashcoin", "dash", b"XsVkhTxLjzdXP1xZWtEFRj1mDhWcU6d8tE", "main"),
    ("dashcoin", "dash", b"yPv7h2i8v3dJjfSH4L3x91JSJszjdbsJJA", "test"),
    ("ether-zero", "etz", b"900ff070d37657cdf8016bca0d60cb493ebf7f83", "both"),
    ("ethereum", "eth", b"0x154985aD8A10AFe32bdF9CE08b8b9dcD082Db34d", "both"),
    ("ethereum-classic", "etc", b"0x7BC75Dd175D91aE9fbC8a8280056d6D77f90c5f9", "both"),
]


class TestCoinaddr:
    @pytest.mark.parametrize("name, ticker, address, network", TEST_DATA)
    def test_validation_by_name(self, name, ticker, address, network):
        result = coinaddr.validate(name, address)

        assert result.name == name
        assert result.ticker == ticker
        assert result.address == address
        assert result.valid == True
        assert result.network == network

    @pytest.mark.parametrize("name, ticker, address, network", TEST_DATA)
    def test_validation_by_ticker(self, name, ticker, address, network):
        result = coinaddr.validate(ticker, address)

        assert result.name == name
        assert result.ticker == ticker
        assert result.address == address
        assert result.valid == True
        assert result.network == network

    @pytest.mark.parametrize("name, ticker, address, network", TEST_DATA)
    def test_validation_from_text(self, name, ticker, address, network):
        result = coinaddr.validate(name, address.decode())

        assert result.name == name
        assert result.ticker == ticker
        assert result.address == address
        assert result.valid == True
        assert result.network == network


class TestExtendingCoinaddr:
    def test_extending_currency(self):
        new_currency = Currency(
            "testcoin",
            ticker="ttc",
            validator="Base58Check",
            networks=dict(main=(0x00, 0x05), test=(0x6F, 0xC4)),
        )

        assert new_currency == Currencies.get(new_currency.name)
        assert new_currency == Currencies.get(new_currency.ticker)

    def test_extending_validator(self):
        class NewValidator(ValidatorBase):
            name = "new"
            networks = "testing"

            def validate(self):
                return True

        validator = Validators.get("new")
        assert NewValidator == validator
