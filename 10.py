from base import Solution

from dataclasses import dataclass
from typing import List
from collections import deque

import re

@dataclass
class Data:
    num_lights: int
    lights_target_on: List[int]
    buttons: List[List[int]]
    joltage: List[int]


class SolutionImpl(Solution):
    def parse(self, file_data):
        result: List[Data] = []
        for line in file_data:
            match = re.match(r'^(?P<lights>\[.*\]) (?P<buttons>(\(\d+(,\d+)*\) )+)\{(?P<joltage>[\d, ]+)\}$', line.strip())
            lights_str = match.group("lights")[1:-1]
            lights_target_on = [idx for idx, c in enumerate(lights_str) if c == "#"]
            buttons_str = match.group("buttons").strip().split(" ")
            buttons = []
            for b_str in buttons_str:
                b_str_clean = b_str[1:-1]
                b_indices = [int(x) for x in b_str_clean.split(",")]
                buttons.append(b_indices)
            joltage_str = match.group("joltage").strip().split(",")
            joltage = [int(x) for x in joltage_str]
            result.append(Data(len(lights_str), lights_target_on, buttons, joltage))

        return result


def list_to_num(indices: List[int]) -> int:
    return sum([2 ** i for i in indices]) 

def solution_1(data):
    result = 0

    for line in data:
        lights_num = list_to_num(line.lights_target_on)
        buttons = [list_to_num(b) for b in line.buttons]
        distances = [0 for _ in range(2 ** line.num_lights)]

        queue = [(0, 0)]
        
        best_dist = -1

        while len(queue) > 0:
            idx, dist = queue.pop(0)

            if distances[idx] > 0:
                continue

            distances[idx] = dist

            if idx == lights_num:
                best_dist = dist

            for b in buttons:
                queue.append((idx ^ b, dist + 1))

        result += best_dist

    return result


        
   
def solution_2(data):
    result = 0

    for line in data:
        distances = {}
        dim = len(line.joltage)
        target = line.joltage
        buttons = line.buttons

        queue = deque()
        queue.append((tuple([0 for _ in range(dim)]), 0))
        
        best_dist = -1

        while len(queue) > 0:
            idx, dist = queue.popleft()

            if idx in distances:
                continue

            if any([idx[i] > target[i] for i in range(dim)]):
                continue

            distances[idx] = dist

            if all([idx[i] == target[i] for i in range(dim)]):
                best_dist = dist
                break

            for b in buttons:
                queue.append((tuple([idx[i] + 1 if i in b else idx[i] for i in range(dim)]), dist + 1))

        print("xd")
        result += best_dist

    return result


solution_idx = 10
full_input = f"full_{solution_idx}"
short_input = f"short_{solution_idx}"
short_result_1 = 7
short_result_2 = 33

SolutionImpl(full_input, short_input, short_result_1).run(solution_1)
SolutionImpl(full_input, short_input, short_result_2).run(solution_2)
