import json
import logging
import os.path

from src.external_api import convert_currencies

par_dir = os.path.abspath(os.path.join(__file__, os.pardir))
par_dir = os.path.abspath(os.path.join(par_dir, os.pardir))
utils_log_filename = os.path.join(par_dir, "logs", "utils.log")

logging.basicConfig(level=logging.DEBUG, filemode="w", encoding="utf-8")
utils_logger = logging.getLogger("utils_logger")
utils_logger.setLevel(logging.DEBUG)
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


def transaction_amount(transaction: dict, target_cur_code: str = "RUB") -> float:
    """принимает на вход транзакцию и возвращает сумму транзакции (amount)
    в рублях (по умолчанию) или в другой указанной валюте"""
    op_amount = transaction.get("operationAmount", {})
    if op_amount:
        utils_logger.info("данные о транзакции загружены успешно")
        currency = op_amount.get("currency", {})
        amount = op_amount.get("amount")
        if amount:
            amount = float(amount)
            cur_code = currency.get("code")
            if cur_code:
                if cur_code != target_cur_code:
                    result = convert_currencies(cur_code, target_cur_code, amount)
                    if result != 0:
                        utils_logger.info(
                            f"валюта {cur_code} переконвертирована в {target_cur_code} успешно"
                        )
                        return result
                    else:
                        utils_logger.error("Код валюты транзакции указан неверно")
                        raise ValueError("Код валюты транзакции указан неверно")
                else:
                    utils_logger.info("размер транзакции в рублях определен успешно")
                    return float(amount)
            else:
                utils_logger.error("данные о валюте не найдены")
                raise ValueError("Транзакция содержит неполные данные")
        else:
            utils_logger.error("данные о транзакции в валюте не найдены")
            raise ValueError("Транзакция содержит неполные данные")
    else:
        utils_logger.error("данные о размере транзакции не найдены")
        raise ValueError("Транзакция содержит неполные данные")


# d = load_ops_from_json_file(u'..\data\operations.json')
