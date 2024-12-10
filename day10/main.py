import pathlib

directions = [
    (0, 1),
    (1, 0),
    (0, -1),
    (-1, 0)
]

def is_valid(x: int, y: int, rows: int, cols: int) -> bool:
    return 0 <= x < rows and 0 <= y < cols

def bfs(start_x: int, start_y: int, matrix: list[list[int]]) -> int:
    rows = len(matrix)
    cols = len(matrix[0])
    visited = set()
    nines = set()
    queue = [(start_x, start_y, 0)]

    while len(queue) > 0:
        x, y, height = queue.pop(0)

        if (x, y) in visited:
            continue

        visited.add((x, y))

        if matrix[x][y] == 9:
            nines.add((x, y))
            continue

        for direction in directions:
            i = x + direction[0]
            j = y + direction[1]

            if is_valid(i, j, rows, cols) and matrix[i][j] == height + 1:
                queue.append((i, j, height + 1))

    return len(nines)

def dfs(start_x: int, start_y: int, matrix: list[list[int]], height: int, visited: set) -> int:
    rows = len(matrix)
    cols = len(matrix[0])

    if not is_valid(start_x, start_y, rows, cols) or (start_x, start_y) in visited or matrix[start_x][start_y] != height:
        return 0

    if matrix[start_x][start_y] == 9:
        return 1

    visited.add((start_x, start_y))

    trails = 0

    for direction in directions:
        trails += dfs(start_x + direction[0], start_y + direction[1], matrix, height + 1, visited)

    visited.remove((start_x, start_y))

    return trails

def first_part(input: str) -> int:
    matrix = []
    for line in input.split('\n'):
        matrix.append([int(c) for c in line])

    rows = len(matrix)
    cols = len(matrix[0])

    ans = 0

    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 0:
                ans += bfs(i, j, matrix)

    return ans

def second_part(input: str) -> int:
    matrix = []
    for line in input.split('\n'):
        matrix.append([int(c) for c in line])

    rows = len(matrix)
    cols = len(matrix[0])

    ans = 0

    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 0:
                ans += dfs(i, j, matrix, 0, set())

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