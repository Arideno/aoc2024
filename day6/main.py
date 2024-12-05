def first_part(input: str) -> int:
    pass

def second_part(input: str) -> int:
    pass

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