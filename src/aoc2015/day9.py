import heapq
import re

lines = """
London to Dublin = 464
London to Belfast = 518
Dublin to Belfast = 141
""".strip().splitlines()

with open('../../resources/day9.txt', 'r') as f:
    lines = f.read().strip().splitlines()

nodes = dict()

for line in lines:
    start, end, distance = re.findall(r"(\w+) to (\w+) = (\d+)", line)[0]
    distance = int(distance)
    nodes[start] = nodes.get(start, set())
    nodes[start].add((end, distance))

    nodes[end] = nodes.get(end, set())
    nodes[end].add((start, distance))


def shortest_path(source):
    q = []
    heapq.heapify(q)
    heapq.heappush(q, (0, source, {source}))

    while q:
        cost, current, seen = heapq.heappop(q)

        if seen == nodes.keys():
            return cost

        for next, distance in nodes.get(current, []):
            if next in seen: continue

            heapq.heappush(q, (distance + cost, next, seen | {next}))

    return float("inf")

def longest_path(source):
    q = []
    heapq.heapify(q)
    heapq.heappush(q, (0, source, {source}))

    while q:
        cost, current, seen = heapq.heappop(q)

        if seen == nodes.keys():
            return -cost

        for next, distance in nodes.get(current, []):
            if next in seen: continue

            heapq.heappush(q, (cost - distance, next, seen | {next}))

    return float("-inf")

def part1():
    min_cost = float("inf")
    for node in nodes.keys():
        min_cost = min(min_cost, shortest_path(node))

    print(min_cost)


def part2():
    max_cost = float("-inf")
    for node in nodes.keys():
        max_cost = max(max_cost, longest_path(node))

    print(max_cost)

part1()
part2()