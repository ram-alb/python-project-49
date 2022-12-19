from brain_games.games.brain_prime import (
    prime_question_and_answer,
    prime_rules,
)
from brain_games.games_engine import play_game


def prime_main():
    play_game(prime_rules, prime_question_and_answer)


if __name__ == '__main__':
    prime_main()
