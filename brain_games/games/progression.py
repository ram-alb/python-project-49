from random import randint

PROGRESSION_RULES = 'What number is missing in the progression?'


def get_step():
    min_step = 1
    max_step = 10
    return randint(min_step, max_step)


def get_border_values(step, progression_length):
    min_first_item = 0
    max_first_item = 100
    first_item = randint(min_first_item, max_first_item)
    last_item = first_item + step * (progression_length - 1)
    return first_item, last_item


def get_game_data(get_rules=False):
    if get_rules:
        return PROGRESSION_RULES

    progression_length = 10

    step = get_step()
    first_item, last_item = get_border_values(step, progression_length)

    progression = list(range(first_item, last_item + step, step))
    missed_value_index = randint(0, progression_length - 1)

    answer = progression[missed_value_index]
    progression[missed_value_index] = '..'
    question = ' '.join([str(item) for item in progression])

    return question, answer
