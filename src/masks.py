import logging
import os.path

par_dir = os.path.abspath(os.path.join(__file__, os.pardir))
par_dir = os.path.abspath(os.path.join(par_dir, os.pardir))
masks_log_filename = os.path.join(par_dir, "logs", "masks.log")

# Основная конфигурация logging
logging.basicConfig(level=logging.DEBUG, filemode="w")
masks_logger = logging.getLogger("masks_logger")
masks_logger.setLevel(logging.DEBUG)
masks_log_handler = logging.FileHandler(filename=masks_log_filename)
""" Формат записи логов включает метку времени, название модуля, уровень серьезности и сообщение """
masks_log_formatter = logging.Formatter(
    "%(asctime)s %(levelname)s in module %(filename)s: %(message)s"
)
masks_log_handler.setFormatter(masks_log_formatter)
masks_logger.addHandler(masks_log_handler)


def get_mask_card_number(card_number: int) -> str:
    """функция принимает на вход номер банковской карты в виде числа и возвращает строку с замаскированным номером"""
    if not isinstance(card_number, int):
        masks_logger.error(
            f"{card_number} не является номером карты, не состоит из 16 цифр"
        )
        raise TypeError("Номер карты - 16 цифр")
    if len(str(card_number)) != 16:
        masks_logger.error(
            f"номер карты {card_number} содержит меньше или больше 16 цифр"
        )
        raise ValueError("Номер карты - 16 цифр")

    masks_logger.info("номер карты замаскирован успешно")
    return (
        str(card_number)[:4]
        + " "
        + str(card_number)[4:6]
        + "** **** "
        + str(card_number)[-4:]
    )


def get_mask_account(account_no: int) -> str:
    """функция принимает на вход номер банковского счета в виде числа и возвращает строку с замаскированным номером"""
    if not isinstance(account_no, int):
        masks_logger.error(
            f"{account_no} не является номером счета, не состоит из 20 цифр"
        )
        raise TypeError("Номер счета - 20 цифр")
    if len(str(account_no)) != 20:
        masks_logger.error(
            f"номер счета {account_no} содержит меньше или больше 20 цифр"
        )
        raise ValueError("Номер счета - 20 цифр")
    masks_logger.info("номер счета замаскирован успешно")
    return "**" + str(account_no)[-4:]
