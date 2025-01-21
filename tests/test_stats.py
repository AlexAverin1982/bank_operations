from src.stats_tools import count_categories


def test_count_categories(random_transactions: list[dict]) -> None:
    random_transactions[0]['description'] = 'ONE'
    random_transactions[1]['description'] = 'ONE'
    random_transactions[2]['description'] = 'ONE'
    random_transactions[3]['description'] = 'TWO'
    random_transactions[4]['description'] = 'TWO'

    random_transactions = random_transactions[:5]

    result = count_categories(random_transactions, ['ONE', 'TWO'])
    assert result == {'ONE': 3, 'TWO': 2}
