import re

lines = """
Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.
Dancer can fly 16 km/s for 11 seconds, but then must rest for 162 seconds.
""".strip().splitlines()

with open("../../resources/day14.txt") as f:
    lines = f.read().strip().splitlines()

reindeers = []
for line in lines:
    reindeer, distance, distance_time, rest = \
        re.findall(r"(\w+) can fly (\d+) km/s for (\d+) seconds, but then must rest for (\d+) seconds.", line)[0]
    distance = int(distance)
    distance_time = int(distance_time)
    rest = int(rest)
    reindeers.append((reindeer, distance, distance_time, rest))


def at_time(time, reindeers):
    max_total = float('-inf')
    for _, distance, distance_time, rest in reindeers:
        m = int(time / (distance_time + rest))
        left = time - (m * (distance_time + rest))
        if left >= distance_time:
            m += 1
        total_distance = m * distance_time * distance
        max_total = max(max_total, total_distance)
    return max_total


def scored(time, reindeers):
    tic = 1
    reindeers_score = []
    for _, _, distance_time, rest in reindeers:
        reindeers_score.append([0, distance_time, rest, 0])

    while tic <= time:
        for index, (_, distance, distance_time, rest) in enumerate(reindeers):
            if reindeers_score[index][1] > 0:
                reindeers_score[index][0] += distance
                reindeers_score[index][1] -= 1
            else:
                reindeers_score[index][2] -= 1
                if reindeers_score[index][2] == 0:
                    reindeers_score[index][1] = distance_time
                    reindeers_score[index][2] = rest

        best = max(reindeers_score, key=lambda item: item[0])
        best[3] += 1
        tic += 1

    best = max(reindeers_score, key=lambda item: item[3])
    return best[3]


def part1():
    print(at_time(2503, reindeers))


def part2():
    print(scored(2503, reindeers))


part1()
part2()
