import pathlib

def prepare_data(input: str) -> list[tuple[int, list[int]]]:
    eqs = []
    for line in input.split('\n'):
        parts = line.split(': ')
        key = int(parts[0])
        values = [int(x) for x in parts[1].split(' ')]
        eqs.append((key, values))
    return eqs

def rec(result: int, values: list[int], current: int, index: int, with_concat: bool = False) -> bool:
    if index == len(values):
        return current == result
    
    plus = rec(result, values, current + values[index], index + 1, with_concat)
    mul = rec(result, values, current * values[index], index + 1, with_concat)
    concat = rec(result, values, int(str(current) + str(values[index])), index + 1, with_concat)

    return plus or mul or (with_concat and concat)

def first_part(input: str) -> int:
    eqs = prepare_data(input)

    ans = 0

    for key, values in eqs:
        if rec(key, values, values[0], 1):
            ans += key
        
    return ans

def second_part(input: str) -> int:
    eqs = prepare_data(input)

    ans = 0

    for key, values in eqs:
        if rec(key, values, values[0], 1, with_concat=True):
            ans += key
        
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