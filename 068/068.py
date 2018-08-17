import sys


def input(input_file_path):
    with open(input_file_path, "r") as f:
        data = f.readlines()
    return data


def init_map(number):
    map = []
    for i in range(number):
        map.append([sys.maxsize] * number)
    return map


def get_map(map, data):
    for line in data:
        lst = line.split()
        x = int(lst[0])
        y = int(lst[1])
        cost = int(lst[2])
        map[x][y] = cost
        map[y][x] = cost
    return map


def go(index):
    global min, result_tour
    if index >= 3:
        if total_cost + map[tour[index - 1]][tour[0]] < min:
            min = total_cost + map[tour[index - 1]][tour[0]]
            result_tour = []
            for i in range(index):
                result_tour.append(tour[i])
    for i in range(n):
        if not checked[i]:
            tour[index] = i
            checked[i] = True
            add_cost =  map[tour[index - 1]][i]
            total_cost += add_cost
            go(index + 1)
            checked[i] = False
            total_cost -= add_cost


def get_result(result, min):
    if not result:
        return [0]
    else:
        return output_lines = [1, min, len(result), result]


def output(output_file_path, content):
    with open(output_file_path, "w") as f:
        for line in content:
            f.write(str(line) + "\n")


data = input("TOUR.INP")
n = int(data[0])
map = init_map(n)
map = get_map(map, data[1:])
result_tour = []
for i in range(n):
    tour = [i] + [0] * (n - 1)
    checked = [True] + [False] * (n - 1)
    total_cost = 0
    min = sys.maxsize
    go(1)
output_lines = get_result(result_tour, min)
output("TOUR.OUT",output_lines)
