
testing = False   # used for debugging messages and to pick the file
stage_2 = True    # used for more complex coding changes
file2read = 'Data/Day01_Sample.txt' if testing else 'Data/Day01_01.txt'
pos = 50   # The dial starts by pointing at 50
goalPos = 0  # the number of times the dial is left pointing at 0 after any rotation in the sequence
loopCounter = 0  # number of times past the position

from read_files import get_1line

map = get_1line(file2read)
counter = 0
for turns in map:
    direction = turns[0]   # Left or Right
    rotationAmount = int(turns[1:])   # how many numbers can be over 100
    if rotationAmount > 100:
        turnaround = rotationAmount // 100   # how many times around the dial
        rotationAmount -= turnaround * 100   # remove it, so that only the two digit number remains
        if stage_2:
            loopCounter += turnaround

    rotationAmount *= 1 if direction == 'R' else -1
    new_pos = pos + rotationAmount

    if new_pos < 0:
        pos = 100 + new_pos
        loopCounter += 1 if stage_2 else 0
    elif new_pos > 99:
        pos = new_pos - 100
        loopCounter += 1 if stage_2 else 0
    else:
        pos = new_pos
    if  stage_2 and pos == 0:
        loopCounter += 1

    print(f'{loopCounter:05d} {turns} ends at {pos}')

print(f'{loopCounter} ')
#511 is too low for part 1
# Part 2
# 6698 is too low
# 7848 is too high




