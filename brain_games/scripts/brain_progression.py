from brain_games.games.progression import get_game_data
from brain_games.games_engine import play_game


def main():
    play_game(get_game_data)


if __name__ == '__main__':
    main()
