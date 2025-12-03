
testing = True   # used for debugging messages and to pick the file
stage_2 = True    # used for more complex coding changes
aocDay = '02'
file2read = 'Data/Day'+aocDay+'_Sample.txt' if testing else 'Data/Day'+aocDay+'_01.txt'
pos = 50   # The dial starts by pointing at 50
goalPos = 0  # the number of times the dial is left pointing at 0 after any rotation in the sequence
loopCounter = 0  # number of times past the position

from read_files import read_parse_comma

def part_01(data_list):
    print(f'In part 1')
    max_range = 0
    sum_invalids = 0
    for items in data_list:
        lowrange, highrange = map(int, items.split('-'))
        range = highrange - lowrange
        max_range = range if range > max_range else max_range
        while (lowrange <= highrange):
            lowstring = str(lowrange)
            sizeofLowrange = len(lowstring)
            if sizeofLowrange % 2 == 0:
                middle = sizeofLowrange // 2
                leftside = lowstring[:middle]
                rightside = lowstring[middle:]
                if leftside == rightside:
                    sum_invalids += lowrange
                    print(f'Found invalid {lowrange}')
            lowrange += 1
    print(f'Total Invalids {sum_invalids}')



def part_02(data_list):
    sum_invalids = 0
    for items in data_list:
        lowrange, highrange = map(int, items.split('-'))
        while (lowrange <= highrange):
            lowstring = str(lowrange)
            sizeofLowrange = len(lowstring) // 2
            for numdigits in range(sizeofLowrange):
                searchstring = lowstring[:numdigits + 1]
                if lowstring.count(searchstring) > 1 and len(lowstring) % lowstring.count(searchstring) == 0:
                    print(f'search string = {searchstring} for {lowstring}')
                numdigits += 1
            # if sizeofLowrange % 2 == 0:
            #     middle = sizeofLowrange // 2
            #     leftside = lowstring[:middle]
            #     rightside = lowstring[middle:]
            #     if leftside == rightside:
            #         sum_invalids += lowrange
            #         print(f'Found invalid {lowrange}')
            lowrange += 1
    print(f'Total Invalids {sum_invalids}')


data_list = read_parse_comma(a_file=file2read)

if stage_2:
    part_02(data_list=data_list)
else:
    part_01(data_list=data_list)
