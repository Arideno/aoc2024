# Day 25 - 2024

import pathlib
from helpers import *


def get_heights(matrix: list[str]) -> list[int]:
    heights = []
    for i in range(len(matrix[0])):
        heights.append([col[i] for col in matrix].count('#'))
    return heights


def first_part(input: str) -> int:
    blocks = input.split('\n\n')

    lock_heights = []
    key_heights = []

    for block in blocks:
        lines = block.split('\n')
        if lines[0].count('.') > 0:
            lock_heights.append(get_heights(lines))
        else:
            key_heights.append(get_heights(lines))

    ans = 0

    for key in key_heights:
        for lock in lock_heights:
            valid = True
            for i, j in zip(key, lock):
                if i + j > 7:
                    valid = False
                    break

            if valid:
                ans += 1

    return ans


if __name__ == '__main__':
    path = pathlib.Path(__file__).parent.parent.joinpath(
        'data', '2024', 'day25')
    test_input = open(path.joinpath('input.test.txt'), 'r').read()
    input = open(path.joinpath('input.txt'), 'r').read()

    print('First part:')
    print(f'Test: {first_part(test_input)}')
    print(f'Answer: {first_part(input)}')
