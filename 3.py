from base import Solution


class SolutionImpl(Solution):
    def parse(self, file_data):
        return [[int(number) for number in line.strip()] for line in file_data]


def get_top_number_idx(line, left, right):
    best_idx = right
    while right >= left:
        if line[right] >= line[best_idx]:
            best_idx = right
        right -= 1

    return best_idx


def get_best_number(line, n_digits):
    result = 0
    left = 0
    right = len(line) - n_digits
    while n_digits > 0:
        next_digit_idx = get_top_number_idx(line, left, right)
        result *= 10
        result += line[next_digit_idx]
        left = next_digit_idx + 1
        right += 1
        n_digits -= 1

    return result


def solution_1(data):
    return sum([get_best_number(line, 2) for line in data])


def solution_2(data):
    return sum([get_best_number(line, 12) for line in data])


solution_idx = 3
full_input = f"full_{solution_idx}"
short_input = f"short_{solution_idx}"
short_result_1 = 357
short_result_2 = 3121910778619

SolutionImpl(full_input, short_input, short_result_1).run(solution_1)
SolutionImpl(full_input, short_input, short_result_2).run(solution_2)
