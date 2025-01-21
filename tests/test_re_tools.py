from src.re_tools import find_matches_in_description


def test_find_matches_in_description(random_transactions: list[dict]) -> None:
    random_transactions[0]['description'] = 'here__'
    result = find_matches_in_description(random_transactions, 'here')
    assert result == [random_transactions[0]]
