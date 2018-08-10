import sys


def input(input_file_path):
    with open(input_file_path, "r") as f:
        map = []
        data = f.readlines()
        n = int(data[0].split()[0])
        for i in range(n):
            map.append([1000] * n)
        start_end_nodes = data[1].split()
        ha = int(start_end_nodes[0])
        sa = int(start_end_nodes[1])
        hb = int(start_end_nodes[2])
        sb = int(start_end_nodes[3])
        for line in data[2:]:
            x = int(line.split()[0])
            y = int(line.split()[1])
            time = int(line.split()[2])
            map[x][y] = time
    return n, ha, sa, hb, sb, map


def init_trace_map():
    trace = []
    for i in range(n):
        trace.append([-1] * n)
    for i in range(n):
        for j in range(n):
            if i != j:
                trace[i][j] = i
    return trace


def process_map(trace, map):
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if map[i][k] + map[k][j] < map[i][j]:
                    map[i][j] = map[i][k] + map[k][j]
                    trace[i][j] = k
    return trace, map


def get_node(map):
    for row_index, row in enumerate(map):
        for col_index, cell in enumerate(row):
            if map[ha][col_index] + map[col_index][sa] == map[ha][sa]:
                if map[hb][col_index] + map[col_index][sb] == map[hb][sb]:
                    if map[ha][col_index] == map[hb][col_index]:
                        return col_index
    return -1


def get_path(start, end):
    path = [end]
    node = end
    while node != start:
        path.append(trace[start][node])
        node = trace[start][node]
    return path[::-1]


def get_output_content(node):
    if node == -1:
        output_lines = ["NO"]
    else:
        output_lines = ["YES"]
        output_lines.append(map[ha][node] + map[node][sa])
        path = set(get_path(ha, node) + get_path(node, sa))
        output_lines.append(path)
        output_lines.append(map[hb][node] + map[node][sb])
        path = set(get_path(hb, node) + get_path(node, sb))
        output_lines.append(path)
        output_lines.append(node)
        output_lines.append(map[ha][node])
    return output_lines


def output(output_file_path, output_content):
    with open(output_file_path, "w") as f:
        for line in output_content:
            f.write(str(line) + "\n")


n, ha, sa, hb, sb, map = input("FRIEND.INP")
trace = init_trace_map()
trace, map = process_map(trace, map)
node = get_node(map)
output_lines = get_output_content(node)
output("FRIEND.OUT", output_lines)
