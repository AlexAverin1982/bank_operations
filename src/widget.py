# type: ignore
from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(id_string: str) -> str:
    """функция получает номер счета или карты и маскирует его"""
    data = id_string.split()
    if str(data[0]).lower().strip().startswith("счет"):
        data[-1] = get_mask_account(int(data[-1]))
    else:
        data[-1] = get_mask_card_number(int(data[-1]))
    return " ".join(data)


def get_date(input_date: str) -> str:
    """возвращает строку с датой, меняя формат"""
    result = input_date.split("T")[0].split("-")
    return "{}.{}.{}".format(result[2], result[1], result[0])


# if __name__ == "__main__":
#     print(mask_account_card("Visa Platinum 7000792289606361"))
#     print(mask_account_card("Maestro 7000792289606361"))
#     print(mask_account_card("Счет 73654108430135874305"))
#
#     test_data = [
#         "Maestro 1596837868705199",
#         "Счет 64686473678894779589",
#         "MasterCard 7158300734726758",
#         "Счет 35383033474447895560",
#         "Visa Classic 6831982476737658",
#         "Visa Platinum 8990922113665229",
#         "Visa Gold 5999414228426353",
#         "Счет 73654108430135874305",
#     ]
#
#     for example in test_data:
#         print(mask_account_card(example))
#     print("-" * 10)
#     print(get_date("2024-03-11T02:26:18.671407"))
