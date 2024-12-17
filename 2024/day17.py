### Day 17 - 2024

import pathlib
from helpers import *
import threading

def get_value(operand, reg) -> int:
    if operand <= 3:
        return operand
    if operand == 4:
        return reg['A']
    if operand == 5:
        return reg['B']
    if operand == 6:
        return reg['C']

def run(program, regs) -> list[int]:
    ip = 0
    output = []

    while ip < len(program):
        op = program[ip]
        operand = program[ip + 1]
        ip += 2

        if op == 0:
            regs['A'] //= 2 ** get_value(operand, regs)
        elif op == 1:
            regs['B'] ^= operand
        elif op == 2:
            regs['B'] = get_value(operand, regs) % 8
        elif op == 3:
            if regs['A'] != 0:
                ip = operand
        elif op == 4:
            regs['B'] ^= regs['C']
        elif op == 5:
            output.append(get_value(operand, regs) % 8)
        elif op == 6:
            regs['B'] = regs['A'] // (2 ** get_value(operand, regs))
        elif op == 7:
            regs['C'] = regs['A'] // (2 ** get_value(operand, regs))

    return output

def first_part(input: str) -> str:
    regs_input, program_input = input.split('\n\n')
    a, b, c = extract_ints(regs_input)
    regs = {'A': a, 'B': b, 'C': c}
    program = extract_ints(program_input)

    output = run(program, regs)

    return ','.join([str(x) for x in output])

# B = A & 7
# B = B XOR 7
# C = A >> B
# B = B XOR C
# B = B XOR 4
# OUT LAST 3 BITS OF B
# A = A >> 3
# GOTO 0 IF A != 0

def rec(program, init_regs, a, prefix) -> int:
    for shift in range(8):
        regs = init_regs.copy()
        regs['A'] = a * 8 + shift
        output = run(program, regs)

        if output == program[prefix:]:
            if prefix == 0:
                return a * 8 + shift

            next = rec(program, regs, a * 8 + shift, prefix - 1)
            if next is not None:
                return next

def second_part(input: str) -> int:
    regs_input, program_input = input.split('\n\n')
    a, b, c = extract_ints(regs_input)
    regs = {'A': a, 'B': b, 'C': c}
    program = extract_ints(program_input)

    return rec(program, regs, 0, len(program) - 1)

if __name__ == '__main__':
    path = pathlib.Path(__file__).parent.parent.joinpath('data', '2024', 'day17')
    test_input = open(path.joinpath('input.test.txt'), 'r').read()
    input = open(path.joinpath('input.txt'), 'r').read()

    print('First part:')
    print(f'Test: {first_part(test_input)}')
    print(f'Answer: {first_part(input)}')

    print()

    print('Second part:')
    print(f'Test: {second_part(test_input)}')
    print(f'Answer: {second_part(input)}')
