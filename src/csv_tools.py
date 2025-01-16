from csv import reader


def load_ops_from_csv(filepath: str, delimiter: str = ",") -> list[dict]:
    """Загрузка данных об операциях из файла csv"""
    result = []
    try:
        with open(filepath, encoding="utf-8") as file:
            r = reader(file, delimiter=delimiter)
            rows = [row for row in r]
            fields = rows.pop(0)
            for row in rows:
                result.append(dict(zip(fields, row)))

    except FileNotFoundError:
        result = []

    return result
