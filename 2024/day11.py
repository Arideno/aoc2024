### Day 11 - 2024

import pathlib
from helpers import *
import functools
    
def split_num(n: int) -> tuple[int, int]:
    s = str(n)
    mid = len(s) // 2
    left = int(s[:mid])
    right = int(s[mid:])
    return left, right

@functools.cache
def count(stone: int, blinks: int) -> int:
    if blinks == 0:
        return 1

    if stone == 0:
        return count(1, blinks - 1)
    elif len(str(stone)) % 2 == 0:
        left, right = split_num(stone)
        return count(left, blinks - 1) + count(right, blinks - 1)
    else:
        return count(stone * 2024, blinks - 1)

def first_part(input: str) -> int:
    stones = [int(x) for x in input.split()]

    ans = 0

    for stone in stones:
        ans += count(stone, 25)

    return ans

def second_part(input: str) -> int:
    stones = [int(x) for x in input.split()]

    ans = 0

    for stone in stones:
        ans += count(stone, 75)

    return ans 

if __name__ == '__main__':
    path = pathlib.Path(__file__).parent.parent.joinpath('data', '2024', 'day11')
    test_input = open(path.joinpath('input.test.txt'), 'r').read()
    input = open(path.joinpath('input.txt'), 'r').read()

    print('First part:')
    print(f'Test: {first_part(test_input)}')
    print(f'Answer: {first_part(input)}')

    print()

    print('Second part:')
    print(f'Test: {second_part(test_input)}')
    print(f'Answer: {second_part(input)}')
