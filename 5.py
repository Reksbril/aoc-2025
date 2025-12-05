from base import Solution


class SolutionImpl(Solution):
    def parse(self, file_data):
        ranges = []
        checks = []
        i = 0
        while True:
            line = file_data[i].strip()
            if len(line) == 0:
                break
            line_range = line.split("-")
            ranges.append((int(line_range[0]), int(line_range[1])))
            i += 1

        i += 1
        checks = [int(line) for line in file_data[i:]]
        return ranges, checks


def solution_1(data):
    result = 0
    ranges, ids = data
    for id in ids:
        for r in ranges:
            if id >= r[0] and id <= r[1]:
                result += 1
                break
    return result


def solution_2(data):
    sorted_ranges = []
    ranges, _ = data

    for r in ranges:
        idx = 0

        # look for first sorted range that we potentially overlap with
        while True:
            sr = sorted_ranges[idx]
            if r[0] <= sr[1]:


solution_idx = 5
full_input = f"full_{solution_idx}"
short_input = f"short_{solution_idx}"
short_result_1 = 3
short_result_2 = -1

SolutionImpl(full_input, short_input, short_result_1).run(solution_1)
SolutionImpl(full_input, short_input, short_result_2).run(solution_2)
