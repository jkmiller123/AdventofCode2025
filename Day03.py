testing = False   # used for debugging messages and to pick the file
stage_2 = True    # used for more complex coding changes
aocDay = '03'
file2read = 'Data/Day'+aocDay+'_Sample.txt' if testing else 'Data/Day'+aocDay+'_01.txt'
pos = 50   # The dial starts by pointing at 50
goalPos = 0  # the number of times the dial is left pointing at 0 after any rotation in the sequence
loopCounter = 0  # number of times past the position

from read_files import get_2d_int

def part_01(data_list):
    print(f'In part 1')
    grand_total = 0
    for block in data_list:
        small_list = block[0:len(block)-1]
        largest = max(small_list)
        pos = block.index(largest)
        remain_list = block[pos+1:]
        next_largest = max(remain_list)
        new_value = largest*10 + next_largest
      #  print(f'{new_value} is the largest 2 digit value of {block}')
        grand_total += new_value
    print(f'Total Output for Part 1 is {grand_total}')

def part_02(data_list):
    print(f'In Part 2')
    grand_total = 0
    dg1 = 0
    for block in data_list:
        new_value = 0
        small_list = block
        dg2 = 0   # digit counter number 2,
        for digit_counter in range(11,-1,-1):
         #   print(f'{dg2}, {len(block)} , {digit_counter} = {len(block) - digit_counter}')
            small_list = block[dg2:len(block)-digit_counter]
            largest = max(small_list)
            pos = small_list.index(largest)
            new_value = new_value * 10 + largest
          # print(f'{dg1}:{dg2} subset list is {small_list} current largest is {new_value}')
            dg2 += 1 + pos
        dg1 += 1
        grand_total += new_value
    print(f'Total Output for Part 2 is {grand_total}')

 #           remain_list = block[pos+1:]
 #           next_largest = max(remain_list)
 #           new_value = new_value*10 + next_largest
#        print(f'{new_value} is the largest 12 digit value of {block}')
#        grand_total += new_value

datafile = get_2d_int(file2read)

part_01(data_list=datafile)
if stage_2:
    part_02(data_list=datafile)
