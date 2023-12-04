from pathlib import Path


def get_data() -> list[str]:
    with Path('src/app/data/day_1.data').open() as f:
        return f.readlines()


def get_total(rows: list[str]) -> int:
    total = 0

    for row in rows:
        num_string = next((char for char in row if char.isdigit()), '')

        for char in reversed(row):
            if char.isdigit():
                num_string += char
                break

        if not num_string:
            continue

        total += int(num_string)

    return total


if __name__ == '__main__':
    print(f'Total: {get_total(get_data())}')
