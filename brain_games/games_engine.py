import prompt
from brain_games.cli import welcome_user


def is_answer_correct(user_answer, right_answer):
    return user_answer == str(right_answer)


def complete_game(rounds_number, user_name):
    if rounds_number:
        print(f"Let's try again, {user_name}!")
    else:
        print(f'Congratulations, {user_name}!')


def play_game(get_game_rules, get_question_and_answer):
    rounds_number = 3

    user_name = welcome_user()
    print(get_game_rules())

    while rounds_number:
        question, right_answer = get_question_and_answer()
        print(f'Question: {question}')

        user_answer = prompt.string('Your answer: ')

        if is_answer_correct(user_answer, right_answer):
            print('Correct!')
        else:
            print(f'{user_answer} is wrong answer ;(. Correct answer was {right_answer}.')
            break
        rounds_number -= 1

    complete_game(rounds_number, user_name)
