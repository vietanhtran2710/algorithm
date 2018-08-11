import sys


def input(input_file_path):
    with open(input_file_path, "r") as f:
        data = f.readlines()
    return data


def get_maze(data):
    maze = []
    for i in range(len(data)):
        maze.append([])
    for index, row in enumerate(data):
        for cell in row:
            maze[index].append(cell)
    return maze


def get_map_pos(row, col, length):
    return row * length + col


def get_map(maze):
    map = []
    for i in range(len(maze) * len(maze[0])):
        map.append([sys.maxsize] * len(maze) * len(maze[0]))
    for row_index, row in enumerate(maze):
        for col_index, cell in enumerate(row):
            if cell == ".":
                if row_index < len(maze) - 1:
                    if maze[row_index + 1][col_index] == ".":
                        x = get_map_pos(row_index, col_index, len(row))
                        y = get_map_pos(row_index + 1, col_index, len(row))
                        map[x][y] = 1
                if col_index < len(row) - 1:
                    if maze[row_index][col_index + 1] == ".":
                        x = get_map_pos(row_index, col_index, len(row))
                        y = get_map_pos(row_index, col_index + 1, len(row))
                        map[x][y] = 1
    return map


def ford_bellman(map):
    n = len(map)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if map[i][k] + map[k][j] < map[i][j]:
                    map[i][j] = map[i][k] + map[k][j]
    return map


def output(output_file_path, map):
    max = 0
    for i in range(len(map)):
        for j in range(len(map)):
            if map[i][j] != sys.maxsize:
                if map[i][j] > max:
                    max = map[i][j]
    with open(output_file_path, "w") as f:
        f.write(str(max))


data = input("LABYR.INP")
maze = get_maze(data)
map = get_map(maze)
map = ford_bellman(map)
output("LABYR.OUT",map)
