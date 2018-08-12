import sys


def input(input_file_path):
    with open(input_file_path, "r") as f:
        data = f.readlines()
    return data


def get_number(data):
    lst = data.split()
    m = int(lst[0])
    n = int(lst[1])
    p = int(lst[2])
    return m, n, p


def get_tower(data):
    tower = []
    for i in range(len(data)):
        tower.append([])
    for index, floor in enumerate(data):
        for room in floor.split():
            tower[index].append(int(room))
    return tower


def get_room_position(row, col):
    return row * n + col


def get_map(tower):
    map = []
    for i in range(m*n):
        map.append([sys.maxsize] * m * n)
    for r_index, floor in enumerate(tower):
        for c_index, room in enumerate(floor):
            if r_index < len(tower) - 1:
                x = get_room_position(r_index, c_index)
                y = get_room_position(r_index + 1, c_index)
                map[x][y] = tower[r_index + 1][c_index]
                map[y][x] = tower[r_index][c_index]
            if c_index < len(floor) - 1:
                x = get_room_position(r_index, c_index)
                y = get_room_position(r_index, c_index + 1)
                map[x][y] = tower[r_index][c_index + 1]
                map[y][x] = tower[r_index][c_index]
    return map


def init_trace():
    trace = []
    for i in range(n * m):
        trace.append([-1] * n * m)
    for i in range(n * m):
        for j in range(n * m):
            if i != j:
                trace[i][j] = j
    return trace


def ford_bellman(map):
    n = len(map)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if map[i][k] + map[k][j] < map[i][j]:
                    map[i][j] = map[i][k] + map[k][j]
                    trace[i][j] = k
    return map


def get_result(map):
    finish_room = get_room_position(len(tower) - 1, p)
    min = sys.maxsize
    for i in range(n):
        for j in range(n * (m - 1), n * m - 1):
            if j != finish_room:
                if map[i][j] + tower[0][i] < min:
                    min = map[i][j] + tower[0][i]
                    start_room = i
                    end_room = j
    path = [start_room]
    node = start_room
    while node != end_room:
        path.append(trace[node][end_room])
        node = trace[node][end_room]
    min += tower[len(tower) - 1][p]
    output_lines = [str(min) + " " + str(len(path) + 1)]
    for room in path:
        floor = int(room/n)
        index = room % n
        output_lines.append(str(floor) + " " + str(index))
    output_lines.append(str(len(tower) - 1) + " " + str(p))
    return output_lines


def output(output_file_path, data):
    with open(output_file_path, "w") as f:
        for line in data:
            f.write(line + "\n")


data = input("SIGN.INP")
m, n, p = get_number(data[0])
tower = get_tower(data[1:])
trace = init_trace()
map = get_map(tower)
map = ford_bellman(map)
output_lines = get_result(map)
output("SIGN.OUT", output_lines)
