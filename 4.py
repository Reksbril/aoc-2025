from base import Solution


class SolutionImpl(Solution):
    def parse(self, file_data):
        return [[c for c in line.strip()] for line in file_data]

def neighbours(data, i, j):
    for k in [-1, 0, 1]:
        for l in [-1, 0, 1]:
            if k == 0 and l == 0:
                continue
            if i + k >= 0 and i + k < len(data) and j + l >= 0 and j + l < len(data[0]):
                yield (i + k, j + l)

def count_rolls(data, i, j):
    count = 0
    for ii, jj in neighbours(data, i, j):
        if data[ii][jj] == "@":
            count += 1

    return count

def iterate_once(data, remove=False):
    result = 0
    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j] != "@":
                continue
            if count_rolls(data, i, j) < 4:
                result += 1
                if remove:
                    data[i][j] = "x"
    return result


def solution_1(data):
    return iterate_once(data)

def solution_2(data):
    result = 0
    while True:
        iter_result = iterate_once(data, True)
        result += iter_result
        if iter_result == 0:
            break
    return result


solution_idx = 4
full_input = f"full_{solution_idx}"
short_input = f"short_{solution_idx}"
short_result_1 = 13
short_result_2 = 43

SolutionImpl(full_input, short_input, short_result_1).run(solution_1)
SolutionImpl(full_input, short_input, short_result_2).run(solution_2)
