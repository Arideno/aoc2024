### Day 9 - 2024

import pathlib
from helpers import *
    
def first_part(input: str) -> int:
    disc_map = [int(x) for x in list(input)]
    file_id = 0
    blocks = []

    for i in range(len(disc_map)):
        if i % 2 == 0:
            blocks = blocks + [file_id for i in range(disc_map[i])]
            file_id += 1
        else:
            blocks = blocks + [None for i in range(disc_map[i])]

    last_free_space_index = blocks.index(None)
    last_block_index = len(blocks) - 1

    while True:
        free_space_index = last_free_space_index
        block_to_move_index = last_block_index 

        while blocks[free_space_index] is not None:
            free_space_index += 1

        while blocks[block_to_move_index] is None:
            block_to_move_index -= 1

        last_free_space_index = free_space_index
        last_block_index = block_to_move_index

        if free_space_index > block_to_move_index:
            break

        blocks[free_space_index], blocks[block_to_move_index] = blocks[block_to_move_index], blocks[free_space_index]

    ans = 0

    i = 0

    while blocks[i] is not None and i < len(blocks):
        ans += i * blocks[i]
        i += 1

    return ans

def second_part(input: str) -> int:
    disc_map = [int(x) for x in list(input)]
    file_id = 0
    blocks = []

    for i in range(len(disc_map)):
        if i % 2 == 0:
            blocks = blocks + [file_id for i in range(disc_map[i])]
            file_id += 1
        else:
            blocks = blocks + [None for i in range(disc_map[i])]

    last_block_index = len(blocks) - 1

    while True:
        block_to_move_end_index = last_block_index

        while blocks[block_to_move_end_index] is None:
            block_to_move_end_index -= 1

        block_to_move_start_index = block_to_move_end_index
        file_id = blocks[block_to_move_end_index]

        while blocks[block_to_move_start_index] == file_id:
            block_to_move_start_index -= 1

        if blocks[block_to_move_start_index] != file_id:
            block_to_move_start_index += 1
        
        block_len = block_to_move_end_index - block_to_move_start_index + 1

        last_free_space_index = blocks.index(None)

        if last_free_space_index > block_to_move_end_index:
            break

        while True:
            free_space_start_index = last_free_space_index
            
            while blocks[free_space_start_index] is not None:
                free_space_start_index += 1

            free_space_end_index = free_space_start_index

            while free_space_end_index < len(blocks) and blocks[free_space_end_index] is None:
                free_space_end_index += 1

            if free_space_end_index >= len(blocks) or blocks[free_space_end_index] is not None:
                free_space_end_index -= 1

            if free_space_start_index > block_to_move_end_index:
                last_free_space_index = None
                break

            free_space_len = free_space_end_index - free_space_start_index + 1

            if block_len <= free_space_len:
                for i in range(block_len):
                    blocks[block_to_move_start_index + i] = None
                    blocks[free_space_start_index + i] = file_id
                break
            else:
                last_free_space_index = free_space_end_index + 1
        
        if last_free_space_index is None:
            last_block_index = block_to_move_start_index - 1
            last_free_space_index = blocks.index(None)

    ans = 0

    for i in range(len(blocks)):
        if blocks[i] is not None:
            ans += i * blocks[i]

    return ans

if __name__ == '__main__':
    path = pathlib.Path(__file__).parent.parent.joinpath('data', '2024', 'day09')
    test_input = open(path.joinpath('input.test.txt'), 'r').read()
    input = open(path.joinpath('input.txt'), 'r').read()

    print('First part:')
    print(f'Test: {first_part(test_input)}')
    print(f'Answer: {first_part(input)}')

    print()

    print('Second part:')
    print(f'Test: {second_part(test_input)}')
    print(f'Answer: {second_part(input)}')
