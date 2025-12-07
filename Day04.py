from typing import List

testing = True   # used for debugging messages and to pick the file
stage_2 = False    # used for more complex coding changes
aocDay = '04'
file2read = 'Data/Day'+aocDay+'_Sample.txt' if testing else 'Data/Day'+aocDay+'_01.txt'
max_rolls = 4   # Maximum number of rolls allowed in area
symbol_paper = '@'
grid_size = 3  #  3x3

from read_files import get_2d_char

def part1(my_map):
    # count the rolls (@) that have fewer than max_rolls within the surronding grid
    max_rows = len(my_map)
    max_cols = len(my_map[0])
    print(f'{max_cols} x {max_rows}')
    rolls_to_remove = 0
    for y in range(max_rows):
        for x in range(max_cols):
            num_rolls = 0
            if my_map[y][x] == symbol_paper:
                check_min_y = y - 1 if y > 0 else 0
                check_max_y = y + 1 if y <= max_rows else max_rows
                check_min_x = x - 1 if x > 0 else 0
                check_max_x = x + 1 if x <= max_cols else max_cols
                print(f'{x} : [{check_min_x} {check_max_x}] ')
                for y1 in range(check_min_y, min(max_rows, check_max_y + 1 )  , 1):
                    for x1 in range(check_min_x, min(max_cols, check_max_x + 1 ) , 1):
                        print(f'      {y1} --  ( {x1} ) ', end="")
                        if my_map[y1][x1] == symbol_paper:
                           num_rolls += 1
                    print(f"")
            if num_rolls >= max_rolls + 1:
                rolls_to_remove += 1

    print(f'Total rolls to remove {rolls_to_remove}')

    
def part2(map):
    print(f'In Part 2')
    
    
paperRollmap: list[list[chr]] = get_2d_char(file2read)

part1(paperRollmap)
if stage_2:
    part2(paperRollmap)

for t in range(5,8,1):
    print(f' {t}')
