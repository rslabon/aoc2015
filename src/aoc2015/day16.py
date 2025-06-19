import re

with open("../../resources/day16.txt") as f:
    lines = f.read().strip().splitlines()

aunts = []
for line in lines:
    nr, rest = re.findall(r"Sue (\d+): (.*)", line)[0]
    nr = int(nr)
    parts = rest.split(",")
    properties = dict()
    for part in parts:
        p1, p2 = part.split(": ")
        p1 = p1.strip()
        p2 = p2.strip()
        properties[p1] = int(p2)

    aunts.append((nr, properties))

pattern = {
    "children": 3,
    "cats": 7,
    "samoyeds": 2,
    "pomeranians": 3,
    "akitas": 0,
    "vizslas": 0,
    "goldfish": 5,
    "trees": 3,
    "cars": 2,
    "perfumes": 1
}


def part1():
    max_score = float("-inf")
    max_nr = None
    for nr, properties in aunts:
        score = 0
        for k in properties.keys():
            if pattern[k] == properties[k]:
                score += 1
        if max_score < score:
            max_score = score
            max_nr = nr

    print(max_nr)


def part2():
    max_score = float("-inf")
    max_nr = None
    for nr, properties in aunts:
        score = 0
        for k in properties.keys():
            if k in ["cats", "trees"]:
                if pattern[k] < properties[k]:
                    score += 1
            elif k in ["pomeranians", "goldfish"]:
                if pattern[k] > properties[k]:
                    score += 1
            elif pattern[k] == properties[k]:
                score += 1
        if max_score < score:
            max_score = score
            max_nr = nr

    print(max_nr)


part1()
part2()
