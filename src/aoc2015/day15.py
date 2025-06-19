import re
from collections import deque
from functools import reduce

lines = """
Butterscotch: capacity -1, durability -2, flavor 6, texture 3, calories 8
Cinnamon: capacity 2, durability 3, flavor -2, texture -1, calories 3
""".strip().splitlines()

with open('../../resources/day15.txt') as f:
    lines = f.read().strip().splitlines()


def total_score(teaspoons, ingredients, max_calories):
    score = []
    for index in range(5):
        result = 0
        for properties_index, properties in enumerate(ingredients):
            result += teaspoons[properties_index] * properties[index]

        score.append(max(0, result))

    if max_calories:
        if score[4] == 500:
            return reduce(lambda x, y: x * y, score[:4], 1)
        else:
            return 0

    return reduce(lambda x, y: x * y, score[:4], 1)


ingredients = []
for line in lines:
    capacity, durability, flavor, texture, calories = \
        re.findall(r"\w+: capacity (-?\d+), durability (-?\d+), flavor (-?\d+), texture (-?\d+), calories (-?\d+)",
                   line)[0]
    capacity = int(capacity)
    durability = int(durability)
    flavor = int(flavor)
    texture = int(texture)
    calories = int(calories)

    ingredients.append([capacity, durability, flavor, texture, calories])


def possible():
    q = deque()
    q.append((100, 0, 0, 0))

    result = set()
    while q:
        x, y, z, k = q.popleft()

        if x < 0 or y < 0 or z < 0 or k < 0:
            continue
        if x > 100 or y > 100 or z > 100 or k > 100:
            continue
        if (x, y, z, k) in result:
            continue

        result.add((x, y, z, k))

        q.append((x + 1, y - 1, z, k))
        q.append((x + 1, y, z - 1, k))
        q.append((x + 1, y, z, k - 1))

        q.append((x - 1, y + 1, z, k))
        q.append((x, y + 1, z - 1, k))
        q.append((x, y + 1, z, k - 1))

        q.append((x - 1, y, z + 1, k))
        q.append((x, y - 1, z + 1, k))
        q.append((x, y, z + 1, k - 1))

        q.append((x - 1, y, z, k + 1))
        q.append((x, y - 1, z, k + 1))
        q.append((x, y, z - 1, k + 1))

    return result


def part1():
    max_total_score = float("-inf")
    for x, y, z, k in possible():
        max_total_score = max(max_total_score, total_score([x, y, z, k], ingredients, None))

    print(max_total_score)


def part2():
    max_total_score = float("-inf")
    for x, y, z, k in possible():
        max_total_score = max(max_total_score, total_score([x, y, z, k], ingredients, 500))

    print(max_total_score)


part1()
part2()
