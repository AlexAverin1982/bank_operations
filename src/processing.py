def filter_by_state(data_in: list[dict], state: str = 'EXECUTED') -> list[dict]:
    """ функция фильтрует исходный список словарей, возвращая список только словарей с указанным состоянием state """
    return [d for d in data_in if d.get('state', '') == state]



