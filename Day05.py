testing = False   # used for debugging messages and to pick the file
stage_2 = False    # used for more complex coding changes
aocDay = '05'
file2read = 'Data/Day'+aocDay+'_Sample.txt' if testing else 'Data/Day'+aocDay+'_01.txt'

from read_files import get_2parts

db = get_2parts(file2read)
ingredient_db = db[0]
spoiled = db[1]
ingredient_ranges = []
# ingredient_list = []
for items in ingredient_db:
    low_range, highrange = map(int,items.split("-"))
    ingredient_ranges.append([low_range, highrange])
    # for b in range(low_range,highrange):
    #     ingredient_list.append(b)
    # ingredient_list.append(highrange)

# ingredient_set = set(ingredient_list)
fresh_set = set()
ingredient_set = set()

for item in spoiled:
    for [low_range,highrange] in ingredient_ranges:
        if int(item) >= low_range and int(item) <= highrange:
            fresh_set.add(int(item))
            ing_range = str(low_range) + '-' + str(highrange)
            ingredient_set.add(ing_range)


ing_dict = {}
ing_range_key = 0
for item in ingredient_set:
    range_found = False
    low_range, high_range = map(int,item.split('-'))
    for item2 in ing_dict.keys():
        if low_range <= ing_dict[item2][0] and high_range >= ing_dict[item2][0] :
            ing_dict[item2][0] = low_range
            range_found = True
            if (low_range == 81726117115089):
                print(f'a {high_range} {len(ing_dict)}  {range_found}')
        if high_range >= ing_dict[item2][1] and low_range <= ing_dict[item2][1] :
            ing_dict[item2][1] = high_range
            range_found = True
            if (low_range == 81726117115089):
                print(f'b {high_range} {len(ing_dict)}  {range_found}')
    if (low_range == 81726117115089):
        print(f'c {high_range} {len(ing_dict)}  {range_found}')
    if range_found == False:
        ing_dict[ing_range_key] = [low_range, high_range]
        ing_range_key += 1

total_num_ing = 0
for item in ing_dict.keys():
    total_num_ing += (ing_dict[item][1]-ing_dict[item][0] + 1)
print(f'There are {len(fresh_set)} fresh ingredients ')
print(f'There are {total_num_ing}  ingredients ranges ')
for item in ing_dict.values():
     if (item[0] == 81726117115089):
         print(f'xxx {item[1]} {len(ing_dict)}  ')
     print(f'{item[0]} {item[1]}')

# Part 2
#  136 too low
# 354980328653069 too high
# 325,336,290,828,831 too low