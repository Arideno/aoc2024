import pathlib

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

    ans = 0

    q = [(0, sx, sy, 3)]
    visited = {}

    while len(q) > 0:
        s, x, y, d = q.pop(0)

        if (x, y, d) in visited and visited[(x, y, d)] < s:
            continue

        visited[(x, y, d)] = s

        if x == fx and y == fy:
            continue

        nx, ny = x + directions[d][0], y + directions[d][1]
        if is_valid(nx, ny, rows, cols) and matrix[nx][ny] != '#':
            q.append((s + 1, nx, ny, d))

        q.append((s + 1000, x, y, (d + 1) % 4))
        q.append((s + 1000, x, y, (d - 1) % 4))

    ans = 10**9
    for d in range(4):
        if (fx, fy, d) in visited:
            ans = min(ans, visited[(fx, fy, d)])

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

    ans = 0

    q = [(0, sx, sy, 3, set([]))]
    visited = {}
    bs = 10**9
    ans = set()

    while len(q) > 0:
        s, x, y, d, path = q.pop(0)

        if (x, y, d) in visited and visited[(x, y, d)] < s:
            continue

        visited[(x, y, d)] = s

        if x == fx and y == fy:
            if s < bs:
                bs = s
                ans = set()
                ans.update(path)
            elif s == bs:
                ans.update(path)
            continue

        nx, ny = x + directions[d][0], y + directions[d][1]
        if is_valid(nx, ny, rows, cols) and matrix[nx][ny] != '#':
            q.append((s + 1, nx, ny, d, path.union([(x, y)])))

        q.append((s + 1000, x, y, (d + 1) % 4, path))
        q.append((s + 1000, x, y, (d - 1) % 4, path))

    return len(ans) + 1

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