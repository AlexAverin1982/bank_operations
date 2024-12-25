from typing import Any, Generator


def filter_by_currency(transactions: list[dict], currency: str) -> filter:
    """Функция возвращает итератор, который поочередно выдает транзакции,
    где валюта операции соответствует заданной (например, USD)."""
    return filter(
        lambda x: x.get("operationAmount", {"currency": {"code": ""}})
        .get("currency", {"code": ""})
        .get("code", "")
        == currency,
        transactions,
    )


def transaction_descriptions(transactions: list[dict]) -> Generator:
    """генератор принимает на вход список словарей с транзакциями и возвращает описание каждой операции по очереди"""
    for x in transactions:
        yield x.get("description", "")


def np(number: int, order: int) -> str:
    """часть номера карты number, order = 1-4"""
    result = ("0" * 16 + str(number))[-16:]
    return result[(order - 1) * 4: order * 4]


def card_number_generator(
    start: int = 1, stop: int = 9999999999999999
) -> Generator[str, Any, None]:
    """генератор выдает номера банковских карт в формате XXXX XXXX XXXX XXXX,
    где X — цифра номера карты.
    Генератор может сгенерировать номера карт в заданном диапазоне от 0000 0000 0000 0001 до 9999 9999 9999 9999.
    Генератор должен принимать начальное и конечное значения для генерации диапазона номеров.
    """
    return (
        f"{np(i, 1)} {np(i, 2)} {np(i, 3)} {np(i, 4)}" for i in range(start, stop + 1)
    )
