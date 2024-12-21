# Day 21 - 2024

import pathlib
from collections import deque
import functools
from helpers import *

num_keypad = [
    ['7', '8', '9'],
    ['4', '5', '6'],
    ['1', '2', '3'],
    [' ', '0', 'A']
]
num_start = (3, 2)

dir_keypad = [
    [' ', '^', 'A'],
    ['<', 'v', '>']
]
dir_start = (0, 2)


def find_pos(keypad: list[list[str]], symbol: str) -> tuple[int, int]:
    for i in range(len(keypad)):
        for j in range(len(keypad[0])):
            if keypad[i][j] == symbol:
                return (i, j)


@functools.cache
def cheapest(seq, r):
    if r == 0:
        return len(seq)

    ans = 0
    curr = dir_start

    for c in seq:
        target = find_pos(dir_keypad, c)
        ans += cheapest_dir(curr, target, r)
        curr = target

    return ans


@functools.cache
def cheapest_dir(start, end, r):
    ans = float('inf')
    queue = deque([(start, '')])

    while len(queue) > 0:
        pos, seq = queue.popleft()
        if pos == end:
            rec = cheapest(seq + 'A', r - 1)
            ans = min(ans, rec)
            continue

        if dir_keypad[pos[0]][pos[1]] == ' ':
            continue

        if pos[0] < end[0]:
            queue.append(((pos[0] + 1, pos[1]), seq + 'v'))
        elif pos[0] > end[0]:
            queue.append(((pos[0] - 1, pos[1]), seq + '^'))

        if pos[1] < end[1]:
            queue.append(((pos[0], pos[1] + 1), seq + '>'))
        elif pos[1] > end[1]:
            queue.append(((pos[0], pos[1] - 1), seq + '<'))

    return ans


def calc_whole(start, end, r):
    ans = float('inf')
    queue = deque([(start, '')])

    while len(queue) > 0:
        pos, seq = queue.popleft()
        if pos == end:
            rec = cheapest(seq + 'A', r)
            ans = min(ans, rec)
            continue

        if num_keypad[pos[0]][pos[1]] == ' ':
            continue

        if pos[0] < end[0]:
            queue.append(((pos[0] + 1, pos[1]), seq + 'v'))
        elif pos[0] > end[0]:
            queue.append(((pos[0] - 1, pos[1]), seq + '^'))

        if pos[1] < end[1]:
            queue.append(((pos[0], pos[1] + 1), seq + '>'))
        elif pos[1] > end[1]:
            queue.append(((pos[0], pos[1] - 1), seq + '<'))

    return ans


def first_part(input: str) -> int:
    codes = input.splitlines()

    ans = 0

    for code in codes:
        curr = num_start

        for c in code:
            target = find_pos(num_keypad, c)
            ans += calc_whole(curr, target, 2) * int(code[:-1])
            curr = target

    return ans


def second_part(input: str) -> int:
    codes = input.splitlines()

    ans = 0

    for code in codes:
        curr = num_start

        for c in code:
            target = find_pos(num_keypad, c)
            ans += calc_whole(curr, target, 25) * int(code[:-1])
            curr = target

    return ans


if __name__ == '__main__':
    path = pathlib.Path(__file__).parent.parent.joinpath(
        'data', '2024', 'day21')
    test_input = open(path.joinpath('input.test.txt'), 'r').read()
    input = open(path.joinpath('input.txt'), 'r').read()

    print('First part:')
    print(f'Test: {first_part(test_input)}')
    print(f'Answer: {first_part(input)}')

    print()

    print('Second part:')
    print(f'Test: {second_part(test_input)}')
    print(f'Answer: {second_part(input)}')
