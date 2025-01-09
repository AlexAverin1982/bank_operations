import json
import os.path

from src.external_api import convert_currencies


def load_ops_from_json_file(filename: str) -> list[dict]:
    """функция принимает на вход путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях"""
    result = []
    if os.path.exists(filename) and os.path.isfile(filename):
        try:
            with open(filename, encoding="utf-8") as f:
                result = json.load(f)
        except json.JSONDecodeError:
            result = []
    return result


def transaction_amount(transaction: dict, target_cur_code: str = "RUB") -> float:
    """принимает на вход транзакцию и возвращает сумму транзакции (amount)
    в рублях (по умолчанию) или в другой указанной валюте"""
    op_amount = transaction.get("operationAmount", {})
    if op_amount:
        currency = op_amount.get("currency", {})
        amount = op_amount.get("amount")
        if amount:
            amount = float(amount)
            cur_code = currency.get("code")
            if cur_code:
                if cur_code != target_cur_code:
                    result = convert_currencies(cur_code, target_cur_code, amount)
                    if result != 0:
                        return result
                    else:
                        raise ValueError("Код валюты транзакции указан неверно")
                else:
                    return float(amount)
            else:
                raise ValueError("Транзакция содержит неполные данные")
        else:
            raise ValueError("Транзакция содержит неполные данные")
    else:
        raise ValueError("Транзакция содержит неполные данные")


# d = load_ops_from_json_file(u'..\data\operations.json')
