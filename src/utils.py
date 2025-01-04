import json
import os.path


def load_ops_from_json_file(filename: str) -> list[dict]:
    """ функция принимает на вход путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях"""
    result = []
    if os.path.exists(filename) and os.path.isfile(filename):
        try:
            with open(filename) as f:
                result = json.load(f)
        except json.JSONDecodeError as e:
            result = []
    return result


def transaction_amount(transaction: dict, target_cur_code: str = 'RUB') -> float:
    """ принимает на вход транзакцию и возвращает сумму транзакции (amount)
    в рублях (по умолчанию) или в другой указанной валюте"""
    result = 0.0
    op_amount = transaction.get("operationAmount", {})
    currency = op_amount.get('currency', {})
    result = op_amount.get('amount', 0.0)
    cur_code = currency.get('code', '')
    if cur_code != target_cur_code:
        result = convert_currencies(cur_code, target_cur_code)
