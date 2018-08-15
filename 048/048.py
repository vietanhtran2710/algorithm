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


def get_room(map):
    global count

    def init_map(map, value):
        lst = []
        for i in range(len(map)):
            lst.append([])
        for index, line in enumerate(map):
            for item in line:
                lst[index].append(value)
        return lst

    def go(row, col, num, checked):
        global count
        checked[row][col] = True
        room[row][col] = num
        count += 1
        value = map[row][col]
        for i in range(4):
            if value & (1 << i) == (1 << i):
                if i == 0 and col > 0:
                    if not checked[row][col]:
                        go(row, col - 1, num, checked)
                if i == 1 and row > 0:
                    if not checked[row][col]:
                        go(row - 1, col, num, checked)
                if i == 2 and col < len(map[0]) - 1:
                    if not checked[row][col]:
                        go(row, col + 1, num, checked)
                if i == 3 and row < len(map) - 1:
                    if not checked[row][col]:
                        go(row + 1, col, num, checked)
        return checked


    checked = init_map(map, False)
    room = init_map(map, 0)
    size = []
    for row_index, line in enumerate(map):
        for col_index, block in enumerate(line):
            if not checked[row_index][col_index]:
                count = 0
                checked = go(row_index, col_index, len(size), checked)
                size.append(count)
    return room, size


def get_result(room, size):
    output_lines = [len(size)]
    max = -1
    for size in size:
        if size > max:
            max = size
    output_lines.append(max)
    max = -1
    direction = ""
    dir = {0: "W", 1: "N", 2: "E", 3: "S"}
    for row_index, line in enumerate(room):
        for col_index, block in enumerate(line):
            for i in range(4):
                if block & (1 << i) == (1 << i):
                    if i == 0 and col_index > 0:
                        room_block = room[row_index][col_index - 1]
                        new_size = size[block] + room_block
                        if max < new_size:
                            max = new_size
                            max_col = col_index
                            max_row = row_index
                            direction = dir[i]
                    if i == 1 and row_index > 0:
                        room_block = room[row_index - 1][col_index]
                        new_size = size[block] + room_block
                        if max < new_size:
                            max = new_size
                            max_col = col_index
                            max_row = row_index
                            direction = dir[i]
                    if i == 2 and col_index < len(map[0]) - 1:
                        room_block = room[row_index][col_index + 1]
                        new_size = size[block] + room_block
                        if max < new_size:
                            max = new_size
                            max_col = col_index
                            max_row = row_index
                            direction = dir[i]
                    if i == 3 and row_index < len(map) - 1:
                        room_block = room[row_index + 1][col_index]
                        new_size = size[block] + room_block
                        if max < new_size:
                            max = new_size
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
room, size = get_room(map)
print(size)
for line in room:
    print(line)
output_lines = get_result(room, size)
output("DWALLL.OUT", output_lines)
