import os.path

from src.generators import filter_by_currency, filter_by_currency2
from src.masks import get_masked_account_or_card
from src.processing import filter_by_state, sort_by_date
from src.re_tools import find_matches_in_description
from src.utils import get_currency_code, get_currency_name, transaction_amount
from src.widget import get_date


def show_main_menu() -> int:
    """главное меню программы"""

    print("Выберите необходимый пункт меню:")
    print("1. Получить информацию о транзакциях из JSON-файла")
    print("2. Получить информацию о транзакциях из CSV-файла")
    print("3. Получить информацию о транзакциях из XLSX-файла")

    user_choise = input("Ваш выбор: ")
    if user_choise.isdigit():
        user_choise = int(user_choise)
    else:
        user_choise = 0
    if user_choise == 1:
        print("Для обработки выбран JSON-файл.")
    elif user_choise == 2:
        print("Для обработки выбран CSV-файл.")
    elif user_choise == 3:
        print("Для обработки выбран XLSX-файл.")
    else:
        print("Программа завершает свою работу")

    return user_choise


def show_select_status_menu() -> str:
    """меню выбора статуса отображаемых транзакций"""
    while True:
        print("Программа: Введите статус, по которому необходимо выполнить фильтрацию.")
        print("Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING")
        user_choise = input("Ваш выбор: ").upper()
        if user_choise not in ["EXECUTED", "CANCELED", "PENDING"]:
            print(f'\nСтатус операции "{user_choise}" недоступен.\n')
        else:
            print(f'Операции отфильтрованы по статусу "{user_choise}"')
            break
    return user_choise


def show_display_params_menu() -> dict:
    """меню параметров отображения результатов"""
    result = {}
    user_choise = input("Отсортировать операции по дате? Да/Нет: ").lower()
    result["sort by date"] = user_choise == "да"
    if result["sort by date"]:
        user_choise = input("Отсортировать по возрастанию или по убыванию?: ").lower()
        result["descending order"] = user_choise != "по возрастанию"
    user_choise = input("Выводить только рублевые тразакции? Да/Нет: ").lower()
    result["rub only"] = user_choise == "да"
    user_choise = input(
        "Отфильтровать список транзакций по определенному слову в описании? Да/Нет: "
    ).lower()
    result["fiter description"] = user_choise == "да"
    if result["fiter description"]:
        result["description filter word"] = input(
            "Введите часть строки описания транзакций: "
        )
    return result


def query_file_name() -> str:
    """запрос имени файла для чтения"""
    while True:
        filename = input("Введите полный путь к файлу данных: ")
        if not os.path.exists(filename):
            print("\nВведнный файл не существует.\n")
            interrupt = input("Прекратить ввод? Да/нет: ").lower() == "да"
            if interrupt:
                filename = ""
                break
        else:
            break
    return filename


def load_data_from_file(filename: str, op_file_type: int) -> list[dict]:
    """загрузка данных о транзакциях из файлов разных типов"""

    result = []
    if op_file_type == 1:
        from src.utils import load_ops_from_json_file

        result = load_ops_from_json_file(filename)
    elif op_file_type == 2:
        from src.csv_tools import load_ops_from_csv

        result = load_ops_from_csv(filename, delimiter=";")
    elif op_file_type == 3:
        from src.excel_tools import load_ops_from_xlsx

        result = load_ops_from_xlsx(filename)
    return result


def print_formatted_operation(data: dict) -> None:
    """отформатированный вывод данных о транзакции"""
    description = data.get("description", "")
    print(get_date(data.get("date", "")) + " " + description)
    src_account = data.get("from", "")
    dst_account = data.get("to", "")
    currency_name = get_currency_name(data)
    currency_code = get_currency_code(data)
    amount = transaction_amount(data, currency_code)

    if str(description).lower().find("открытие") == -1:
        print(
            get_masked_account_or_card(src_account)
            + " -> "
            + get_masked_account_or_card(dst_account)
        )
    else:
        print(get_masked_account_or_card(dst_account))

    print(f"Сумма: {amount} {currency_name}\n")


def show_result(result_data: list[dict]) -> None:
    if len(result_data):
        print("\nРаспечатываю итоговый список транзакций...\n")
        print(f"Всего банковских операций в выборке: {len(result_data)}")
        for item in result_data:
            print_formatted_operation(item)
    else:
        print(
            "Не найдено ни одной транзакции, подходящей под ваши условия фильтрации\n"
        )


def main():
    """"""
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
    while True:
        final_data_to_show = []
        file_type = show_main_menu()
        if file_type == 0:
            break

        data_file = query_file_name()
        if not data_file:
            break

        operations_data = load_data_from_file(data_file, file_type)

        filter_status = show_select_status_menu()
        results_display_params = show_display_params_menu()

        data_to_show = filter_by_state(operations_data, filter_status)

        if results_display_params["fiter description"]:
            data_to_show = find_matches_in_description(
                data_to_show, pattern=results_display_params["description filter word"]
            )

        if results_display_params["sort by date"]:
            data_to_show = sort_by_date(
                data_to_show, results_display_params["descending order"]
            )

        if results_display_params["rub only"]:
            final_data_to_show = list(filter_by_currency(data_to_show, "RUB"))
            if not final_data_to_show:
                final_data_to_show = list(filter_by_currency2(data_to_show, "RUB"))

        show_result(final_data_to_show)


if __name__ == "__main__":
    main()
