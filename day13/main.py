import pathlib
from itertools import product
from math import gcd

def first_part(input: str) -> int:
    ans = 0

    machines = input.split('\n\n')
    for machine in machines:
        info = machine.split('\n')
        a = info[0].split(', ')
        b = info[1].split(', ')
        c = info[2]

        button_a = {
            'x': int(a[0].split('+')[1]),
            'y': int(a[1].split('+')[1]),
            'cost': 3
        }
        button_b = {
            'x': int(b[0].split('+')[1]),
            'y': int(b[1].split('+')[1]),
            'cost': 1
        }
        prize = {
            'x': int(c.split('=')[1].split(', ')[0]),
            'y': int(c.split('=')[2]),
        }

        min_tokens = float('inf')
        found = False

        for a_presses, b_presses in product(range(101), repeat=2):
            total_x = a_presses * button_a['x'] + b_presses * button_b['x']
            total_y = a_presses * button_a['y'] + b_presses * button_b['y']

            if total_x == prize['x'] and total_y == prize['y']:
                min_tokens = min(min_tokens, a_presses * button_a['cost'] + b_presses * button_b['cost'])
                found = True

        if found:
            ans += min_tokens

    return ans

def second_part(input: str) -> int:
    ans = 0

    machines = input.split('\n\n')
    for machine in machines:
        info = machine.split('\n')
        a = info[0].split(', ')
        b = info[1].split(', ')
        c = info[2]

        button_a = {
            'x': int(a[0].split('+')[1]),
            'y': int(a[1].split('+')[1]),
            'cost': 3
        }
        button_b = {
            'x': int(b[0].split('+')[1]),
            'y': int(b[1].split('+')[1]),
            'cost': 1
        }
        prize = {
            'x': int(c.split('=')[1].split(', ')[0]) + 10000000000000,
            'y': int(c.split('=')[2]) + 10000000000000,
        }

        ax, ay = button_a['x'], button_a['y']
        bx, by = button_b['x'], button_b['y']
        tx, ty = prize['x'], prize['y']

        b = (tx * ay - ty * ax) // (ay * bx - by * ax)
        a = (tx * by - ty * bx) // (by * ax - bx * ay)

        if ax * a + bx * b == tx and ay * a + by * b == ty:
            if a >= 0 and b >= 0:
                ans += a * button_a['cost'] + b * button_b['cost']

    return ans

if __name__ == '__main__':
    path = pathlib.Path(__file__).parent
    test_input = open(path.joinpath('test_input.txt'), 'r').read()
    input = open(path.joinpath('input.txt'), 'r').read()

    print('First part:')
    print(f'Test: {first_part(test_input)}')
    print(f'Answer: {first_part(input)}')

    print()

    print('Second part:')
    print(f'Test: {second_part(test_input)}')
    print(f'Answer: {second_part(input)}')