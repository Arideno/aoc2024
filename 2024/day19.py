### Day 19 - 2024

import pathlib
from helpers import *

def first_part(input: str) -> int:
    patterns, designs = input.split('\n\n')
    patterns = patterns.split(', ')

    ans = 0

    for design in designs.splitlines():
        dp = [False] * (len(design) + 1)
        dp[0] = True

        for i in range(1, len(design) + 1):
            for pattern in patterns:
                if i >= len(pattern) and dp[i - len(pattern)] and design[i - len(pattern):i] == pattern:
                    dp[i] = True
                    break

        if dp[-1]:
            ans += 1

    return ans

def second_part(input: str) -> int:
    patterns, designs = input.split('\n\n')
    patterns = patterns.split(', ')

    ans = 0

    for design in designs.splitlines():
        dp = [0] * (len(design) + 1)
        dp[0] = 1

        for i in range(1, len(design) + 1):
            for pattern in patterns:
                if i >= len(pattern) and design[i - len(pattern):i] == pattern:
                    dp[i] += dp[i - len(pattern)]

        ans += dp[-1]

    return ans

if __name__ == '__main__':
    path = pathlib.Path(__file__).parent.parent.joinpath('data', '2024', 'day19')
    test_input = open(path.joinpath('input.test.txt'), 'r').read()
    input = open(path.joinpath('input.txt'), 'r').read()

    print('First part:')
    print(f'Test: {first_part(test_input)}')
    print(f'Answer: {first_part(input)}')

    print()

    print('Second part:')
    print(f'Test: {second_part(test_input)}')
    print(f'Answer: {second_part(input)}')
