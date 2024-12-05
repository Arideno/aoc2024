def prepare_data(input: str) -> tuple[dict[int, int], list[list[int]]]:
    sections = input.strip().split('\n\n')
    rules_tuples = [[int(x) for x in line.split('|')] for line in sections[0].split('\n')]
    updates = [[int(x) for x in line.split(',')] for line in sections[1].split('\n')]

    rules = {}

    for x, y in rules_tuples:
        if x in rules:
            rules[x].append(y)
        else:
            rules[x] = [y]

    return rules, updates

def is_valid(update: list[int], rules: dict[int, int]) -> bool:
    is_valid = True
    for i in range(1, len(update)):
        if update[i] in rules:
            for j in range(i):
                if update[j] in rules[update[i]]:
                    is_valid = False
                    break

    return is_valid

def first_part(input: str) -> int:
    rules, updates = prepare_data(input)

    ans = 0

    for update in updates:
        if is_valid(update, rules):
            ans += update[len(update) // 2]

    return ans

def second_part(input: str) -> int:
    rules, updates = prepare_data(input)

    ans = 0

    incorrect_updates = []

    for update in updates:
        if not is_valid(update, rules):
            incorrect_updates.append(update)

    for update in incorrect_updates:
        while not is_valid(update, rules):
            for i in range(1, len(update)):
                if update[i] in rules:
                    for j in range(i):
                        if update[j] in rules[update[i]]:
                            update[i], update[j] = update[j], update[i]

    for update in incorrect_updates:
        ans += update[len(update) // 2]

    return ans

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