### Day 8 - 2024

import pathlib
from helpers import *
    
def first_part(input: str) -> int:
    matrix = read_string_matrix(input)
    rows = len(matrix)
    cols = len(matrix[0])

    ans = 0

    visited = set()

    for i in range(rows):
        for j in range(cols):
            el = matrix[i][j]
            if el == '.':
                continue
            for x in range(rows):
                for y in range(cols):
                    if i == x and j == y:
                        continue
                    if matrix[x][y] == '.':
                        continue
                    if matrix[x][y] == el:
                        dx = x - i
                        dy = y - j
                        if is_valid(x + dx, y + dy, rows, cols) and not (x + dx, y + dy) in visited:
                            visited.add((x + dx, y + dy))
                            ans += 1
                        if is_valid(i - dx, j - dy, rows, cols) and not (i - dx, j - dy) in visited:
                            visited.add((i - dx, j - dy))
                            ans += 1
    
    return ans

def second_part(input: str) -> int:
    matrix = read_string_matrix(input)
    rows = len(matrix)
    cols = len(matrix[0])

    ans = 0

    visited = set()

    for i in range(rows):
        for j in range(cols):
            el = matrix[i][j]
            if el == '.':
                continue
            for x in range(rows):
                for y in range(cols):
                    if i == x and j == y:
                        continue
                    if matrix[x][y] == '.':
                        continue
                    if matrix[x][y] == el:
                        dx = x - i
                        dy = y - j

                        k, l = x, y

                        while is_valid(k, l, rows, cols):
                            if not (k, l) in visited:
                                visited.add((k, l))
                                ans += 1
                            
                            k += dx
                            l += dy

                        k, l = i, j

                        while is_valid(k, l, rows, cols):
                            if not (k, l) in visited:
                                visited.add((k, l))
                                ans += 1

                            k -= dx
                            l -= dy

    return ans

if __name__ == '__main__':
    path = pathlib.Path(__file__).parent.parent.joinpath('data', '2024', 'day08')
    test_input = open(path.joinpath('input.test.txt'), 'r').read()
    input = open(path.joinpath('input.txt'), 'r').read()

    print('First part:')
    print(f'Test: {first_part(test_input)}')
    print(f'Answer: {first_part(input)}')

    print()

    print('Second part:')
    print(f'Test: {second_part(test_input)}')
    print(f'Answer: {second_part(input)}')
