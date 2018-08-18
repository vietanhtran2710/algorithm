def get_map(scientist):
    map = []
    for i in range(len(scientist)):
        map.append([False] * len(scientist))
    for index, person in enumerate(scientist):
        for j in range(index + 1, len(scientist)):
            for character in person:
                if character in scientist[j]:
                    map[index][j] = True
                    map[j][index] = True
    return map


def go(index):
    global result
    if index == len(scientist):
        result = path
    else:
        for i in range(len(scientist)):
            if index == len(scientist) - 1:
                connection = map[path[index - 1]][i] and map[i][0]
                if connection and not result and not checked[i]:
                    checked[i] = True
                    path[index] = i
                    go(index + 1)
                    checked[i] = False
            else:
                if map[path[index - 1]][i] and not result and not checked[i]:
                    checked[i] = True
                    path[index] = i
                    go(index + 1)
                    checked[i] = False


def output(output_file_path, result):
    with open(output_file_path, "w") as f:
        if result:
            for person_index in result:
                f.write(str(person_index) + "\n")
        else:
            f.write("NO SOLUTION")


with open("PARTY.INP", "r") as f:
    scientist = f.readlines()
for i in range(len(scientist)):
    scientist[i] = scientist[i].strip()
map = get_map(scientist)
result = []
path = [0] * len(scientist)
checked = [True] + [False] * (len(scientist) - 1)
go(1)
output("PARTY.OUT", result)
