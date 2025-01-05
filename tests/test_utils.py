import os
import random
from unittest.mock import Mock, patch

# from src.external_api import convert_currencies
import pytest

from src.external_api import convert_currencies, get_currency_rate
from src.utils import load_ops_from_json_file, transaction_amount
# def read_file(filename):
#     with open(filename, 'r') as f:
#         return json.load(f)
#
#
# @patch('builtins.open', create=False)
# def test_read_empty_file(mock_open):
#     mock_file = mock_open.return_value.__enter__.return_value
#     mock_file.read.return_value = ''
#     assert load_ops_from_json_file('test.txt') == []
#     mock_open.assert_called_once_with('test.txt', 'r')
from tests.conftest import get_random_transaction


def test_load_valid_json_file() -> None:
    par_dir = os.path.abspath(os.path.join(__file__, os.pardir))
    par_dir = os.path.abspath(os.path.join(par_dir, os.pardir))
    filename = os.path.join(par_dir, "data", "operations.json")
    data = load_ops_from_json_file(filename)
    assert len(data) > 0


def test_load_invalid_json_file() -> None:
    data = load_ops_from_json_file(r"..\data\operations_invalid.json")
    assert data == []


def test_load_nonexistant_json_file() -> None:
    data = load_ops_from_json_file(r"..\invalid_path\operations_invalid.json")
    assert data == []


def test_mock_loading_json_file() -> None:
    mock_load_json_file_with_single_data_item = Mock(
        return_value=[
            {
                "id": 441945886,
                "state": "EXECUTED",
                "date": "2019-08-26T10:50:58.294041",
            }
        ]
    )
    # redirecting testing func execution to mock object
    load_ops_from_json_file = mock_load_json_file_with_single_data_item
    mocking_data = load_ops_from_json_file("test.txt")
    assert mocking_data[0]["id"] == 441945886
    mock_load_json_file_with_single_data_item.assert_called()


def convert_USD_to_RUB(amount: float) -> float:
    from src import external_api

    return external_api.convert_currencies("USD", "RUB", amount)


def test_currency_convertion_patched() -> None:
    rand_transaction = get_random_transaction(cur_code="USD")
    amount = float(rand_transaction["operationAmount"]["amount"])
    with patch("src.external_api.convert_currencies") as mock_func:
        expected = mock_func.return_value = 100 * amount
        result = convert_USD_to_RUB(amount)
        assert expected == result
        mock_func.assert_called_once_with("USD", "RUB", amount)


def test_USD_rate() -> None:
    result = get_currency_rate("USD")
    assert float(result.get("rate", "0")) > 0


def test_RUB_rate() -> None:
    with pytest.raises(ValueError) as e:
        get_currency_rate("RUB")
    assert str(e.value) == "Данные по этой валюте отсутствуют"


def test_convert_currencies() -> None:
    assert convert_currencies("RUB", "USD", 100) > 0


def test_transaction_amount(random_transactions: list[dict]) -> None:
    result = transaction_amount(random.choice(random_transactions), "RUB")
    assert result > 0


def test_transaction_amount2(random_transactions: list[dict]) -> None:
    result = transaction_amount(random.choice(random_transactions), "EUR")
    assert result > 0


def test_invalid_transaction_amount(random_transactions: list[dict]) -> None:
    t = random.choice(random_transactions)
    del t["operationAmount"]
    with pytest.raises(ValueError) as e:
        transaction_amount(t, "RUB")
        assert str(e.value == "Транзакция содержит неполные данные")


def test_invalid_transaction_amount2(random_transactions: list[dict]) -> None:
    t = random.choice(random_transactions)
    del t["operationAmount"]["amount"]
    with pytest.raises(ValueError) as e:
        transaction_amount(t, "RUB")
        assert str(e.value == "Транзакция содержит неполные данные")


def test_invalid_transaction_currency(random_transactions: list[dict]) -> None:
    t = random.choice(random_transactions)
    t["operationAmount"]["currency"]["code"] = "XXX"
    with pytest.raises(ValueError) as e:
        transaction_amount(t, "RUB")
        assert str(e.value == "Код валюты транзакции указан неверно")
