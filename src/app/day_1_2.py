from pathlib import Path


def get_data() -> list[str]:
    with Path('src/app/data/day_1.data').open() as f:
        return f.readlines()


nums_as_strings = {
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9,
}

min_string_num_length = min(len(key) for key in nums_as_strings)


def get_first_num(row: str) -> str:
    num_as_string = ''
    string = ''

    for char in row:
        try:
            int(char)
            num_as_string = char
            break
        except ValueError:
            string += char

            if len(string) >= min_string_num_length:
                for key in nums_as_strings:
                    if string.endswith(key):
                        num_as_string = str(nums_as_strings[key])
                        break
        if num_as_string:
            break
    return num_as_string


def get_second_num(row: str) -> str:
    num_as_string = ''
    string = ''

    for char in reversed(row):
        try:
            int(char)
            num_as_string = char
            break
        except ValueError:
            string = f'{char}{string}'

            if len(string) >= min_string_num_length:
                for key in nums_as_strings:
                    if string.startswith(key):
                        num_as_string = str(nums_as_strings[key])
                        break
        if num_as_string:
            break
    return num_as_string


def get_total(rows: list[str]) -> int:
    total = 0

    for row in rows:
        num_as_string = get_first_num(row)
        num_as_string += get_second_num(row)

        if not num_as_string:
            continue

        total += int(num_as_string)

    return total


if __name__ == '__main__':
    print(f'Total: {get_total(get_data())}')
