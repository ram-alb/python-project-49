from brain_games.games.brain_progression import (
    progression_question_and_answer,
    progression_rules,
)
from brain_games.games_engine import play_game


def main():
    play_game(progression_rules, progression_question_and_answer)


if __name__ == '__main__':
    main()
