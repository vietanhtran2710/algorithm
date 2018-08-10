import sys
import math


def get_input_data(input_file_path):
    with open(input_file_path, "r") as f:
        data = f.readlines()
    return data


def get_computer_number(data):
    return int(data[0].split()[0])


def get_position(data):
    computer_pos = []
    for line in data:
        x_pos = float(line.split()[0])
        y_pos = float(line.split()[1])
        computer_pos.append([x_pos, y_pos])
    return computer_pos


def distance(com1, com2):
    delta_x = abs(computer_pos[com1][0] - computer_pos[com2][0])
    delta_y = abs(computer_pos[com1][1] - computer_pos[com2][1])
    return math.sqrt(delta_x * delta_x + delta_y * delta_y)


def get_map(data):
    map = []
    for i in range(n):
        map.append([sys.maxsize] * n)
    for line in data:
        x = int(line.split()[0])
        y = int(line.split()[1])
        map[x][y] = distance(x, y)
    return map


def ford_bellman(map):
    n = len(map)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if map[i][k] + map[k][j] < map[i][j]:
                    map[i][j] = map[i][k] + map[k][j]
    return map


def get_integrate_area(map):
    n = len(map)
    lst = []
    checked = [False] * n
    for i in range(n):
        if not(checked[i]):
            checked[i] = True
            area = [i]
            for j in range(n):
                if map[i][j] != sys.maxsize:
                    checked[j] = True
                    area.append(j)
            lst.append(area)
    return lst


def get_connection_list(area_list):
    n = len(area_list)
    lst = []
    for i in range(n):
        for j in range(i + 1, n):
            min = sys.maxsize
            min_com_1 = -1
            min_com_2 = -2
            for com1 in area_list[i]:
                for com2 in area_list[j]:
                    if distance(com1, com2) < min:
                        min = distance(com1, com2)
                        min_com_1 = com1
                        min_com_2 = com2
            lst.append([min, min_com_1, min_com_2])
    return lst


def get_first_element(array):
    return array[0]


def output(output_file_path):
    output_lines = []
    connection.sort(key=get_first_element)
    total_length = 0
    for item in connection[:len(area_list) - 1]:
        total_length += item[0]
    output_lines.append(str(len(area_list) - 1) + " " + str(total_length))
    for item in connection[:len(area_list) - 1]:
        output_lines.append(str(item[1]) + " " + str(item[2]))
    with open(output_file_path, "w") as f:
        for line in output_lines:
            f.write(line + "\n")


data = get_input_data("NET.INP")
n = get_computer_number(data)
computer_pos = get_position(data[1:n + 1])
map = get_map(data[n + 1:])
map = ford_bellman(map)
area_list = get_integrate_area(map)
connection = get_connection_list(area_list)
output("NET.OUT")
