def input(input_file_path):
    with open(input_file_path, "r") as f:
        data = f.readlines()
        map = [[0] * (len(data[0].split()) + 2)]
        for line in data:
            lst = line.split()
            append_lst = [0]
            for item in lst:
                append_lst.append(int(item))
            append_lst.append(0)
            map.append(append_lst)
        map.append([0] * (len(data[0].split()) + 2))
    return map


def get_diff(row, col, map):
    horiz_dir = [-1, 0, 1, 0]
    verti_dir = [0, 1, 0, -1]
    height = map[row][col]
    diff = 0
    for i in range(4):
        value = map[row + horiz_dir[i]][col + verti_dir[i]]
        if value < height:
            diff += height - value
    return diff


def output(output_file_path, result):
    with open(output_file_path, "w") as f:
        f.write(str(result))


map = input("PAINT.INP")
count = 0
for i in range(1, len(map) - 1):
    for j in range(1, len(map[0]) - 1):
        count += 1 + get_diff(i, j, map)
output("PAINT.OUT", count)
