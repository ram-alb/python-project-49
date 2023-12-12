from random import randint

EVEN_RULES = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(number):
    return number % 2 == 0


def get_game_data(get_rules=False):
    if get_rules:
        return EVEN_RULES
    question_number = randint(1, 100)
    answer = 'yes' if is_even(question_number) else 'no'
    return question_number, answer
