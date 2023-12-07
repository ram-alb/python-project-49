from random import randint


def calc_rules():
    return 'What is the result of the expression?'


def calc_question_and_answer():
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

    return (question, answer)


def calc():
    return calc_rules, calc_question_and_answer
