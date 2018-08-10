n = 0
m = 0
map = []


def input(input_file_path):
    global n, m, map
    with open(input_file_path, "r") as f:
        data = f.readlines()
        n = int(data[0].split()[0])
        for i in range(n):
            map.append([False] * n)
        m = int(data[0].split()[1])
        for line in data[1:]:
            x = int(line.split()[0])
            y = int(line.split()[1])
            map[x][y] = True
            for line in map:
                print(line)
            print("")


def process_and_output(output_file_path):
    global n, map
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if map[i][k] and map[k][j]:
                    map[i][j] = True
    for line in map:
        print(line)
    checked = [False] * n
    result = []
    for i in range(n):
        if not checked[i]:
            checked[i] = True
            area = [i]
            for j in range(n):
                if not checked[j]:
                    for node in area:
                        if map[node][j] and map[j][node]:
                            checked[j] = True
                            area.append(j)
                            break
            result.append(area)
    output_lines = [len(result)]
    for area in result:
        output_lines.append(area)
    with open(output_file_path, "w") as f:
        for line in output_lines:
            f.write(str(line) + "\n")


input("GRAPH.INP")
process_and_output("GRAPH.OUT")
