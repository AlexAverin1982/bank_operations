import json
import os.path

from src.external_api import convert_currencies


def load_ops_from_json_file(filename: str) -> list[dict]:
    """ функция принимает на вход путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях"""
    result = []
    if os.path.exists(filename) and os.path.isfile(filename):
        try:
            with open(filename, encoding='utf-8') as f:
                result = json.load(f)
        except json.JSONDecodeError as e:
            result = []
    return result


def transaction_amount(transaction: dict, target_cur_code: str = 'RUB') -> float:
    """ принимает на вход транзакцию и возвращает сумму транзакции (amount)
    в рублях (по умолчанию) или в другой указанной валюте"""
    op_amount = transaction.get("operationAmount", {})
    currency = op_amount.get('currency', {})
    amount = float(op_amount.get('amount', 0.0))
    cur_code = currency.get('code', '')
    if cur_code != target_cur_code:
        return convert_currencies(cur_code, target_cur_code, amount)
    else:
        return amount


# d = load_ops_from_json_file(u'..\data\operations.json')
