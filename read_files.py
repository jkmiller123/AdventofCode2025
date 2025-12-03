
# file2read = "Day17/Sample.txt"
# abc = get_2d_char(file2read)
# a123 = get_2d_int(file2read)

def get_2d_lists(a_file):
    # this will create a list of lists.  not exactly what I was looking for.
    # prefer to make an array with definite co-ordinates.
   return [[x for x in line_in.split()] for line_in in open(a_file).readlines()]

def get_2d_char(a_file):
    # this will create a list of lists.  not exactly what I was looking for.
    # prefer to make an array with definite co-ordinates.
    with open(a_file, 'r') as f:
        data = f.read().splitlines()

    cols = len(data[0])
    rows = len(data)
    t_maze = [[0] * cols for i in range(rows)]  # define a blank maze

    for x in range(cols):
        for y in range(rows):
            t_maze[y][x] = data[y][x]
    return t_maze

def get_1d_array(afile):
    with open(afile, 'r') as f:
        data = f.read().splitlines()

    rows = len(data)
    t_data = [[0] for i in range(rows)]
    for x in range(rows):
        t_data[x] = int(data[x])

    return t_data

def get_1d_int(a_file):
    # this will create a list of lists.  not exactly what I was looking for.
    # prefer to make an array with definite co-ordinates.
    with open(a_file, 'r') as f:
        data = f.read().splitlines()

    data2 = data[0].split(' ')
    cols = len(data2)
    t_maze = [[0] for i in range(cols)]  # define a blank maze

    for x in range(cols):
        t_maze[x] = int(data2[x])
    return t_maze

def get_2d_int(a_file):
    # this will create a list of lists.  not exactly what I was looking for.
    # prefer to make an array with definite co-ordinates.
    with open(a_file, 'r') as f:
        data = f.read().splitlines()

    cols = len(data[0])
    rows = len(data)
    t_maze = [[0] * cols for i in range(rows)]  # define a blank maze

    for x in range(cols):
        for y in range(rows):
            t_maze[y][x] = int(data[y][x])
    return t_maze

def get_2parts(a_file):
    with open(a_file,'r') as f:
        data = f.read().strip().split("\n\n")

    return data[0].splitlines(), data[1].splitlines()

def get_multi_parts(a_file):
    with open(a_file) as f:
        ws = [[list(y) for y in blocks.split('\n')] for blocks in f.read().strip().split("\n\n")]

    return ws

def get_1part(a_file):
    with open(a_file,'r') as f:
        data = f.read().strip().split("\n\n")

    newdata = []
    for items in data:
        newdata.append(items.splitlines())
    return newdata

def get_1line(a_file):
    with open(a_file,'r') as f:
        data = f.read().strip().splitlines()
    return data
def get_dict(a_file):
    with open(a_file,'r') as f:
        data2 = f.read().strip().splitlines()
    data3 = data2[0].split(" ")
    data = {}
    for items in data3:
        data.update({items : 1})
    return data


def read_parse_colon(a_file):
    with open(a_file,'r') as f:
        data = f.read().strip().splitlines()

    value = []
    formula = []
    for items in data:
        avalue, aformula = items.split(":")
        value.append(avalue.strip())
        formula.append(aformula.strip())

    return value, formula
    

def read_parse_comma(a_file):
    with open(a_file,'r') as f:
        data = f.read().strip().split(',')
    return data
    