# Day 24 - 2024

import pathlib
import re
from helpers import *


def simulate(wires: dict[str, int], gates: dict[str, tuple[str, str, str]]) -> dict[str, int]:
    wires = wires.copy()
    gates = gates.copy()
    while len(gates) > 0:
        for out, (in1, op, in2) in gates.copy().items():
            val1 = wires.get(in1)
            val2 = wires.get(in2)

            if val1 is None or val2 is None:
                continue

            if op == 'AND':
                wires[out] = val1 & val2
            elif op == 'OR':
                wires[out] = val1 | val2
            elif op == 'XOR':
                wires[out] = val1 ^ val2

            del gates[out]

    return wires


def get_digits_for_wire_prefix(wires: dict[str, int], prefix: str) -> str:
    tuples = []
    for wire, val in wires.items():
        if wire.startswith(prefix):
            tuples.append((wire, val))

    tuples.sort(key=lambda x: x[0], reverse=True)
    digits = ''.join([str(val) for _, val in tuples])

    return digits


def first_part(input: str) -> int:
    l1, l2 = input.split('\n\n')
    wires = {}
    gates = {}

    for line in l1.splitlines():
        wire, val = line.split(': ')
        wires[wire] = int(val)

    for line in l2.splitlines():
        match = re.match(r'(\w+) (AND|OR|XOR) (\w+) -> (\w+)', line)
        in1, op, in2, out = match.groups()
        gates[out] = (in1, op, in2)

    out_wires = simulate(wires, gates)
    digits = get_digits_for_wire_prefix(out_wires, 'z')

    return int(digits, 2)


def get_dependency(gates: dict[str, tuple[str, str, str]], wire: str) -> str:
    if wire not in gates:
        return wire

    in1, op, in2 = gates[wire]
    return f'({get_dependency(gates, in1)} {op} {get_dependency(gates, in2)})'


def second_part(input: str) -> int:
    l1, l2 = input.split('\n\n')
    wires = {}
    gates = {}

    for line in l1.splitlines():
        wire, val = line.split(': ')
        wires[wire] = int(val)

    for line in l2.splitlines():
        match = re.match(r'(\w+) (AND|OR|XOR) (\w+) -> (\w+)', line)
        in1, op, in2, out = match.groups()
        gates[out] = (in1, op, in2)

    wires = simulate(wires, gates)

    x_digits = get_digits_for_wire_prefix(wires, 'x')
    y_digits = get_digits_for_wire_prefix(wires, 'y')
    z_digits = get_digits_for_wire_prefix(wires, 'z')

    x = int(x_digits, 2)
    y = int(y_digits, 2)

    expected_z = str(bin(x + y))[2:]

    print(f'Exp: {expected_z}')
    print(f'Act: {z_digits}')

    print(get_dependency(gates, 'z05'))
    print(get_dependency(gates, 'z06'))
    print(get_dependency(gates, 'z07'))
    print(get_dependency(gates, 'z16'))
    print(get_dependency(gates, 'z21'))
    print(get_dependency(gates, 'z22'))
    print(get_dependency(gates, 'z23'))
    print(get_dependency(gates, 'z39'))
    print(get_dependency(gates, 'z40'))
    print(get_dependency(gates, 'z41'))
    print(get_dependency(gates, 'z42'))


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
