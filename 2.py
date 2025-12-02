from base import Solution


class SolutionImpl(Solution):
    def parse(self, file_data):
        intervals = file_data[0].split(",")
        split_intervals = [
            interval.split("-") for interval in intervals
        ]
        return [(int(interval[0]), int(interval[1])) for interval in split_intervals]


def sum_of_divisible_numbers(start: int, stop: int, divisor: int):
    divisible_start = (start // divisor) * divisor
    if divisible_start != start:
        divisible_start += divisor

    divisible_stop = (stop // divisor) * divisor

    if divisible_stop < divisible_start:
        return 0

    n = (divisible_stop - divisible_start) // divisor + 1

    return (divisible_start + divisible_stop) * n // 2


def get_intervals_overlap(start_1: int, stop_1: int, start_2: int, stop_2: int):
    if start_1 > stop_2 or start_2 > stop_1:
        return None

    endpoints = [start_1, stop_1, start_2, stop_2]
    endpoints.sort()
    return (endpoints[1], endpoints[2])


def sum_of_invalid_numbers_in_interval(start: int, stop: int):
    result = 0

    start_small = 10
    stop_small = 99
    divisor = 11

    while stop > start_small:
        overlap = get_intervals_overlap(start, stop, start_small, stop_small)
        if overlap is None:
            start_small *= 100
            stop_small = stop_small * 100 + 99
            divisor = (divisor - 1) * 10 + 1
            continue

        result += sum_of_divisible_numbers(overlap[0], overlap[1], divisor)

        start_small *= 100
        stop_small = stop_small * 100 + 99
        divisor = (divisor - 1) * 10 + 1
       
    return result


def solution_1(data):
    result = 0
    for (start, stop) in data:
        result += sum_of_invalid_numbers_in_interval(start, stop)

    return result

def sum_of_invalid_numbers_v2_in_interval(start, stop):



def solution_2(data):
    result = 0
    for (start, stop) in data:
        result += sum_of_invalid_numbers_in_interval(start, stop)

    return result


solution_idx = 2
full_input = f"full_{solution_idx}"
short_input = f"short_{solution_idx}"
short_result_1 = 1227775554
short_result_2 = -1

SolutionImpl(full_input, short_input, short_result_1).run(solution_1)
SolutionImpl(full_input, short_input, short_result_2).run(solution_2)
