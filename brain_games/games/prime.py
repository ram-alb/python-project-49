from random import randint

PRIME_RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    divisor = 2
    while number % divisor != 0:
        divisor += 1
    return divisor == number


def get_game_data(is_rules=False):
    if is_rules:
        return PRIME_RULES
    min_number = 2
    max_number = 100
    question = randint(min_number, max_number)
    answer = 'yes' if is_prime(question) else 'no'
    return question, answer
