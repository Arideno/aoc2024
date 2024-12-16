import pathlib
from queue import PriorityQueue

directions = [
    (-1, 0),
    (0, -1),
    (1, 0),
    (0, 1)
]

def is_valid(x: int, y: int, rows: int, cols: int) -> bool:
    return x >= 0 and x < rows and y >= 0 and y < cols

def first_part(input: str) -> int:
    matrix = []

    for line in input.split('\n'):
        matrix.append(list(line))

    rows = len(matrix)
    cols = len(matrix[0])

    sx, sy = 0, 0
    fx, fy = 0, 0

    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 'S':
                sx, sy = i, j
            elif matrix[i][j] == 'E':
                fx, fy = i, j

    pq = PriorityQueue()
    pq.put((0, sx, sy, 3))
    visited = set()

    while not pq.empty():
        s, x, y, d = pq.get()

        if (x, y, d) in visited:
            continue

        if x == fx and y == fy:
            ans = s
            break

        visited.add((x, y, d))

        nx, ny = x + directions[d][0], y + directions[d][1]
        if is_valid(nx, ny, rows, cols) and matrix[nx][ny] != '#':
            pq.put((s + 1, nx, ny, d))

        pq.put((s + 1000, x, y, (d + 1) % 4))
        pq.put((s + 1000, x, y, (d - 1) % 4))

    return ans

def second_part(input: str) -> int:
    matrix = []

    for line in input.split('\n'):
        matrix.append(list(line))

    rows = len(matrix)
    cols = len(matrix[0])

    sx, sy = 0, 0
    fx, fy = 0, 0

    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 'S':
                sx, sy = i, j
            elif matrix[i][j] == 'E':
                fx, fy = i, j

    pq = PriorityQueue()
    pq.put((0, sx, sy, 3, set()))
    visited = {}
    best = 10**9
    all_pos = set()

    while not pq.empty():
        s, x, y, d, pos = pq.get()

        if (x, y, d) in visited and visited[(x, y, d)] < s:
            continue

        if x == fx and y == fy:
            if s < best:
                best = s
                all_pos = pos
            elif s == best:
                all_pos.update(pos)
            continue

        visited[(x, y, d)] = s

        nx, ny = x + directions[d][0], y + directions[d][1]
        if is_valid(nx, ny, rows, cols) and matrix[nx][ny] != '#':
            pq.put((s + 1, nx, ny, d, pos.union([(nx, ny)])))

        pq.put((s + 1000, x, y, (d + 1) % 4, pos))
        pq.put((s + 1000, x, y, (d - 1) % 4, pos))

    return len(all_pos) + 1

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