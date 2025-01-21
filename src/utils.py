import json
import logging
import os.path

from src.external_api import convert_currencies

par_dir = os.path.abspath(os.path.join(__file__, os.pardir))
par_dir = os.path.abspath(os.path.join(par_dir, os.pardir))
utils_log_filename = os.path.join(par_dir, "logs", "utils.log")

logging.basicConfig(level=logging.DEBUG, filemode="w", encoding="utf-8")
utils_logger = logging.getLogger("utils_logger")
utils_logger.setLevel(logging.CRITICAL)
utils_log_handler = logging.FileHandler(filename=utils_log_filename, encoding="utf-8")
""" Формат записи логов включает метку времени, название модуля, уровень серьезности и сообщение. """
utils_log_formatter = logging.Formatter(
    "%(asctime)s %(levelname)s in module %(filename)s: %(message)s"
)
utils_log_handler.setFormatter(utils_log_formatter)
utils_logger.addHandler(utils_log_handler)


def load_ops_from_json_file(filename: str) -> list[dict]:
    """функция принимает на вход путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях"""
    result = []
    if os.path.exists(filename) and os.path.isfile(filename):
        try:
            with open(filename, encoding="utf-8") as f:
                result = json.load(f)
            utils_logger.info(f"файл {filename} с данными операций загружен успешно")
        except json.JSONDecodeError as ex:
            result = []
            utils_logger.error(ex)
    else:
        utils_logger.error(f"файл {filename} не найден")
    return result


def extract_amount_from(transaction: dict) -> float:
    """извлекает объем транзакции в исходной валюте"""
    op_amount = transaction.get("operationAmount", {})
    if op_amount:
        utils_logger.info("данные о транзакции загружены успешно")
        amount = op_amount.get("amount")
        if amount:              # and amount.isnumeric():
            utils_logger.info("размер транзакции определен успешно")
            return float(amount)
        else:
            utils_logger.error("данные о транзакции в валюте не найдены")
            raise ValueError("Транзакция содержит неполные данные")
    else:
        amount = transaction.get("amount", "")
        if amount and amount.isnumeric():
            return float(amount)
        else:
            utils_logger.error("данные о размере транзакции не найдены")
            raise ValueError("Транзакция содержит неполные данные")


def get_currency_code(transaction: dict) -> str:
    """принимает на вход транзакцию и возвращает код валюты"""
    op_amount = transaction.get("operationAmount", {})
    if op_amount:
        currency = op_amount.get("currency", {})
        return currency.get("name", "")
    else:
        currency = transaction.get("currency_code", "")
        if currency:
            return currency
        else:
            utils_logger.error("данные о размере транзакции не найдены")
            raise ValueError("Транзакция содержит неполные данные")


def get_currency_name(transaction: dict) -> str:
    """принимает на вход транзакцию и возвращает имя валюты"""
    op_amount = transaction.get("operationAmount", {})
    if op_amount:
        currency = op_amount.get("currency", {})
        return currency.get("name", "")
    else:
        currency = transaction.get("currency_name", "")
        if currency:
            return str(currency)
        else:
            utils_logger.error("данные о размере транзакции не найдены")
            raise ValueError("Транзакция содержит неполные данные")


def transaction_amount(transaction: dict, target_cur_code: str = "RUB") -> float:
    """принимает на вход транзакцию и возвращает сумму транзакции (amount)
    в рублях (по умолчанию) или в другой указанной валюте"""
    amount = extract_amount_from(transaction)
    if amount:
        utils_logger.info("данные о транзакции загружены успешно")
        currency_code = get_currency_code(transaction)
        if currency_code != target_cur_code:
            result = convert_currencies(currency_code, target_cur_code, amount)
            if result != 0:
                utils_logger.info(
                    f"валюта {currency_code} переконвертирована в {target_cur_code} успешно"
                )
                return result
            else:
                utils_logger.error(f"Код валюты {currency_code} транзакции указан неверно")
                raise ValueError(f"Код валюты {currency_code} транзакции указан неверно")
        else:
            utils_logger.info("размер транзакции определен успешно")
            return float(amount)
    else:
        utils_logger.error("данные о размере транзакции не найдены")
        raise ValueError("Транзакция содержит неполные данные")


# d = load_ops_from_json_file(u'..\data\operations.json')
