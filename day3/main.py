import re

def first_part(input: str) -> int:
    pattern = r'mul\((\d+),(\d+)\)'
    matches = re.findall(pattern, input)

    return sum([int(a) * int(b) for a, b in matches])    

def second_part(input: str) -> int:
    cleaned_input = re.sub(r"don't\(\).*?do\(\)", '', input, flags=re.DOTALL)
    cleaned_input = re.sub(r"don't\(\).*$", '', cleaned_input, flags=re.DOTALL)

    pattern = r'mul\((\d+),(\d+)\)'
    matches = re.findall(pattern, cleaned_input)

    return sum([int(a) * int(b) for a, b in matches])

if __name__ == '__main__':
    test_input = open('test_input.txt', 'r').read()
    input = open('input.txt', 'r').read()

    print('First part:')
    print(f'Test: {first_part(test_input)}')
    print(f'Answer: {first_part(input)}')

    print()

    print('Second part:')
    print(f'Test: {second_part(test_input)}')
    print(f'Answer: {second_part(input)}')