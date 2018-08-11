import sys


def input(input_file_path):
    with open(input_file_path, "r") as f:
        data = f.readlines()
    return data


def get_map(data):
    map = []
    for i in range(n):
        map.append([False] * n)
    for line in data:
        x = int(line.split()[0])
        y = int(line.split()[1])
        map[x][y] = True
    return map


def ford_bellman(map):
    n = len(map)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if map[i][k] and map[k][j]:
                    map[i][j] = True
    return map


def get_result(map):
    lst = []
    for i in range(n):
        area = [i]
        for j in range(n):
            if (i != j) and (map[i][j]):
                area.append(j)
        lst.append(area)
    min = sys.maxsize
    for area in lst:
        if len(area) < min:
            result = area
            min = len(area)
    return [min, result]


def output(output_file_path, data):
    with open(output_file_path, "w") as f:
        for line in data:
            f.write(str(line) + "\n")


data = input("FLOWERS.INP")
n = int(data[0])
map = get_map(data[1:])
map = ford_bellman(map)
output_lines = get_result(map)
output("FLOWERS.OUT", output_lines)
