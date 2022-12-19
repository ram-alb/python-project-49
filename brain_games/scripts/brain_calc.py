from brain_games.games.brain_calc import (
    calc_question_and_answer,
    get_calc_rules,
)
from brain_games.games_engine import play_game


def main():
    play_game(get_calc_rules, calc_question_and_answer)


if __name__ == '__main__':
    main()
