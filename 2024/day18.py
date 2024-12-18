### Day 18 - 2024

import pathlib
from helpers import *

directions = [
    (0, 1),
    (1, 0),
    (0, -1),
    (-1, 0)
]

def bfs(matrix: list[list[str]], rows: int, cols: int):
    queue = [(0, 0)]
    visited = set()
    path = {}

    while len(queue) > 0:
        x, y = queue.pop(0)

        if (x, y) == (rows - 1, cols - 1):
            break

        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            if not is_valid(nx, ny, rows, cols) or matrix[nx][ny] == '#' or (nx, ny) in visited:
                continue

            queue.append((nx, ny))
            visited.add((nx, ny))
            path[(nx, ny)] = (x, y)

    return path

def first_part(input: str, rows: int, cols: int, first: int) -> int:
    matrix = [['.' for _ in range(cols)] for _ in range(rows)]

    for line in input.splitlines()[:first]:
        y, x = extract_ints(line)
        matrix[x][y] = '#'

    path = bfs(matrix, rows, cols)

    x, y = rows - 1, cols - 1
    ans = 0

    while (x, y) != (0, 0):
        x, y = path[(x, y)]
        ans += 1

    return ans

def second_part(input: str, rows: int, cols: int, first: int) -> int:
    matrix = [['.' for _ in range(cols)] for _ in range(rows)]

    bytes = []
    for line in input.splitlines():
        bytes.append(extract_ints(line))

    for y, x in bytes[:first]:
        matrix[x][y] = '#'

    for y, x in bytes[first:]:
        matrix[x][y] = '#'
        path = bfs(matrix, rows, cols)
        if path.get((rows - 1, cols - 1)) is None:
            ans = f'{y},{x}'
            break

    return ans

if __name__ == '__main__':
    path = pathlib.Path(__file__).parent.parent.joinpath('data', '2024', 'day18')
    test_input = open(path.joinpath('input.test.txt'), 'r').read()
    input = open(path.joinpath('input.txt'), 'r').read()

    print('First part:')
    print(f'Test: {first_part(test_input, 7, 7, 12)}')
    print(f'Answer: {first_part(input, 71, 71, 1024)}')

    print()

    print('Second part:')
    print(f'Test: {second_part(test_input, 7, 7, 12)}')
    print(f'Answer: {second_part(input, 71, 71, 1024)}')
