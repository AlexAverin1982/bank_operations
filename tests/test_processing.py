from random import randint

import pytest

from src.processing import filter_by_state, sort_by_date


def test_filter_by_state(test_data_for_processing: list[dict]) -> None:
    data = test_data_for_processing
    test_state = test_data_for_processing[randint(0, len(data) - 1)].get("state")
    result = filter_by_state(data, str(test_state))
    passed = True
    for item in result:
        passed = passed and (item.get("state") == test_state)
    assert passed


def test_filter_by_nonexistent_state(test_data_for_processing: list[dict]) -> None:
    assert filter_by_state(test_data_for_processing, 'vjqnevc;qvniu3') == []


def test_sort_by_date(test_data_for_processing: list[dict]) -> None:
    result = sort_by_date(test_data_for_processing)
    passed = True

    for i in range(1, len(result)):
        date0 = result[i - 1].get("date", '')
        date1 = result[i].get("date", '')
        passed = date0 >= date1

    assert passed


def test_sort_by_date_ascending_order(test_data_for_processing: list[dict]) -> None:
    result = sort_by_date(test_data_for_processing, desc_order=False)
    passed = True

    for i in range(1, len(result)):
        date0 = result[i - 1].get("date", '')
        date1 = result[i].get("date", '')
        passed = date0 <= date1

    assert passed


@pytest.mark.parametrize("data, state, expected", [
    ([{"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
      {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
      {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
      {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
      {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
      {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"}], 'CANCELED',
     [{"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
      {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"}]
     )
])
def test_processing_parametrized(data, state, expected):
    result = filter_by_state(data, state)
    passed = len(expected) == len(result)
    for item in result:
        passed = passed and (item in expected)
    assert passed
