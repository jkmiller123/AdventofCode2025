
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

def get_3d_map(a_file):
    # this will create a list of lists.  not exactly what I was looking for.
    # prefer to make an array with definite co-ordinates.
    # Sample data
    # 162,817,812
    # 57,618,57
    # 906,360,560
    # 592,479,940
    # Returns :
    # {817, 162, 812}
    # {57, 618, 57}
    # {360, 906, 560}

    with open(a_file,'r') as f:
        data2 = f.read().strip().splitlines()
    data3 = []
    for items in data2:
        newset = list(map(int,items.split(",")))
        data3.append(newset)
    return data3

def get_3d_set(a_file):
    # this will create a list of lists.  not exactly what I was looking for.
    # prefer to make an array with definite co-ordinates.
    # Sample data
    # 162,817,812
    # 57,618,57
    # 906,360,560
    # 592,479,940
    # Returns :
    # {817, 162, 812}
    # {57, 618, 57}
    # {360, 906, 560}

    with open(a_file,'r') as f:
        data2 = f.read().strip().splitlines()
    data3 = []
    for items in data2:
        newset = tuple(map(int,items.split(",")))
        data3.append(newset)
    return data3
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


def create_base_files(aocDay):
    # Simple little function that will create the 3 standard files along with the standard heading
    # in the python file

    samplefile = 'Data/Day' + aocDay + '_Sample.txt'
    datafile = 'Data/Day' + aocDay + '_01.txt'
    pythonfile = 'Day' + aocDay + '.py'

    with open(samplefile, "w") as f:
        f.write("")
        f.close()

    with open(datafile, "w") as f:
        f.write("")
        f.close()

    with open(pythonfile, "w") as p:
        p.write("testing = True # used for debugging messages and to pick the file\n")
        p.write("stage_2 = False  # used for more complex coding changes\n")
        p.write("aocDay = '"+aocDay+"'\n")
        p.write("file2read = 'Data/Day' + aocDay + '_Sample.txt' if testing else 'Data/Day' + aocDay + '_01.txt'\n")
        p.write("\n")
        p.write("from read_files import get_1line\n")
        p.close()
    return