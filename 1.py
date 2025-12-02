from base import Solution


class SolutionImpl(Solution):
    def parse(self, file_data):
        return [line.strip() for line in file_data]


def solution_1(data):
    current = 50
    total_zeros = 0
    for rotation in data:
        sign = 1
        if rotation[0] == "L":
            sign = -1
        rotation_num = int(rotation[1:])

        current = (current + sign * rotation_num) % 100

        if current == 0:
            total_zeros += 1
    return total_zeros


def solution_2(data):
    current = 50
    total_zeros = 0
    for rotation in data:
        sign = 1
        if rotation[0] == "L":
            sign = -1
        rotation_num = int(rotation[1:])

        current = current + sign * rotation_num

        if current >= 100:
            while current >= 100:
                current -= 100
                total_zeros += 1
            continue

        if current < 0:
            if current == sign * rotation_num:
                total_zeros -= 1
            while current < 0:
                current += 100
                total_zeros += 1

        if current == 0:
            total_zeros += 1

    return total_zeros


solution_idx = 1
full_input = f"full_{solution_idx}"
short_input = f"short_{solution_idx}"
short_result_1 = 3
short_result_2 = 6

SolutionImpl(full_input, short_input, short_result_1).run(solution_1)
SolutionImpl(full_input, short_input, short_result_2).run(solution_2)
