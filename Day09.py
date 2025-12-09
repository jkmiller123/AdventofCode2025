import math

testing = True # used for debugging messges and to pick the file
stage_2 = True  # used for more complex coding changes
aocDay = '09'
file2read = 'Data/Day' + aocDay + '_Sample.txt' if testing else 'Data/Day' + aocDay + '_01.txt'

from read_files import get_3d_set

red_map = get_3d_set(file2read)
num_squares = len(red_map)

def part_1():
    loc1 = 0
    loc2 = 0
    max_area = 0
    for x in range(num_squares):
        for y in range(x+1,num_squares):
            x1, y1 = red_map[x]
            x2, y2 = red_map[y]
            area = (abs(x1-x2)+1) * (abs(y1-y2)+1)
            if area > max_area:
                max_area = area
                loc1 = x
                loc2 = y
    x1,y1 = red_map[loc1]
    x2, y2 = red_map[loc2]
    max_area = (abs(x1-x2)+1) * (abs(y1-y2)+1)
    print(f'max area is {max_area}')
    print(f'Rectange of dimensions {abs(x1-x2)+1} by {(abs(y1-y2)+1)}')
    return

def part_2():
    green_map = []
    for x in range(num_squares):
        x1, y1 = red_map[x]
        for y in range(x + 1, num_squares):
            x2, y2 = red_map[y]
            if x2 == x1 or y2 == y1:
                aset = tuple((x2, y2))
                green_map.append(aset)
                print(f'0', end='')
            else:
                if x2 == x1 and y2 == y1:
                    print(f'#', end='')
                else:
                    print(f'.', end = '')
        print(f'')

part_1()
part_2()

# Part 1
# 4664032812 is too low