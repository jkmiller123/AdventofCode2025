
testing = False   # used for debugging messages and to pick the file
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

def find_factors(number: object) -> object:
    """
    Finds all factors of a given positive integer.
    Args:
        number: A positive integer.
    Returns:
        A list containing all factors of the input number.
    """
    factors = []
    for i in range(1, number + 1):
        if number % i == 0:
            factors.append(i)
    return factors

def part_02(data_list):
    sum_invalids = 0
    for items in data_list:
        lowrange, highrange = map(int, items.split('-'))
        list_of_invalids = set()   # need to create a list to remove duplicates, in sample data 22222 would be added to list 3 times. for 222220-222224
        while (lowrange <= highrange):
            lowstring = str(lowrange)
            # split into factors to list the repeatable groups 
            factorsList = find_factors(len(lowstring))
            for factors in factorsList:
                part = lowstring[0:factors]
                num_parts = lowstring.count(part)
                num_parts_total = int(len(lowstring) / factors)
                if num_parts == num_parts_total and num_parts_total > 1:
                    list_of_invalids.add(part*num_parts_total)
                   # print(f'Found an invalid {part*num_parts_total} of {lowstring}')
            lowrange += 1
        for invalids in list_of_invalids:
            sum_invalids += int(invalids)

        print(f'List of invalids {list_of_invalids} for {items}')
    print(f'Total of invalids {sum_invalids}')

    4174379265
    4174823709


data_list = read_parse_comma(a_file=file2read)

if stage_2:
    part_02(data_list=data_list)
else:
    part_01(data_list=data_list)
