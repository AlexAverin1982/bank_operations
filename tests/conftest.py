from random import randint

import pytest


@pytest.fixture()
def random_card_number(number_length: int = 16) -> int:
    """фикстура номеров банковских карт"""
    result = ""
    for i in range(number_length):
        result += str(randint(0, 9))
    return int(result)


@pytest.fixture()
def random_bank_account_number(number_length: int = 20) -> int:
    """фикстура номеров банковских счетов"""
    result = ""
    for i in range(number_length):
        result += str(randint(0, 9))
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
