import json
import random
from unittest.mock import patch, Mock

# from src.external_api import convert_currencies
from src.utils import load_ops_from_json_file

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
    data = load_ops_from_json_file(r'..\data\operations.json')
    assert len(data) > 0


def test_load_invalid_json_file() -> None:
    data = load_ops_from_json_file(r'..\data\operations_invalid.json')
    assert data == []


def test_load_nonexistant_json_file() -> None:
    data = load_ops_from_json_file(r'..\invalid_path\operations_invalid.json')
    assert data == []


def test_mock_loading_json_file() -> None:
    mock_load_json_file_with_single_data_item = Mock(return_value=[{"id": 441945886,
                                                                    "state": "EXECUTED",
                                                                    "date": "2019-08-26T10:50:58.294041", }])
    # redirecting testing func execution to mock object
    load_ops_from_json_file = mock_load_json_file_with_single_data_item
    mocking_data = load_ops_from_json_file('test.txt')
    assert mocking_data[0]["id"] == 441945886
    mock_load_json_file_with_single_data_item.assert_called()



def convert_USD_to_RUB(amount: float) -> float:
    from src import external_api
    return external_api.convert_currencies('USD', 'RUB', amount)


def test_currency_convertion_patched() -> None:
    rand_transaction = get_random_transaction(cur_code='USD')
    amount = float(rand_transaction['operationAmount']['amount'])
    with patch('src.external_api.convert_currencies') as mock_func:
        expected = mock_func.return_value = 100 * amount
        result = convert_USD_to_RUB(amount)
        assert expected == result
        mock_func.assert_called_once_with('USD', 'RUB', amount)
