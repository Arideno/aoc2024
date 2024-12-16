### Day 4 - 2024

import pathlib
from helpers import *
    
directions = [
    (0, 1),
    (1, 0),
    (0, -1),
    (-1, 0),
    (1, 1),
    (1, -1),
    (-1, 1),
    (-1, -1)
]

def check(x: int, y: int, dx: int, dy: int, matrix: list[list[str]]) -> bool:
    rows, cols = len(matrix), len(matrix[0])

    word = 'XMAS'
    for i in range(len(word)):
        nx, ny = x + i * dx, y + i * dy
        if not is_valid(nx, ny, rows, cols) or matrix[nx][ny] != word[i]:
            return False

    return True

def check_x_mas(x: int, y: int, matrix: list[list[str]]) -> int:
    ans = 0
        
    mas = 'MAS'
    mas_reverse = mas[::-1]

    first_diag = matrix[x-1][y-1] + matrix[x][y] + matrix[x+1][y+1]
    second_diag = matrix[x-1][y+1] + matrix[x][y] + matrix[x+1][y-1]

    if (first_diag == mas or first_diag == mas_reverse) and (second_diag == mas or second_diag == mas_reverse):
        ans += 1

    return ans

def first_part(input: str) -> int:
    matrix = read_string_matrix(input)
    rows, cols = len(matrix), len(matrix[0])

    ans = 0

    for i in range(rows):
        for j in range(cols):
            for dx, dy in directions:
                if check(i, j, dx, dy, matrix):
                    ans += 1
    
    return ans

def second_part(input: str) -> int:
    matrix = read_string_matrix(input)
    rows, cols = len(matrix), len(matrix[0])

    ans = 0

    for x in range(1, rows - 1):
        for y in range(1, cols - 1):
            ans += check_x_mas(x, y, matrix)

    return ans

if __name__ == '__main__':
    path = pathlib.Path(__file__).parent.parent.joinpath('data', '2024', 'day04')
    test_input = open(path.joinpath('input.test.txt'), 'r').read()
    input = open(path.joinpath('input.txt'), 'r').read()

    print('First part:')
    print(f'Test: {first_part(test_input)}')
    print(f'Answer: {first_part(input)}')

    print()

    print('Second part:')
    print(f'Test: {second_part(test_input)}')
    print(f'Answer: {second_part(input)}')
