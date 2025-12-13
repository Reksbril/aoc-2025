from base import Solution


class SolutionImpl(Solution):
    def parse(self, file_data):
        return [(int(line.strip().split(",")[0]), int(line.strip().split(",")[1])) for line in file_data]


def solution_1(data):
    max_size = 0
    for idx, p1 in enumerate(data):
        for p2 in data[idx + 1:]:
            size = (abs(p1[0] - p2[0]) + 1) * (abs(p1[1] - p2[1]) + 1)
            if size > max_size:
                max_size = size

    return max_size


def solution_2(data):
    return 0


solution_idx = 9
full_input = f"full_{solution_idx}"
short_input = f"short_{solution_idx}"
short_result_1 = 50
short_result_2 = -1

SolutionImpl(full_input, short_input, short_result_1).run(solution_1)
SolutionImpl(full_input, short_input, short_result_2).run(solution_2)
