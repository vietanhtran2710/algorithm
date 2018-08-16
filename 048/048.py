def input(input_file_path):
    with open(input_file_path, "r") as f:
        data = f.readlines()
    map = []
    for i in range(len(data)):
        map.append([])
    for index, line in enumerate(data):
        lst = line.split()
        for item in lst:
            map[index].append(int(item))
    return map


def init_map(map, value):
    lst = []
    for i in range(len(map)):
        lst.append([])
    for index, line in enumerate(map):
        for item in line:
            lst[index].append(value)
    return lst


def go(row, col, num):
    global count, room, checked
    checked[row][col] = True
    room[row][col] = num
    count += 1
    value = map[row][col]
    for i in range(4):
        if value & (1 << i) != (1 << i):
            if i == 0 and col > 0:
                if not checked[row][col - 1]:
                    go(row, col - 1, num)
            if i == 1 and row > 0:
                if not checked[row - 1][col]:
                    go(row - 1, col, num)
            if i == 2 and col < len(map[0]) - 1:
                if not checked[row][col + 1]:
                    go(row, col + 1, num)
            if i == 3 and row < len(map) - 1:
                if not checked[row + 1][col]:
                    go(row + 1, col, num)


def get_result(room, size):
    output_lines = [len(size)]
    max = -1
    for s in size:
        if s > max:
            max = s
    output_lines.append(max)
    max = -1
    direction = ""
    dir = {0: "W", 1: "N", 2: "E", 3: "S"}
    for row_index, line in enumerate(room):
        for col_index, block in enumerate(line):
            for i in range(4):
                if map[row_index][col_index] & (1 << i) == (1 << i):
                    if i == 0 and col_index > 0:
                        room_block = room[row_index][col_index - 1]
                        if room_block != block:
                            if max < size[block] + size[room_block]:
                                max = size[block] + size[room_block]
                                max_col = col_index
                                max_row = row_index
                                direction = dir[i]
                    if i == 1 and row_index > 0:
                        room_block = room[row_index - 1][col_index]
                        if room_block != block:
                            if max < size[block] + size[room_block]:
                                max = size[block] + size[room_block]
                                max_col = col_index
                                max_row = row_index
                                direction = dir[i]
                    if i == 2 and col_index < len(map[0]) - 1:
                        room_block = room[row_index][col_index + 1]
                        if room_block != block:
                            if max < size[block] + size[room_block]:
                                max = size[block] + size[room_block]
                                max_col = col_index
                                max_row = row_index
                                direction = dir[i]
                    if i == 3 and row_index < len(map) - 1:
                        room_block = room[row_index + 1][col_index]
                        if room_block != block:
                            if max < size[block] + size[room_block]:
                                max = size[block] + size[room_block]
                                max_col = col_index
                                max_row = row_index
                                direction = dir[i]
    output_lines.append([max_row, max_col, direction])
    output_lines.append(max)
    return output_lines


def output(output_file_path, data):
    with open(output_file_path, "w") as f:
        for line in data:
            f.write(str(line) + "\n")


map = input("DWALL.INP")
count = 0
checked = init_map(map, False)
room = init_map(map, 0)
size = []
for row_index, line in enumerate(map):
    for col_index, block in enumerate(line):
        if not checked[row_index][col_index]:
            count = 0
            go(row_index, col_index, len(size))
            size.append(count)
output_lines = get_result(room, size)
output("DWALL.OUT", output_lines)
