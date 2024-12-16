import re

def extract_ints(raw: str) -> list[int]:
    return list(map(int, re.findall(r"((?:-|\+)?\d+)", raw)))