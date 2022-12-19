from brain_games.games.brain_gcd import gcd_question_and_answer, gcd_rules
from brain_games.games_engine import play_game


def main():
    play_game(gcd_rules, gcd_question_and_answer)


if __name__ == '__main__':
    main()
