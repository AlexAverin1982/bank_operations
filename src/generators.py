def filter_by_currency(transactions: list[dict], currency: str) -> filter:
    """ Функция возвращает итератор, который поочередно выдает транзакции,
    где валюта операции соответствует заданной (например, USD). """
    return \
        filter(
            lambda x:
            x.get("operationAmount", {"currency": {"", ""}}).get("currency", {"code": ""}).get("code", "") == currency,
            transactions)


def transaction_descriptions(transactions: list[dict]):
    """ генератор принимает на вход список словарей с транзакциями и возвращает описание каждой операции по очереди """
    return (x.get("description", "") for x in transactions)


def card_number_generator(operation: str):
    """"""
    pass
