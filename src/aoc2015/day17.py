containers = [
    43,
    3,
    4,
    10,
    21,
    44,
    4,
    6,
    47,
    41,
    34,
    17,
    17,
    44,
    36,
    31,
    46,
    9,
    27,
    38,
]


def combinations_of_containers(containers, value, prev_containers):
    if value < 0:
        return None
    if value == 0:
        return [prev_containers]
    if not containers:
        return None

    result = []
    for i, container in enumerate(containers):
        comb = combinations_of_containers(containers[i + 1:], value - container, prev_containers + [container])
        if comb:
            result += comb

    return result


def part1():
    combinations = combinations_of_containers(containers, 150, [])
    print(len(combinations))


def part2():
    combinations = combinations_of_containers(containers, 150, [])
    min_containers = float('inf')
    for combination in combinations:
        min_containers = min(min_containers, len(combination))

    ways = 0
    for combination in combinations:
        if min_containers == len(combination):
            ways += 1

    print(ways)


part1()
part2()
