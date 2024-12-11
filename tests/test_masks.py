from src.masks import get_mask_card_number, get_mask_account


def test_bank_cards_number_mask(random_card_number: int) -> None:
    result = get_mask_card_number(random_card_number)
    card_no = str(random_card_number)
    assert (
        (result[:4] == card_no[:4])
        and (result[5:7] == card_no[4:6])
        and (result[-4:] == card_no[-4:])
        and (result[7:15] == "** **** ")
    )


def test_bank_account_number_mask(random_bank_account_number: int) -> None:
    result = get_mask_account(random_bank_account_number)
    src_number = str(random_bank_account_number)

    assert (result[-4:] == src_number[-4:]) and (result[:2] == "**")
