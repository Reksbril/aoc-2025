from base import Solution

from dataclasses import dataclass
from typing import List

import math

@dataclass
class Point:
    x: int
    y: int
    z: int


class Node:
    def __init__(self, point: Point, idx: int):
        self.point = point
        self.idx = idx
        self.neighbours: List[Node] = []

    def update_idx(self, new_idx: int):
        if self.idx == new_idx:
            return
        
        self.idx = new_idx

        for neighbour in self.neighbours:
            neighbour.update_idx(new_idx)
    
    def __str__(self):
        return f"Node(idx={self.idx}, point=({self.point.x}, {self.point.y}, {self.point.z}))"
    
    def __repr__(self):
        return self.__str__()

def distance(p1: Point, p2: Point):
    return (p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2 + (p1.z - p2.z) ** 2


class SolutionImpl(Solution):
    def parse(self, file_data):
        result = []
        for line in file_data:
            line_split = line.strip().split(",")
            result.append(Point(int(line_split[0]), int(line_split[1]), int(line_split[2])))

        return result


def solution_1(data):
    distances: List[tuple[int, Node, Node]] = []
    nodes = [Node(point, idx) for idx, point in enumerate(data)]
    circuit_sizes = [1 for _ in range(len(nodes))]
    for idx, n1 in enumerate(nodes):
        for n2 in nodes[idx + 1:]:
            distances.append((distance(n1.point, n2.point), n1, n2))

    distances.sort(key=lambda x: x[0])

    n_cables = 10 if len(data) < 100 else 1000

    for d in distances[:n_cables]:
        if d[1].idx == d[2].idx:
            continue

        new_idx = min(d[1].idx, d[2].idx)
        old_idx = max(d[1].idx, d[2].idx)
        d[1].update_idx(new_idx)
        d[2].update_idx(new_idx)

        d[1].neighbours.append(d[2])
        d[2].neighbours.append(d[1])

        circuit_sizes[new_idx] = circuit_sizes[new_idx] + circuit_sizes[old_idx]
        circuit_sizes[old_idx] = 0

        n_cables -= 1
    return math.prod(sorted(circuit_sizes, reverse=True)[:3])
    

def solution_2(data):
    distances: List[tuple[int, Node, Node]] = []
    nodes = [Node(point, idx) for idx, point in enumerate(data)]
    circuit_sizes = [1 for _ in range(len(nodes))]
    for idx, n1 in enumerate(nodes):
        for n2 in nodes[idx + 1:]:
            distances.append((distance(n1.point, n2.point), n1, n2))

    distances.sort(key=lambda x: x[0])

    for d in distances:
        if d[1].idx == d[2].idx:
            continue

        new_idx = min(d[1].idx, d[2].idx)
        old_idx = max(d[1].idx, d[2].idx)
        d[1].update_idx(new_idx)
        d[2].update_idx(new_idx)

        d[1].neighbours.append(d[2])
        d[2].neighbours.append(d[1])

        circuit_sizes[new_idx] = circuit_sizes[new_idx] + circuit_sizes[old_idx]
        circuit_sizes[old_idx] = 0

        if circuit_sizes[new_idx] == len(nodes):
            return d[1].point.x * d[2].point.x


solution_idx = 8
full_input = f"full_{solution_idx}"
short_input = f"short_{solution_idx}"
short_result_1 = 40
short_result_2 = 25272

SolutionImpl(full_input, short_input, short_result_1).run(solution_1)
SolutionImpl(full_input, short_input, short_result_2).run(solution_2)
