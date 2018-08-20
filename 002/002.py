def input(input_file_path):
    with open(input_file_path, "r") as f:
        data = f.readlines()
    map = []
    for index, line in enumerate(data):
        map.append([])
        for item in line.split():
            map[index].append(int(item))
    return map


def isPrime(i):
    for j in range(2, i):
        if i % j == 0:
            return False
    return True


def have_duplicate(arr):
    for item in arr:
        if arr.count(item) >= 2:
            return True
    return False


def process(arr):
    for i in range(2, len(arr)):
        for number in prime:
            if have_duplicate(arr[i]):
                if number not in arr[i] and i + number < 51:
                    if len(arr[i]) + 1 > len(arr[i + number]):
                        arr[i + number] = arr[i] + [number]
            else:
                if i + number < 51:
                    if len(arr[i]) + 1 > len(arr[i + number]):
                        arr[i + number] = arr[i] + [number]
    return arr


def get_result(board):
    for r_ind, line in enumerate(board):
        for c_ind, item in enumerate(line):
            board[r_ind][c_ind] = len(arr[board[r_ind][c_ind]])
    return board


def output(output_file_path, board):
    with open(output_file_path, "w") as f:
        for line in board:
            f.write(str(line) + "\n")


prime = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47)
board = input("INP.B1")
arr = [[]] * 51
for number in range(2, 51):
    if isPrime(number):
        arr[number] = [number]
arr = process(arr)
board = get_result(board)
output("OUT.B1", board)
