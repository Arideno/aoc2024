### Day 1 - 2024

import pathlib
from helpers import *
    
def first_part(input: str) -> int:
    list1, list2 = [], []

    for line in input.splitlines():
        x, y = extract_ints(line)
        list1.append(x)
        list2.append(y)
    
    list1.sort()
    list2.sort()

    ans = 0

    for i in range(len(list1)):
        diff = abs(list1[i] - list2[i])
        ans += diff

    return ans

def second_part(input: str) -> int:
    list1, list2 = [], []

    for line in input.splitlines():
        x, y = extract_ints(line)
        list1.append(x)
        list2.append(y)

    ans = 0

    dic = {}

    for i in range(len(list2)):
        if dic.get(list2[i]) is None:
            dic[list2[i]] = 1
        else:
            dic[list2[i]] += 1

    for i in range(len(list1)):
        if dic.get(list1[i]):
            ans += list1[i] * dic.get(list1[i])

    return ans

if __name__ == '__main__':
    path = pathlib.Path(__file__).parent.parent.joinpath('data', '2024', 'day01')
    test_input = open(path.joinpath('input.test.txt'), 'r').read()
    input = open(path.joinpath('input.txt'), 'r').read()

    print('First part:')
    print(f'Test: {first_part(test_input)}')
    print(f'Answer: {first_part(input)}')

    print()

    print('Second part:')
    print(f'Test: {second_part(test_input)}')
    print(f'Answer: {second_part(input)}')
