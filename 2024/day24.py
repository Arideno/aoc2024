# Day 24 - 2024

import pathlib
import re
from helpers import *


def eval_gate(gate, wires):
    match = re.match(r'(\w+) (AND|OR|XOR) (\w+) -> (\w+)', gate)

    in1, op, in2, out = match.groups()
    val1 = wires.get(in1)
    val2 = wires.get(in2)

    if val1 is None or val2 is None:
        return False

    if op == 'AND':
        wires[out] = val1 & val2
    elif op == 'OR':
        wires[out] = val1 | val2
    elif op == 'XOR':
        wires[out] = val1 ^ val2

    return True


def first_part(input: str) -> int:
    l1, l2 = input.split('\n\n')
    wires = {}
    gates = []

    for line in l1.splitlines():
        wire, val = line.split(': ')
        wires[wire] = int(val)

    for line in l2.splitlines():
        gates.append(line)

    while len(gates) > 0:
        for gate in gates.copy():
            if eval_gate(gate, wires):
                gates.remove(gate)

    bin_val = ''.join(str(wires[f'z{i:02}'])
                      for i in range(len(wires) - 1, -1, -1) if f'z{i:02}' in wires)
    return int(bin_val, 2)


def second_part(input: str) -> int:
    # Done manually
    pass


if __name__ == '__main__':
    path = pathlib.Path(__file__).parent.parent.joinpath(
        'data', '2024', 'day24')
    test_input = open(path.joinpath('input.test.txt'), 'r').read()
    input = open(path.joinpath('input.txt'), 'r').read()

    print('First part:')
    print(f'Test: {first_part(test_input)}')
    print(f'Answer: {first_part(input)}')

    print()

    print('Second part:')
    print(f'Test: {second_part(test_input)}')
    print(f'Answer: {second_part(input)}')
