def get_mask_card_number(card_number: int) -> str:
    """функция принимает на вход номер банковской карты в виде числа и возвращает строку с замаскированным номером"""
    return (
        str(card_number)[:4]
        + " "
        + str(card_number)[4:6]
        + "** **** "
        + str(card_number)[-4:]
    )


def get_mask_account(account_no: int) -> str:
    """функция принимает на вход номер банковского счета в виде числа и возвращает строку с замаскированным номером"""
    return "**" + str(account_no)[-4:]
