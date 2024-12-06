def prepare_data(input: str) -> list[list[str]]:
    return [list(row) for row in input.split('\n')]

def first_part(input: str) -> int:
    matrix = prepare_data(input)
    rows = len(matrix)
    cols = len(matrix[0])

    guard_x, guard_y = 0, 0
    guard_direction = (-1, 0)

    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == '^':
                guard_x, guard_y = i, j

    visited = set()
    visited.add((guard_x, guard_y, guard_direction))
    matrix[guard_x][guard_y] = 'X'

    x, y = guard_x, guard_y
    
    while True:
        x += guard_direction[0]
        y += guard_direction[1]

        if x < 0 or x >= rows or y < 0 or y >= cols:
            break

        if matrix[x][y] == '#':
            x -= guard_direction[0]
            y -= guard_direction[1]
            guard_direction = (guard_direction[1], -guard_direction[0])
            continue
        
        if (x, y, guard_direction) in visited:
            break

        visited.add((x, y, guard_direction))
        matrix[x][y] = 'X'

    return sum([row.count('X') for row in matrix])

def second_part(input: str) -> int:
    matrix = prepare_data(input)
    rows = len(matrix)
    cols = len(matrix[0])

    guard_x, guard_y = 0, 0    

    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == '^':
                guard_x, guard_y = i, j

    loop_count = 0
    
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == '.':
                matrix[i][j] = '#'

                guard_direction = (-1, 0)

                visited = set()
                visited.add((guard_x, guard_y, guard_direction))

                x, y = guard_x, guard_y
                while True:
                    x += guard_direction[0]
                    y += guard_direction[1]

                    if x < 0 or x >= rows or y < 0 or y >= cols:
                        break

                    if matrix[x][y] == '#':
                        x -= guard_direction[0]
                        y -= guard_direction[1]
                        guard_direction = (guard_direction[1], -guard_direction[0])
                        continue
                    
                    if (x, y, guard_direction) in visited:
                        loop_count += 1
                        break

                    visited.add((x, y, guard_direction))
                
                matrix[i][j] = '.'

    return loop_count

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