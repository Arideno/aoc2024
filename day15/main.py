import pathlib

directions = {
    '<': (0, -1),
    '>': (0, 1),
    '^': (-1, 0),
    'v': (1, 0)
}

def first_part(input: str) -> int:
    matrix = []
    matrix_input, moves_input = input.split('\n\n')

    for line in matrix_input.split('\n'):
        matrix.append(list(line))

    moves = ''.join(moves_input.split('\n'))

    rows = len(matrix)
    cols = len(matrix[0])
    rx, ry = 0, 0

    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == '@':
                rx, ry = i, j
                break

    for move in moves:
        direction = directions[move]
        nrx, nry = rx + direction[0], ry + direction[1]

        if matrix[nrx][nry] == '#':
            continue

        if matrix[nrx][nry] == 'O':
            nx, ny = nrx, nry
            while matrix[nx][ny] == 'O':
                nx, ny = nx + direction[0], ny + direction[1]

            if matrix[nx][ny] == '#':
                continue

            matrix[nrx][nry] = '@'
            if direction[0] != 0:
                for i in range(nrx+direction[0], nx+direction[0], direction[0]):
                    matrix[i][ny] = 'O'

            if direction[1] != 0:
                for i in range(nry+direction[1], ny+direction[1], direction[1]):
                    matrix[nx][i] = 'O'

            matrix[rx][ry] = '.'
            rx, ry = nrx, nry
        else:
            matrix[nrx][nry] = '@'
            matrix[rx][ry] = '.'
            rx, ry = nrx, nry

    ans = 0

    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 'O':
                ans += 100 * i + j

    return ans

def can_move(matrix, rx, ry, dx, dy) -> bool:
    nx = rx + dx
    ny = ry + dy

    if matrix[nx][ny] == '#':
        return False

    if matrix[nx][ny] == '.':
        return True

    if dx != 0:
        if matrix[nx][ny] == '[':
            return can_move(matrix, nx, ny, dx, dy) and can_move(matrix, nx, ny+1, dx, dy)
        else:
            return can_move(matrix, nx, ny, dx, dy) and can_move(matrix, nx, ny-1, dx, dy)

    if matrix[nx][ny] == '[':
        return can_move(matrix, nx, ny+1, dx, dy)
    else:
        return can_move(matrix, nx, ny-1, dx, dy)

def move(matrix, rx, ry, dx, dy):
    nx, ny = rx + dx, ry + dy

    if matrix[nx][ny] == '#':
        return

    if matrix[nx][ny] == '.':
        matrix[rx][ry], matrix[nx][ny] = matrix[nx][ny], matrix[rx][ry]
        return

    if dx != 0:
        if matrix[nx][ny] == '[':
            move(matrix, nx, ny, dx, dy)
            move(matrix, nx, ny+1, dx, dy)
            matrix[rx][ry], matrix[nx][ny] = matrix[nx][ny], matrix[rx][ry]
        else:
            move(matrix, nx, ny, dx, dy)
            move(matrix, nx, ny-1, dx, dy)
            matrix[rx][ry], matrix[nx][ny] = matrix[nx][ny], matrix[rx][ry]
        return

    if matrix[nx][ny] == '[':
        move(matrix, nx, ny+1, dx, dy)
        matrix[nx][ny+1], matrix[nx][ny], matrix[rx][ry] = matrix[nx][ny], matrix[rx][ry], matrix[nx][ny+1]
    else:
        move(matrix, nx, ny-1, dx, dy)
        matrix[nx][ny-1], matrix[nx][ny], matrix[rx][ry] = matrix[nx][ny], matrix[rx][ry], matrix[nx][ny-1]

def second_part(input: str) -> int:
    matrix = []
    matrix_input, moves_input = input.split('\n\n')

    for line in matrix_input.split('\n'):
        new_line = ''
        for char in line:
            if char == 'O':
                new_line += '[]'
            elif char == '#':
                new_line += '##'
            elif char == '.':
                new_line += '..'
            else:
                new_line += '@.'
        matrix.append(list(new_line))

    moves = ''.join(moves_input.split('\n'))

    rows = len(matrix)
    cols = len(matrix[0])
    rx, ry = 0, 0

    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == '@':
                rx, ry = i, j
                break

    for m in moves:
        dx, dy = directions[m]
        if can_move(matrix, rx, ry, dx, dy):
            move(matrix, rx, ry, dx, dy)
            rx, ry = rx + dx, ry + dy

    ans = 0

    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == '[':
                ans += 100 * i + j

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