import re
from pathlib import Path


def get_game_id(game: str) -> int:
    match = re.match(r'Game (\d+)', game)
    return (match and int(match[1])) or 0


def game_is_possible(game: str, allowed_color_counts: dict[str, int]) -> bool:
    game_sets = game.split(': ')[1].split(';')

    for game_set in game_sets:
        print(f'{game_set=}')
        color_counts = game_set.lstrip(' ').rstrip(' ').split(', ')
        print(f'{color_counts=}')

        for color_count in color_counts:
            print(f'{color_count=}')
            color_info = color_count.split(' ')
            count = int(color_info[0])
            name = color_info[1]

            if count > allowed_color_counts.get(name, 0):
                return False
    return True


def get_possible_games_sum(games: list[str], allowed_color_counts: dict[str, int]) -> int:
    possible_game_total = 0

    for game in games:
        game_id = get_game_id(game=game)

        if game_is_possible(game=game, allowed_color_counts=allowed_color_counts):
            possible_game_total += game_id

    return possible_game_total


if __name__ == '__main__':
    data = Path('src/app/data/day_2.data').read_text().splitlines()
    print(f"{get_possible_games_sum(data, {'red': 12, 'green': 13, 'blue': 14})=}")
