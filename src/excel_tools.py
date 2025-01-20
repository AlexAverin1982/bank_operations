from pandas import read_excel


def load_ops_from_xlsx(filepath: str) -> list[dict]:
    """загружает данные по транзакциям из файлов excel"""
    result = []
    try:
        # column_types = {'id': int, 'state': str, 'date': datetime, 'amount': int,
        #                 'currency_name': str, 'currency_code':str, 'from': str, 'to': str, 'description': str}
        excel_data = read_excel(filepath, dtype=str)
        fields = list(excel_data.head(0).columns.values)
        for i in range(excel_data.shape[0]):
            row = list(excel_data.iloc[i])
            result.append(dict(zip(fields, row)))
    except:
        result = []

    return result
