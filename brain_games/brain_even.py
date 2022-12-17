from brain_games.cli import welcome_user
from random import randint
import prompt


def is_even(number):
    return number % 2 == 0


def brain_even():
    user_name = welcome_user()

    print('Answer "yes" if the number is even, otherwise answer "no".')

    current_round = 1
    max_rounds = 3
    while current_round <= max_rounds:
        question_number = randint(1, 100)

        if is_even(question_number):
            right_answer = 'yes'
        else:
            right_answer = 'no'

        user_answer = prompt.string(f'Question {question_number}\nYour answer: ')
        if user_answer == right_answer:
            print('Correct!')
        else:
            print(f'{user_answer} is wrong answer ;(. Correct answer was {right_answer}.')
            break
        current_round += 1

    if current_round > max_rounds:
        print(f'Congratulations, {user_name}!')
    else:
        print(f"Let's try again, {user_name}!")
