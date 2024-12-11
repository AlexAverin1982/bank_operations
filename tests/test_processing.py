from random import randint

from src.processing import filter_by_state, sort_by_date


def test_filter_by_state(test_data_for_processing: list[dict]) -> None:
    data = test_data_for_processing
    test_state = test_data_for_processing[randint(0, len(data) - 1)].get("state")
    result = filter_by_state(data, str(test_state))
    passed = True
    for item in result:
        passed = passed and (item.get("state") == test_state)
    assert passed


def test_sort_by_date(test_data_for_processing: list[dict]) -> None:
    result = sort_by_date(test_data_for_processing)
    passed = True

    for i in range(1, len(result)):
        date0 = result[i - 1].get("date", '')
        date1 = result[i].get("date", '')
        passed = date0 >= date1

    assert passed
