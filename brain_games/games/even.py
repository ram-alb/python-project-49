from random import randint


def is_even(number):
    return number % 2 == 0


def even_rules():
    return 'Answer "yes" if the number is even, otherwise answer "no".'


def even_question_and_answer():
    question_number = randint(1, 100)
    answer = 'yes' if is_even(question_number) else 'no'
    return (question_number, answer)


def even():
    return even_rules, even_question_and_answer
