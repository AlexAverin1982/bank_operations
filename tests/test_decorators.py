import os.path

import pytest

from src.decorators import log
from src.masks import get_mask_card_number

par_dir = os.path.abspath(os.path.join(__file__, os.pardir))
par_dir = os.path.abspath(os.path.join(par_dir, os.pardir))
log_filename = os.path.join(par_dir, "logs", "decorator.log")


@log()
def logged_get_mask_card_number(card_number: int) -> str:
    return get_mask_card_number(card_number)


@log(log_filename)
def get_mask_card_number_logged_to_file(card_number: int) -> str:
    return get_mask_card_number(card_number)


def test_log_decorator_1(capsys: pytest.CaptureFixture) -> None:
    result = logged_get_mask_card_number(1234567890123456)
    captured = capsys.readouterr()
    assert (
        (result == "1234 56** **** 3456")
        and (captured[0].find(" ok\n") > 0)
        and (captured[0].find("\nResult is") > 0)
    )


def test_log_decorator_2(capsys: pytest.CaptureFixture) -> None:
    # with pytest.raises(Exception, match="Номер карты - 16 цифр"):
    result = logged_get_mask_card_number(123456789012345678)
    captured = capsys.readouterr()
    passed = (
        (result is None)
        and (captured[0].find("error: ") > 0)
        and (captured[0].find("Номер карты - 16 цифр") > 0)
    )
    assert passed


def test_log_decorator_3(capsys: pytest.CaptureFixture) -> None:
    result = logged_get_mask_card_number(card_number=123456789012345678)
    captured = capsys.readouterr()
    passed = (
        (result is None)
        and (captured[0].find("error: ") > 0)
        and (captured[0].find("Номер карты - 16 цифр") > 0)
    )
    assert passed


def test_log_to_file_decorator_1() -> None:
    result = get_mask_card_number_logged_to_file(1234567890123456)
    log_file_exists = os.path.exists(log_filename)
    passed = False
    if log_file_exists:
        with open(log_filename, "r") as f:
            lines = f.read()
            passed = (lines.find("get_mask_card_number") >= 0) and (
                lines.find("1234 56** **** 3456") > 0
            )

    assert passed and (result == "1234 56** **** 3456")
