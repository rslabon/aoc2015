import heapq
from collections import deque
from functools import reduce

weights = [1, 2, 3, 4, 5, 7, 8, 9, 10, 11]

weights = [
    1,
    2,
    3,
    5,
    7,
    13,
    17,
    19,
    23,
    29,
    31,
    37,
    41,
    43,
    53,
    59,
    61,
    67,
    71,
    73,
    79,
    83,
    89,
    97,
    101,
    103,
    107,
    109,
    113,
]


def qe(products):
    return reduce(lambda x, y: x * y, products)


def find_smallest_qe(weights, value):
    q = []
    heapq.heapify(q)
    heapq.heappush(q, (0, set(), value))
    seen = set()
    result = []

    while q:
        _, current_weights, current_value = heapq.heappop(q)
        if tuple(current_weights) in seen:
            continue
        seen.add(tuple(current_weights))
        if current_value == 0:
            return qe(current_weights)

        for i, weight in enumerate(weights):
            if weight not in current_weights and current_value - weight >= 0:
                heapq.heappush(q, (current_value - weight, current_weights | {weight}, current_value - weight))

    return result


def find_smallest_qe2(weights, value):
    q = deque()
    q.append((set(), value))
    seen = set()
    result = []

    while q:
        current_weights, current_value = q.popleft()
        if tuple(current_weights) in seen:
            continue
        seen.add(tuple(current_weights))
        if current_value == 0:
            return qe(current_weights)

        for i, weight in enumerate(weights):
            if weight not in current_weights and current_value - weight >= 0:
                q.append((current_weights | {weight}, current_value - weight))

    return result


def part1():
    total_weight = sum(weights)
    single_group = total_weight // 3
    print(find_smallest_qe(weights, single_group))


def part2():
    total_weight = sum(weights)
    single_group = total_weight // 4
    print(find_smallest_qe2(weights, single_group))


part1()
part2()
