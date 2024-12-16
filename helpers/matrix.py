def is_valid(x: int, y: int, rows: int, cols: int) -> bool:
    return 0 <= x < rows and 0 <= y < cols

def read_string_matrix(s: str) -> list[list[str]]:
    return [list(row) for row in s.splitlines()]

def read_int_matrix(s: str) -> list[list[int]]:
    return [[int(cell) for cell in row] for row in s.splitlines()]