import contextlib
from pathlib import Path


def get_data() -> list[str]:
    with Path('src/app/day_1.data').open() as f:
        return f.readlines()


def get_total(rows: list[str]) -> int:
    total = 0

    for row in rows:
        num_string = ''

        for char in row:
            with contextlib.suppress(Exception):
                int(char)
                num_string = char
                break
        for char in reversed(row):
            with contextlib.suppress(Exception):
                int(char)
                num_string += char
                break

        if not num_string:
            continue

        total += int(num_string)

    return total


if __name__ == '__main__':
    print(f'Total: {get_total(get_data())}')
