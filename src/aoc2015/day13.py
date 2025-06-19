import itertools
import re

lines = """
Alice would gain 54 happiness units by sitting next to Bob.
Alice would lose 79 happiness units by sitting next to Carol.
Alice would lose 2 happiness units by sitting next to David.
Bob would gain 83 happiness units by sitting next to Alice.
Bob would lose 7 happiness units by sitting next to Carol.
Bob would lose 63 happiness units by sitting next to David.
Carol would lose 62 happiness units by sitting next to Alice.
Carol would gain 60 happiness units by sitting next to Bob.
Carol would gain 55 happiness units by sitting next to David.
David would gain 46 happiness units by sitting next to Alice.
David would lose 7 happiness units by sitting next to Bob.
David would gain 41 happiness units by sitting next to Carol.
""".strip().splitlines()

with open("../../resources/day13.txt") as f:
    lines = f.read().strip().splitlines()

scheme = dict()

for line in lines:
    person1, action, happiness, person2 = \
        re.findall(r"(\w+) would (gain|lose)+ (\d+) happiness units by sitting next to (\w+).", line)[0]
    action = 1 if action == "gain" else -1
    happiness = int(happiness)
    adj = scheme.get(person1, dict())
    adj[person2] = action * happiness
    scheme[person1] = adj


def find_max(scheme):
    possible = list(itertools.permutations(scheme.keys()))
    max_cost = float("-inf")
    for persons in possible:
        cost = scheme[persons[0]][persons[-1]]
        i = 1
        while i < len(persons):
            cost += scheme[persons[i - 1]][persons[i]]
            cost += scheme[persons[i]][persons[i - 1]]
            i += 1
        cost += scheme[persons[-1]][persons[0]]
        max_cost = max(max_cost, cost)

    return max_cost


def part1():
    print(find_max(scheme))


def part2():
    new_scheme = dict(scheme)
    new_scheme['me'] = dict()
    for p in scheme.keys():
        new_scheme['me'][p] = 0
        new_scheme[p]['me'] = 0

    print(find_max(new_scheme))


part1()
part2()
