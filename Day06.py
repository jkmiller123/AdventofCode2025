testing = False   # used for debugging messages and to pick the file
stage_2 = True    # used for more complex coding changes
debug_msg = 2
aocDay = '06'
file2read = 'Data/Day'+aocDay+'_Sample.txt' if testing else 'Data/Day'+aocDay+'_01.txt'

from read_files import get_2d_lists
from read_files import get_1line

math_data = get_2d_lists(file2read)
math_data2 = get_1line(file2read)

num_rows = len(math_data) - 1
num_actions = len(math_data[0])
actions = math_data[num_rows]

def part_01():
    grand_total = 0
    for x in range(num_actions):
        running_total = 0 if math_data[num_rows][x] == '+' else 1
        for y in range(num_rows):
            if math_data[num_rows][x] == '+':
                running_total += int(math_data[y][x])
            else:
                if debug_msg >= 2:
                  print(f'#{x} has {int(math_data[y][x])} with total {running_total} ')
                running_total *= int(math_data[y][x])
        grand_total += running_total
        if debug_msg >= 1:
            print(f'problem # {x} = {running_total}')

    print(f'Part 1: The grand total is {grand_total}')

def part_02():
    # the positing of the numbers make a difference in the calculation
    column_number = 0
    grand_total = 0
    size_of_input = 0
    for y in range(num_rows):
        size_of_input = max(size_of_input, len(math_data2[y]))
    running_total = 0 if actions[0] == '+' else 1
    for x in range(size_of_input ):
        # check for new column
        thisNumber = ''
        new_column = True
        for y in range(num_rows):
            if x < len(math_data2[y]):
                if math_data2[y][x] != ' ':
                    new_column = False
                    thisNumber += math_data2[y][x]

        if debug_msg >= 2:
            if not new_column:
                print(f'{actions[column_number]} ', end='')
            print(f' {thisNumber} ', end='')

        if new_column:
            print(f'Running_total = {running_total}')
            grand_total += running_total

            column_number += 1
            running_total = 0 if actions[column_number] == '+' else 1

            print(f'')
        else:
            if actions[column_number] == '+':
                running_total += int(thisNumber)
            else:
                running_total *= int(thisNumber)
    grand_total += running_total
    print(f'Running_total = {running_total}')
    print(f'Grand Total = {grand_total}')

    print(f'In Part 2')

if stage_2:
    part_02()
else:
    part_01()

# Part 1 :
#  5,171,061,454,237  too low
#  5,171,061,464,548  is correct
