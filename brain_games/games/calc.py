from random import randint

CALC_RULES = 'What is the result of the expression?'


def get_game_data(get_rules=False):
    if get_rules:
        return CALC_RULES

    min_number = 0
    max_number = 10

    first_number = randint(min_number, max_number)
    second_number = randint(min_number, max_number)

    opertions_number = 3
    opertion = randint(0, opertions_number)

    if opertion == 1:
        question = f'{first_number} + {second_number}'
        answer = first_number + second_number
    elif opertion == 2:
        max_num = max(first_number, second_number)
        min_num = min(first_number, second_number)
        question = f'{max_num} - {min_num}'
        answer = max_num - min_num
    else:
        question = f'{first_number} * {second_number}'
        answer = first_number * second_number

    return question, answer
