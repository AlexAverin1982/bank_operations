from random import randint

import pytest

from src.generators import (card_number_generator, filter_by_currency,
                            transaction_descriptions)
from tests.conftest import currencies


def test_filter_by_currency(random_transactions: list[dict]) -> None:
    rnd_currency: str = str(currencies[randint(0, len(currencies) - 1)])
    filtered_transactions = filter_by_currency(random_transactions, rnd_currency)

    passed = True
    for transaction in filtered_transactions:
        op_am = transaction.get("operationAmount", {"currency": {}})
        currency_data = op_am.get("currency", {"code": ""})
        passed = currency_data.get("code", "") == rnd_currency

    assert passed


def test_filter_by_nonexistent_currency(random_transactions: list[dict]) -> None:
    filtered_transactions = filter_by_currency(random_transactions, "Dollar")
    passed = False
    try:
        next(filtered_transactions)
    except StopIteration:
        passed = True

    assert passed


def test_filter_by_currency_empty_list() -> None:
    filtered_transactions = filter_by_currency([], "USD")
    passed = False
    try:
        next(filtered_transactions)
    except StopIteration:
        passed = True

    assert passed


@pytest.mark.parametrize(
    "transactions, expected_iterations_count",
    [
        ([{}], 0),
        ([{"operationAmount": {"currency": {"a": ""}}}], 0),
        ([{"operationAmount": {"currency": {"code": "USD"}}}], 1),
    ],
)
def test_invalid_transactions_filter_by_currency(
    transactions: list[dict], expected_iterations_count: int
) -> None:
    filtered_transactions = filter_by_currency(transactions, "USD")
    iterations_count = 0
    may_go = True
    while may_go:
        try:
            next(filtered_transactions)
            iterations_count += 1
        except StopIteration:
            may_go = False

    assert iterations_count == expected_iterations_count


def test_transaction_descriptions(random_transactions: list[dict]) -> None:
    descriptions = transaction_descriptions(random_transactions)
    passed = True
    for i, description in enumerate(descriptions):
        passed = description == random_transactions[i].get("description", "")

    assert passed


def test_empty_transaction_descriptions() -> None:
    descriptions = transaction_descriptions([])
    assert len(list(descriptions)) == 0


@pytest.mark.parametrize(
    "start_no, end_no, expected",
    [
        (
            10500,
            10504,
            [
                "0000 0000 0001 0500",
                "0000 0000 0001 0501",
                "0000 0000 0001 0502",
                "0000 0000 0001 0503",
                "0000 0000 0001 0504",
            ],
        )
    ],
)
def test_card_number_generator(start_no: int, end_no: int, expected: list[str]) -> None:
    passed = True
    for i, card_no in enumerate(card_number_generator(start_no, end_no)):
        passed = expected[i] == card_no
    assert passed


@pytest.mark.parametrize(
    "start_no, expected", [(9999999999999999, ["9999 9999 9999 9999"])]
)
def test_last_card_number(start_no: int, expected: list[str]) -> None:
    passed = True
    for i, card_no in enumerate(card_number_generator(start_no)):
        passed = expected[i] == card_no
    assert passed
