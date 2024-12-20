# Day 20 - 2024

import pathlib
from helpers import *
from collections import deque
from heapq import heappush, heappop

directions = [
    (0, 1),
    (0, -1),
    (1, 0),
    (-1, 0)
]


def bfs(matrix, s, e):
    rows = len(matrix)
    cols = len(matrix[0])
    pq = []
    heappush(pq, (0, s))
    visited = set([s])
    path = {}

    while len(pq) > 0:
        steps, (x, y) = heappop(pq)

        if (x, y) == e:
            break

        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            if not is_valid(nx, ny, rows, cols):
                continue

            if matrix[nx][ny] != '#' and (nx, ny) not in visited:
                visited.add((nx, ny))
                heappush(pq, (steps + 1, (nx, ny)))
                path[(nx, ny)] = (x, y)

    return path


def first_part(input: str) -> int:
    matrix = read_string_matrix(input)
    rows = len(matrix)
    cols = len(matrix[0])

    sx, sy = 0, 0
    ex, ey = 0, 0

    for x in range(rows):
        for y in range(cols):
            if matrix[x][y] == 'S':
                sx, sy = x, y
            if matrix[x][y] == 'E':
                ex, ey = x, y

    ans = 0

    pd = bfs(matrix, (sx, sy), (ex, ey))
    p = (ex, ey)
    path = []

    while p != (sx, sy):
        path.append(p)
        p = pd[p]

    path.append((sx, sy))
    path.reverse()

    for i in range(len(path)):
        for j in range(i, len(path)):
            md = abs(path[i][0] - path[j][0]) + abs(path[i][1] - path[j][1])
            if md == 2 and j - i - md >= 100:
                ans += 1

    return ans


def second_part(input: str) -> int:
    matrix = read_string_matrix(input)
    rows = len(matrix)
    cols = len(matrix[0])

    sx, sy = 0, 0
    ex, ey = 0, 0

    for x in range(rows):
        for y in range(cols):
            if matrix[x][y] == 'S':
                sx, sy = x, y
            if matrix[x][y] == 'E':
                ex, ey = x, y

    ans = 0

    pd = bfs(matrix, (sx, sy), (ex, ey))
    p = (ex, ey)
    path = []

    while p != (sx, sy):
        path.append(p)
        p = pd[p]

    path.append((sx, sy))
    path.reverse()

    for i in range(len(path)):
        for j in range(i, len(path)):
            md = abs(path[i][0] - path[j][0]) + abs(path[i][1] - path[j][1])
            if md <= 20 and j - i - md >= 100:
                ans += 1

    return ans


if __name__ == "__main__":
    path = pathlib.Path(__file__).parent.parent.joinpath(
        'data', '2024', 'day20')
    test_input = open(path.joinpath('input.test.txt'), 'r').read()
    input = open(path.joinpath('input.txt'), 'r').read()

    print('First part:')
    print(f'Test: {first_part(test_input)}')
    print(f'Answer: {first_part(input)}')

    print()

    print('Second part:')
    print(f'Test: {second_part(test_input)}')
    print(f'Answer: {second_part(input)}')
