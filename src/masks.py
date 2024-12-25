def get_mask_card_number(card_number: int) -> str:
    """функция принимает на вход номер банковской карты в виде числа и возвращает строку с замаскированным номером"""
    if not isinstance(card_number, int):
        raise TypeError("Номер карты - 16 цифр")
    if len(str(card_number)) != 16:
        raise ValueError("Номер карты - 16 цифр")

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
        raise TypeError("Номер счета - 20 цифр")
    if len(str(account_no)) != 20:
        raise ValueError("Номер счета - 20 цифр")
    return "**" + str(account_no)[-4:]
