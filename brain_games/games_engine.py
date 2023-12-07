import prompt
from brain_games.cli import welcome_user


def play_game(game):
    rounds_number = 3
    rules, get_question_and_answer = game()

    user_name = welcome_user()
    print(rules)

    while rounds_number:
        question, right_answer = get_question_and_answer()
        print(f'Question: {question}')

        user_answer = prompt.string('Your answer: ')

        if user_answer == str(right_answer):
            print('Correct!')
        else:
            print(
                f'{user_answer} is wrong answer ;(. '
                f'Correct answer was {right_answer}.'
            )
            break
        rounds_number -= 1

    if rounds_number:
        print(f"Let's try again, {user_name}!")
    else:
        print(f'Congratulations, {user_name}!')
