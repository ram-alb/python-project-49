from random import randint

prime_rules = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    divisor = 2
    while number % divisor != 0:
        divisor += 1
    return divisor == number


def get_prime_question_and_answer():
    min_number = 2
    max_number = 100
    question = randint(min_number, max_number)
    answer = 'yes' if is_prime(question) else 'no'
    return question, answer


def prime():
    return prime_rules, get_prime_question_and_answer
