# Finished with the help of Reddit
# stage 1, needed to understand that not all splitters are used.  bottom row, 2nd from right
#          never splits anything
# Stage 2, someone pointed out that by keeping track of all the possible ways to get to a cell
#          by looking at the parent row to determine how to get there.

testing = False   # used for debugging messages and to pick the file
stage_2 = True    # used for more complex coding changes
debug_msg = 2
aocDay = '07'
file2read = 'Data/Day'+aocDay+'_Sample.txt' if testing else 'Data/Day'+aocDay+'_01.txt'
startChar = 'S'
splitChar = '^'
blankChar = '.'
branch_set = set()

from read_files import get_1line

thisMap = get_1line(file2read)
num_rows = len(thisMap)
num_col = len(thisMap[0])

beam_splitter = 0
results = [0] * num_col
newtree =[[0 for _ in range(num_col)] for _ in range(num_rows)]

for x in range(num_col):
    if thisMap[0][x] == startChar:
        cur_pos = [(0,x)]
        results[x] = 1
        newtree[0][x] = 1

for y in range(num_rows):
    for x in range(num_col):
        if thisMap[y][x] == splitChar and results[x] == 1:
            results[x] = 0
            results[x-1] = 1
            results[x+1] = 1
            beam_splitter += 1
            newtree[y][x-1] += newtree[y-1][x]
            newtree[y][x+1] += newtree[y-1][x]
        else:
            newtree[y][x] += newtree[y - 1][x]
total_paths = 0
for x in range(num_col):
    total_paths += newtree[num_rows - 1 ][x]


print(f'number of splitter is {beam_splitter}')
print(f'number of paths is {total_paths}')

# Part 1:
#  1716 is too high
