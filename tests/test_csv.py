import os.path
from unittest.mock import Mock, patch

import src.csv_tools
from src.csv_tools import load_ops_from_csv


def use_load_ops_from_csv_for_test_file(filename: str) -> list[dict]:
    from src import csv_tools

    return csv_tools.load_ops_from_csv(filename)


def test_patch_load_csv_file() -> None:
    with patch("src.csv_tools.load_ops_from_csv") as mock_func:
        expected = [{"id": "001", "name": "John", "age": "30"}]
        mock_func.return_value = expected
        # mock_file.read.return_value = 'id,name,age\n001,John,30'
        result = use_load_ops_from_csv_for_test_file("test.csv")
        assert result == expected
        mock_func.assert_called_once_with("test.csv")


def test_mock_load_csv_file() -> None:
    expected = [{"id": "001", "name": "John", "age": "30"}]
    mock_func = Mock(return_value=expected)
    src.csv_tools.load_ops_from_csv = mock_func
    result = use_load_ops_from_csv_for_test_file("test.csv")
    assert result == expected
    # mock_func.assert_called_once_with('test.csv')


# def test_read_empty_file(mock_open):
#     mock_file = mock_open.return_value.__enter__.return_value
#     mock_file.read.return_value = ''
#     assert load_ops_from_json_file('test.txt') == []
#     mock_open.assert_called_once_with('test.txt', 'r')


def test_load_csv() -> None:
    par_dir = os.path.abspath(os.path.join(__file__, os.pardir))
    par_dir = os.path.abspath(os.path.join(par_dir, os.pardir))
    filename = os.path.join(par_dir, "data", "transactions.csv")
    data = load_ops_from_csv(filename, delimiter=";")
    assert data


def test_load_nonexistent_csv() -> None:
    assert load_ops_from_csv("", delimiter=";") == []
