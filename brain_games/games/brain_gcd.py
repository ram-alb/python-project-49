from random import randint


def gcd_rules():
    return 'Find the greatest common divisor of given numbers.'


def get_gcd(number1, number2):
    max_num = max(number1, number2)
    min_num = min(number1, number2)
    remainder = max_num % min_num

    while remainder:
        max_num = max(min_num, remainder)
        min_num = min(min_num, remainder)
        remainder = max_num % min_num

    return min_num


def gcd_question_and_answer():
    min_number = 1
    max_number = 100

    number1 = randint(min_number, max_number)
    number2 = randint(min_number, max_number)

    question = f'{number1} {number2}'
    gcd = get_gcd(number1, number2)

    return (question, gcd)
