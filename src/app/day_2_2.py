from collections import defaultdict
from pathlib import Path


def get_game_power(game: str) -> int:
    game_sets = game.split(': ')[1].split(';')

    fewest_cubes_by_color = defaultdict(int)

    for game_set in game_sets:
        color_counts = game_set.lstrip(' ').rstrip(' ').split(', ')

        for color_count in color_counts:
            color_info = color_count.split(' ')
            count = int(color_info[0])
            name = color_info[1]

            fewest_cubes = fewest_cubes_by_color[name]

            if not fewest_cubes or count > fewest_cubes:
                fewest_cubes_by_color[name] = count

    power = 1
    for count in fewest_cubes_by_color.values():
        power *= count
    return power


def get_power_sum(games: list[str]) -> int:
    return sum(get_game_power(game=game) for game in games)


if __name__ == '__main__':
    data = Path('src/app/data/day_2.data').read_text().splitlines()
    print(f'{get_power_sum(data)=}')
