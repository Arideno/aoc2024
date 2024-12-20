import os
import argparse


def create_files_for_day(year: str, day: int):
    day_str = f'day{day:02d}'

    script_path = os.path.join(year, f'{day_str}.py')
    data_dir = os.path.join('data', year, day_str)
    input_path = os.path.join(data_dir, 'input.txt')
    test_input_path = os.path.join(data_dir, 'input.test.txt')

    code_template = f'''# Day {day} - {year}

import pathlib
from helpers import *

def first_part(input: str) -> int:
    pass

def second_part(input: str) -> int:
   pass

if __name__ == '__main__':
    path = pathlib.Path(__file__).parent.parent.joinpath(
        'data', '{year}', '{day_str}')
    test_input = open(path.joinpath('input.test.txt'), 'r').read()
    input = open(path.joinpath('input.txt'), 'r').read()

    print('First part:')
    print(f'Test: {{first_part(test_input)}}')
    print(f'Answer: {{first_part(input)}}')

    print()

    print('Second part:')
    print(f'Test: {{second_part(test_input)}}')
    print(f'Answer: {{second_part(input)}}')
'''

    os.makedirs(year, exist_ok=True)
    os.makedirs(data_dir, exist_ok=True)

    if not os.path.exists(script_path):
        with open(script_path, 'w') as f:
            f.write(code_template)
        print(f'Created {script_path}')
    else:
        print(f'{script_path} already exists')

    if not os.path.exists(input_path):
        with open(input_path, 'w') as f:
            f.write('')
        print(f'Created {input_path}')
    else:
        print(f'{input_path} already exists')

    if not os.path.exists(test_input_path):
        with open(test_input_path, 'w') as f:
            f.write('')
        print(f'Created {test_input_path}')
    else:
        print(f'{test_input_path} already exists')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Generate files for Advent of Code-style challenges.')
    parser.add_argument(
        'year',
        type=str,
        help='The year for which the files will be generated.'
    )
    parser.add_argument(
        'day',
        type=int,
        help='The day for which the files will be generated.'
    )

    args = parser.parse_args()

    create_files_for_day(args.year, args.day)
