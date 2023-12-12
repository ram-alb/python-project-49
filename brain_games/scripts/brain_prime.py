from brain_games.games.prime import get_game_data
from brain_games.games_engine import play_game


def prime_main():
    play_game(get_game_data)


if __name__ == '__main__':
    prime_main()
