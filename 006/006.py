def input(input_file_path):
    with open(input_file_path, "r") as f:
        return int(f.read())


def is_prime(value):
    for i in range(2, value - 1):
        if value % i == 0:
            return False
    return True


def go(index):
    if index == 2 * n:
        if is_prime(solution[-1] + 1):
            result.append(list(solution))
    else:
        for i in range(2, 2 * n + 1):
            if (not used[i - 1]) and (is_prime(i + solution[index - 1])):
                used[i - 1] = True
                solution[index] = i
                go(index + 1)
                used[i - 1] = False
                solution[index] = 0


def output(output_file_path, data):
    with open(output_file_path, "w") as f:
        f.write(str(len(data)) + "\n")
        for line in data:
            f.write(str(line) + "\n")


n = input("CIRCLE.INP")
solution = [1] + [0] * (2 * n - 1)
used = [True] + [False] * (2 * n - 1)
result = []
go(1)
output("CIRCLE.OUT", result)
