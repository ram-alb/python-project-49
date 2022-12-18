from brain_games.games_engine import play_game
from brain_games.games.brain_prime import prime_rules, prime_question_and_answer


def prime_main():
    play_game(prime_rules, prime_question_and_answer)


if __name__ == '__main__':
    prime_main()
