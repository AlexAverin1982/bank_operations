import random
from datetime import datetime, timedelta
from random import randint

import pytest

transaction_states = ["EXECUTED", "CANCELLED", "IN PROGRESS"]
currencies = ["USD", "RUR", "EUR", "CNY", "JPY"]
descriptions = [
    "Перевод организации",
    "Перевод со счета на счет",
    "Перевод с карты на карту",
]


def random_date(
    start_date_str: str,
    end_date_str: str,
    date_format: str = "%Y-%m-%d",
    output_format: str = "%Y-%m-%dT%X",
) -> str:
    start_date = datetime.strptime(start_date_str, date_format)
    end_date = datetime.strptime(end_date_str, date_format)
    delta = end_date - start_date
    days_difference = delta.days
    res_random_date = start_date + timedelta(days=randint(1, days_difference))
    return res_random_date.strftime(output_format) + f".{randint(100000, 999999)}"


@pytest.fixture()
def random_card_number(number_length: int = 16) -> int:
    """фикстура номеров банковских карт"""
    result = ""
    for i in range(number_length - 1):
        result += str(randint(0, 9))
    result = str(randint(1, 9)) + result
    return int(result)


@pytest.fixture()
def random_bank_account_number(number_length: int = 20) -> int:
    """фикстура номеров банковских счетов"""
    result = ""
    while len(result) < number_length - 1:
        result += str(randint(0, 9))
    result = str(randint(1, 9)) + result
    return int(result)


@pytest.fixture()
def test_data_for_processing() -> list[dict]:
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 93549570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 41428829, "state": "IN_PROGRESS", "date": "3019-07-03T18:35:29.512364"},
        {"id": 944719570, "state": "IN_PROGRESS", "date": "2018-06-30T02:08:58.425572"},
        {
            "id": 1345526727,
            "state": "IN_PROGRESS",
            "date": "2014-09-12T21:27:25.241689",
        },
        {
            "id": 6157765591,
            "state": "IN_PROGRESS",
            "date": "2018-10-14T08:21:33.419441",
        },
    ]


@pytest.fixture()
def test_date() -> str:
    return (
        str(randint(1000, 9999))
        + "-"
        + ("0" + str(randint(1, 12)))[-2:]
        + "-"
        + ("0" + str(randint(1, 28)))[-2:]
        + "T"
        + ("0" + str(randint(0, 23)))[-2:]
        + ":"
        + ("0" + str(randint(0, 59)))[-2:]
        + ":"
        + ("0" + str(randint(0, 59)))[-2:]
        + "."
        + ("000000" + str(randint(0, 999999)))[-6:]
    )


def get_random_transaction(cur_code: str = '') -> dict:
    if cur_code:
        rnd_currency = cur_code
    else:
        rnd_currency = random.choice(currencies)
    currency_dict = {"name": rnd_currency, "code": rnd_currency}
    amount_dict = {
        "amount": str(randint(100, 1000000)) + "." + str(randint(10, 99)),
        "currency": currency_dict,
    }
    return {
        "id": randint(100000000, 999999999),
        "state": transaction_states[randint(0, len(transaction_states) - 1)],
        "date": random_date("2015-01-01", "2025-01-01"),
        "operationAmount": amount_dict,
        "description": descriptions[randint(0, len(descriptions) - 1)],
        "from": "Счет " + str(random_bank_account_number),
        "to": "Счет " + str(random_bank_account_number),
    }


@pytest.fixture()
def random_transactions() -> list[dict]:
    result = []
    count = randint(5, 100)
    for i in range(count):
        rnd_transaction = get_random_transaction()
        result.append(rnd_transaction)

    return result
