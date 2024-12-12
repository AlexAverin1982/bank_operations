import pytest

from src.masks import get_mask_account, get_mask_card_number


def test_bank_cards_number_mask(random_card_number: int) -> None:
    result = get_mask_card_number(random_card_number)
    card_no = str(random_card_number)
    assert (
        (result[:4] == card_no[:4])
        and (result[5:7] == card_no[4:6])
        and (result[-4:] == card_no[-4:])
        and (result[7:15] == "** **** ")
    )


def test_bank_cards_number_maskqqq() -> None:
    with pytest.raises(ValueError):
        assert get_mask_card_number(466570763421305)


def test_bank_account_number_mask(random_bank_account_number: int) -> None:
    result = get_mask_account(random_bank_account_number)
    src_number = str(random_bank_account_number)

    assert (result[-4:] == src_number[-4:]) and (result[:2] == "**")


def test_incorrect_card_number1():
    with pytest.raises(ValueError):
        get_mask_card_number(123)


def test_incorrect_card_number2():
    with pytest.raises(TypeError):
        get_mask_card_number(123.4)


def test_incorrect_account_number1():
    with pytest.raises(ValueError):
        get_mask_account(123)


def test_incorrect_account_number2():
    with pytest.raises(TypeError):
        get_mask_account(1234.5)


def test_incorrect_account_number3():
    with pytest.raises(ValueError):
        get_mask_account(1812659170946368319)


