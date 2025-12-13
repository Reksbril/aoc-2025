from base import Solution

from collections import defaultdict

class SolutionImpl(Solution):
    def parse(self, file_data):
        data = {}
        for line in file_data:
            start, end = line.strip().split(": ")
            data[start] = end.split(" ")

        return data


def solution_1(data):
    n_paths = 0
    visited = set()

    def dfs(curr):
        nonlocal n_paths
        if curr == "out":
            n_paths += 1
            return
        
        for next in data[curr]:
            dfs(next)

    dfs("you")

    return n_paths



def count_paths(data, start, end, skip = None):
    n_paths = {}
    visited = set()

    def dfs(curr):
        nonlocal n_paths
        nonlocal visited

        if curr == skip:
            return 0

        if curr in visited:
            raise RuntimeError("did not expect a loop")

        if curr in n_paths:
            return n_paths[curr]

        if curr == end:
            return 1
        
        visited.add(curr)
        paths = 0

        for next in data[curr]:
            paths += dfs(next)

        visited.remove(curr)
        n_paths[curr] = paths

        return paths

    return dfs(start)


def solution_2(data):
    data["out"] = []

    fft_to_out = count_paths(data, "fft", "out", "dac")
    dac_to_out = count_paths(data, "dac", "out", "fft")

    svr_to_fft = count_paths(data, "svr", "fft", "dac")
    svr_to_dac = count_paths(data, "svr", "dac", "fft")

    fft_to_dac = count_paths(data, "fft", "dac")
    dac_to_fft = count_paths(data, "dac", "fft")

    return svr_to_fft * fft_to_dac * dac_to_out + svr_to_dac * dac_to_fft * fft_to_out


solution_idx = 11
full_input = f"full_{solution_idx}"
short_input = f"short_{solution_idx}"
short_result_1 = 5
short_result_2 = 2

# data for part 1 in data/short_11_part_1
# SolutionImpl(full_input, short_input, short_result_1).run(solution_1)
SolutionImpl(full_input, short_input, short_result_2).run(solution_2)
