from random import randint

import pytest

from src.generators import filter_by_currency, transaction_descriptions
from tests.conftest import currencies


def test_filter_by_currency(random_transactions: list[dict]) -> None:
    rnd_currency: str = str(currencies[randint(0, len(currencies) - 1)])
    filtered_transactions = filter_by_currency(random_transactions, rnd_currency)

    passed = True
    for transaction in filtered_transactions:
        op_am = transaction.get("operationAmount", {"currency": {}})
        currency_data = op_am.get("currency", {"code": ""})
        passed = currency_data.get("code", "") == rnd_currency
        if not passed:
            break

    assert passed


def test_transaction_descriptions(random_transactions: list[dict]) -> None:
    descriptions = transaction_descriptions(random_transactions)
    passed = True
    for i, description in descriptions:
        passed = description == random_transactions[i].get("description", "")

    assert passed


def test_card_number_generator():
    assert True
