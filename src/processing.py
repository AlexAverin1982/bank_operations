def filter_by_state(data_in: list[dict], state: str = 'EXECUTED') -> list[dict]:
    """ функция фильтрует исходный список словарей, возвращая список только словарей с указанным состоянием state """
    return [d for d in data_in if d.get('state', '') == state]


def sort_by_date(data_in: list[dict], desc_order: bool = True) -> list[dict]:
    """ функция возвращает список отсортированный по указанному порядку по ключу date """
    return sorted(data_in, reverse=desc_order, key=lambda x: x['date'])


if __name__ == '__main__':
    test_data = [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                 {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
                 {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                 {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
                 {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
                 {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]
    print('EXECUTED')
    print(filter_by_state(test_data))
    print('CANCELED')
    print(filter_by_state(test_data, 'CANCELED'))
