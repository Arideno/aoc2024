### Day 2 - 2024

import pathlib
from helpers import *
    
def is_safe(levels: list[int]) -> bool:
    is_increasing = levels[0] < levels[1]

    is_safe = True

    for i in range(1, len(levels)):
        if is_increasing: 
            if levels[i] - levels[i-1] >= 1 and levels[i] - levels[i-1] <= 3:
                continue
            else:
                is_safe = False
                break
        else:
            if levels[i-1] - levels[i] >= 1 and levels[i-1] - levels[i] <= 3:
                continue
            else:
                is_safe = False
                break

    return is_safe

def prepare_data(input: str) -> list[list[int]]:
    return [extract_ints(line) for line in input.splitlines()]

def first_part(input: str) -> int:
    levels_list = prepare_data(input)

    ans = 0

    for levels in levels_list:
        if is_safe(levels):
            ans += 1

    return ans

def second_part(input: str) -> int:
    levels_list = prepare_data(input)
    
    ans = 0

    for levels in levels_list:
        if is_safe(levels):
            ans += 1
        else:
            can_be_safe = False
            for i in range(len(levels)):
                if is_safe(levels[:i] + levels[i+1:]):
                    can_be_safe = True
                    break
            
            if can_be_safe:
                ans += 1

    return ans

if __name__ == '__main__':
    path = pathlib.Path(__file__).parent.parent.joinpath('data', '2024', 'day02')
    test_input = open(path.joinpath('input.test.txt'), 'r').read()
    input = open(path.joinpath('input.txt'), 'r').read()

    print('First part:')
    print(f'Test: {first_part(test_input)}')
    print(f'Answer: {first_part(input)}')

    print()

    print('Second part:')
    print(f'Test: {second_part(test_input)}')
    print(f'Answer: {second_part(input)}')
