import os.path
from unittest.mock import Mock, patch

import src.excel_tools
from src.excel_tools import load_ops_from_xlsx


def test_load_xlsx() -> None:
    par_dir = os.path.abspath(os.path.join(__file__, os.pardir))
    par_dir = os.path.abspath(os.path.join(par_dir, os.pardir))
    filename = os.path.join(par_dir, "data", "transactions_excel.xlsx")

    assert load_ops_from_xlsx(filename)


def test_load_nonexistent_xlsx() -> None:
    assert load_ops_from_xlsx("") == []


def use_load_ops_from_xlsx_for_test_file(filename: str) -> list[dict]:
    from src import excel_tools

    return excel_tools.load_ops_from_xlsx(filepath=filename)


def test_patch_load_xlsx_file() -> None:
    with patch("src.excel_tools.load_ops_from_xlsx") as mock_func:
        expected = [{"id": "001", "name": "John", "age": "30"}]
        mock_func.return_value = expected
        # mock_file.read.return_value = 'id,name,age\n001,John,30'
        result = use_load_ops_from_xlsx_for_test_file("test.xlsx")
        assert result == expected
        mock_func.assert_called_once_with(filepath="test.xlsx")


def test_mock_load_xlsx_file() -> None:
    expected = [{"id": "001", "name": "John", "age": "30"}]
    mock_func = Mock(return_value=expected)
    src.excel_tools.load_ops_from_xlsx = mock_func
    result = use_load_ops_from_xlsx_for_test_file("test.xlsx")
    assert result == expected
    # mock_func.assert_called_once_with('test.xlsx')
