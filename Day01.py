
testing = False   # used for debugging messages and to pick the file
stage_2 = True    # used for more complex coding changes
file2read = 'Data/Day01_Sample.txt' if testing else 'Data/Day01_01.txt'
pos = 50   # The dial starts by pointing at 50
goalPos = 0  # the number of times the dial is left pointing at 0 after any rotation in the sequence
loopCounter = 0  # number of times past the position

from read_files import get_1line

map = get_1line(file2read)
counter = 0
for rows in map:
    direction= rows[0]
    rotationAmount = int(rows[1:])
    if rotationAmount > 100:
        turnaround = rotationAmount // 100
        rotationAmount -= turnaround * 100
        if stage_2:
            loopCounter += turnaround

    new_pos = pos + rotationAmount if direction == 'R' else pos - rotationAmount

    if new_pos < 0:
        pos = 100 + new_pos
        loopCounter += 1 if stage_2 else 0
    elif new_pos > 99:
        pos = new_pos - 100
        loopCounter += 1 if stage_2 else 0
    else:
        pos = new_pos
    if not stage_2 and pos == 0:
        loopCounter += 1

    print(f'{loopCounter:05d} {rows} ends at {pos}')

print(f'{loopCounter} ')
#511 is too low for part 1
# 6698 is too low for part 2




