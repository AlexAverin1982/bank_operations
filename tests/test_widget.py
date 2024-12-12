import pytest

from src.widget import get_date, mask_account_card


@pytest.mark.parametrize(
    "test_string, expected_mask",
    [
        ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
        ("Счет 64686473678894779589", "Счет **9589"),
        ("MasterCard 7158300734726758", "MasterCard 7158 30** **** 6758"),
        ("Счет 35383033474447895560", "Счет **5560"),
        ("Visa Classic 6831982476737658", "Visa Classic 6831 98** **** 7658"),
        ("Visa Platinum 8990922113665229", "Visa Platinum 8990 92** **** 5229"),
        ("Visa Gold 5999414228426353", "Visa Gold 5999 41** **** 6353"),
        ("Счет 73654108430135874305", "Счет **4305"),
    ],
)
def test_mask_account_card(test_string: str, expected_mask: str) -> None:
    assert mask_account_card(test_string) == expected_mask


def test_invalid_cards_data() -> None:
    with pytest.raises(ValueError):
        mask_account_card("")


def test_invalid_cards_data1() -> None:
    with pytest.raises(TypeError):
        mask_account_card(123)


def test_invalid_cards_data2() -> None:
    with pytest.raises(ValueError):
        mask_account_card("123")


def test_get_date(test_date: str) -> None:
    assert (
        get_date(test_date)
        == test_date[8:10] + "." + test_date[5:7] + "." + test_date[:4]
    )


def test_invalid_date() -> None:
    with pytest.raises(TypeError):
        get_date(123)


def test_invalid_date1() -> None:
    with pytest.raises(ValueError):
        get_date("123")


def test_invalid_date2() -> None:
    with pytest.raises(ValueError):
        get_date("")


def test_invalid_date3() -> None:
    with pytest.raises(ValueError):
        get_date("2024-03-11-02-26:18.671407")


def test_invalid_date4() -> None:
    with pytest.raises(ValueError):
        get_date("--")


def test_invalid_date5() -> None:
    with pytest.raises(ValueError):
        get_date("2024-43-11-02-26:18.671407")


def test_invalid_date6() -> None:
    with pytest.raises(ValueError):
        get_date("2024-12-32-02-26:18.671407")


def test_date11() -> None:
    assert get_date("1452-08-15T01:0410.799498") == "15.08.1452"
