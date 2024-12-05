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

def is_valid(x: int, y: int) -> bool:
    global rows, cols
    return 0 <= x < rows and 0 <= y < cols

def check(x: int, y: int, dx: int, dy: int) -> bool:
    global matrix

    word = 'XMAS'
    for i in range(len(word)):
        nx, ny = x + i * dx, y + i * dy
        if not is_valid(nx, ny) or matrix[nx][ny] != word[i]:
            return False
    return True

def check_x_mas(x: int, y: int) -> int:
    global matrix

    ans = 0
        
    mas = 'MAS'
    mas_reverse = mas[::-1]

    first_diag = matrix[x-1][y-1] + matrix[x][y] + matrix[x+1][y+1]
    second_diag = matrix[x-1][y+1] + matrix[x][y] + matrix[x+1][y-1]

    if (first_diag == mas or first_diag == mas_reverse) and (second_diag == mas or second_diag == mas_reverse):
        ans += 1

    return ans

def prepare_data(input: str):
    global matrix, rows, cols

    matrix = []

    for line in input.split('\n'):
        matrix.append(list(line.strip()))

    rows = len(matrix)
    cols = len(matrix[0])

def first_part(input: str) -> int:
    prepare_data(input)

    ans = 0

    for i in range(rows):
        for j in range(cols):
            for dx, dy in directions:
                if check(i, j, dx, dy):
                    ans += 1
    
    return ans

def second_part(input: str) -> int:
    prepare_data(input)

    ans = 0

    for x in range(1, rows - 1):
        for y in range(1, cols - 1):
            ans += check_x_mas(x, y)

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