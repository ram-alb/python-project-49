from brain_games.games_engine import play_game
from brain_games.games.brain_calc import get_calc_rules, calc_question_and_answer


def main():
    play_game(get_calc_rules, calc_question_and_answer)


if __name__ == '__main__':
    main()
