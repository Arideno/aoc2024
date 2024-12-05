def prepare_data(input: str) -> tuple[list[int], list[int]]:
    list1 = []
    list2 = []

    for line in input.split('\n'):
        a, b = [int(x) for x in line.split()]
        list1.append(a)
        list2.append(b)

    return list1, list2


def first_part(input: str) -> int:
    list1, list2 = prepare_data(input) 
    
    list1.sort()
    list2.sort()

    ans = 0

    for i in range(len(list1)):
        diff = abs(list1[i] - list2[i])
        ans += diff

    return ans

def second_part(input: str) -> int:
    list1, list2 = prepare_data(input)

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
    test_input = open('test_input.txt', 'r').read()
    input = open('input.txt', 'r').read()

    print('First part:')
    print(f'Test: {first_part(test_input)}')
    print(f'Answer: {first_part(input)}')

    print()

    print('Second part:')
    print(f'Test: {second_part(test_input)}')
    print(f'Answer: {second_part(input)}')