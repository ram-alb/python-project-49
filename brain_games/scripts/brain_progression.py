from brain_games.games.brain_progression import get_game_rules, get_question_and_answer
from brain_games.games_engine import play_game


def main():
    play_game(get_game_rules, get_question_and_answer)


if __name__ == '__main__':
    main()
