from brain_games.games_engine import play_game
from brain_games.games.brain_even import brain_even_rules, brain_even_question_and_answer


def main():
    play_game(brain_even_rules, brain_even_question_and_answer)


if __name__ == '__main__':
    main()
