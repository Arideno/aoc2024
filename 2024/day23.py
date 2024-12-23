# Day 23 - 2024

import pathlib
from collections import defaultdict
from helpers import *


def first_part(input: str) -> int:
    g = defaultdict(set)
    for line in input.splitlines():
        a, b = line.split('-')
        g[a].add(b)
        g[b].add(a)

    triangles = set()

    for node in g:
        neighbors = g[node]
        for neighbor in neighbors:
            common_neighbors = neighbors.intersection(g[neighbor])
            for common_neighbor in common_neighbors:
                triangles.add(tuple(sorted([node, neighbor, common_neighbor])))

    ans = 0

    for triangle in triangles:
        if any(node.startswith('t') for node in triangle):
            ans += 1

    return ans


def is_clique(g, nodes) -> bool:
    for i in range(len(nodes) - 1):
        for j in range(i + 1, len(nodes)):
            if nodes[j] not in g[nodes[i]]:
                return False
    return True


def find_max_clique(g, nodes, start, curr, max):
    if len(curr) > len(max):
        max = curr.copy()

    for i in range(start, len(nodes)):
        curr.append(nodes[i])
        if is_clique(g, curr):
            max = find_max_clique(g, nodes, i + 1, curr, max)
        curr.pop()

    return max


def second_part(input: str) -> int:
    g = defaultdict(set)
    for line in input.splitlines():
        a, b = line.split('-')
        g[a].add(b)
        g[b].add(a)

    nodes = list(g.keys())
    max_clique = find_max_clique(g, nodes, 0, [], [])
    max_clique = sorted(max_clique)

    return ','.join(max_clique)


if __name__ == '__main__':
    path = pathlib.Path(__file__).parent.parent.joinpath(
        'data', '2024', 'day23')
    test_input = open(path.joinpath('input.test.txt'), 'r').read()
    input = open(path.joinpath('input.txt'), 'r').read()

    print('First part:')
    print(f'Test: {first_part(test_input)}')
    print(f'Answer: {first_part(input)}')

    print()

    print('Second part:')
    print(f'Test: {second_part(test_input)}')
    print(f'Answer: {second_part(input)}')
