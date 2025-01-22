def get_word_ending(count):
    """Функция get_word_ending подбирает окончание к слову 'запись' в зависимости от числительного count"""

    ending = ''
    if (4 < count < 21) or (count % 10 == 0):
        ending = 'ей'
    elif count % 10 == 1:
        ending = 'ь'
    elif count % 10 in [2,3,4]:
        ending = 'и'
    else:
        ending = 'ей'
    return ending
