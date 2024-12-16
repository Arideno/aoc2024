### Day 12 - 2024

import pathlib
from helpers import *
    
directions = [
    (0, 1),
    (1, 0),
    (0, -1),
    (-1, 0)
]

def first_part(input: str) -> int:
    matrix = read_string_matrix(input)
    rows = len(matrix)
    cols = len(matrix[0])

    ans = 0

    visited = set()

    for i in range(rows):
        for j in range(cols):
            if (i, j) not in visited:
                queue = [(i, j)]
                visited.add((i, j))
                area = 0
                perim = 0
                char = matrix[i][j]

                while len(queue) > 0:
                    x, y = queue.pop(0)
                    area += 1

                    for dx, dy in directions:
                        nx, ny = x + dx, y + dy
                        if is_valid(nx, ny, rows, cols):
                            if matrix[nx][ny] == char and (nx, ny) not in visited:
                                queue.append((nx, ny))
                                visited.add((nx, ny))
                            elif matrix[nx][ny] != char:
                                perim += 1
                        else:
                            perim += 1

                ans += area * perim

    return ans

def second_part(input: str) -> int:
    matrix = read_string_matrix(input)
    rows = len(matrix)
    cols = len(matrix[0])

    ans = 0

    visited = set()

    for i in range(rows):
        for j in range(cols):
            if (i, j) not in visited:
                queue = [(i, j)]
                visited.add((i, j))
                area = 0
                edges = set()
                char = matrix[i][j]

                while len(queue) > 0:
                    x, y = queue.pop(0)
                    area += 1

                    for d, (dx, dy) in enumerate(directions):
                        nx, ny = x + dx, y + dy
                        if is_valid(nx, ny, rows, cols):
                            if matrix[nx][ny] == char and (nx, ny) not in visited:
                                queue.append((nx, ny))
                                visited.add((nx, ny))
                            elif matrix[nx][ny] != char:
                                edges.add((x, y, d))
                        else:
                            edges.add((x, y, d))

                adj_edges = 0
                for (x, y, d) in edges:
                    nx, ny = x + directions[d][1], y + directions[d][0]
                    if (nx, ny, d) in edges:
                        adj_edges += 1

                sides = len(edges) - adj_edges

                ans += area * sides

    return ans

if __name__ == '__main__':
    path = pathlib.Path(__file__).parent.parent.joinpath('data', '2024', 'day12')
    test_input = open(path.joinpath('input.test.txt'), 'r').read()
    input = open(path.joinpath('input.txt'), 'r').read()

    print('First part:')
    print(f'Test: {first_part(test_input)}')
    print(f'Answer: {first_part(input)}')

    print()

    print('Second part:')
    print(f'Test: {second_part(test_input)}')
    print(f'Answer: {second_part(input)}')
