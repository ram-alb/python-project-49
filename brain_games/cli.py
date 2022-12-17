import prompt


def welcome_user():
    print('\nWelcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name
