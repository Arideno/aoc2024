# Day 22 - 2024

import pathlib
from collections import defaultdict
from helpers import *


def gen(seed: int, i: int) -> list[int]:
    n = seed
    nums = [n]
    for _ in range(i):
        a = n * 64
        n ^= a
        n %= 16777216

        a = n // 32
        n ^= a
        n %= 16777216

        a = n * 2048
        n ^= a
        n %= 16777216

        nums.append(n)

    return nums


def get_prices(nums: list[int]) -> list[int]:
    return [num % 10 for num in nums]


def get_price_changes(prices: list[int]) -> list[int]:
    return [prices[i] - prices[i - 1] for i in range(1, len(prices))]


def total_for_prices(prices: list[int]):
    total = {}
    price_changes = get_price_changes(prices)

    for i in range(len(price_changes) - 3):
        seq = tuple(price_changes[i:i+4])
        if not seq in total:
            total[seq] = prices[i + 4]

    return total


def first_part(input: str) -> int:
    seeds = [int(x) for x in input.splitlines()]

    ans = 0

    for seed in seeds:
        ans += gen(seed, 2000)[-1]

    return ans


def second_part(input: str) -> int:
    seeds = [int(x) for x in input.splitlines()]

    totals = defaultdict(int)

    for seed in seeds:
        nums = gen(seed, 2000)
        prices = get_prices(nums)

        for seq, total in total_for_prices(prices).items():
            totals[seq] += total

    return max(totals.values())


if __name__ == '__main__':
    path = pathlib.Path(__file__).parent.parent.joinpath(
        'data', '2024', 'day22')
    test_input = open(path.joinpath('input.test.txt'), 'r').read()
    input = open(path.joinpath('input.txt'), 'r').read()

    print('First part:')
    print(f'Test: {first_part(test_input)}')
    print(f'Answer: {first_part(input)}')

    print()

    print('Second part:')
    print(f'Test: {second_part(test_input)}')
    print(f'Answer: {second_part(input)}')
