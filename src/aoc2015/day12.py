import json

with open('../../resources/day12.txt', 'r') as f:
    puzzle = f.read().strip()


def add_numbers(data, red=False):
    if isinstance(data, int):
        return data
    if isinstance(data, list):
        total = 0
        for item in data:
            total += add_numbers(item, red)
        return total
    if isinstance(data, dict):
        total = 0
        for _, value in data.items():
            if red and value == "red":
                return 0
            total += add_numbers(value, red)
        return total

    return 0


def part1():
    print(add_numbers(json.loads(puzzle)))


def part2():
    print(add_numbers(json.loads(puzzle), True))


part1()
part2()
