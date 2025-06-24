import functools
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

c = 0

@functools.cache
def find_combination_of_weights(weights, expected, used):
    weights = set(weights)
    if expected == 0:
        global c
        c+=1
        print(c, used)
        return frozenset(frozenset({tuple(used)}))
    if expected < 0:
        return None

    result = set()
    if sum(weights) < expected:
        return None

    for weight in weights:
        items = find_combination_of_weights(frozenset(weights - {weight}), expected - weight, frozenset(used | {weight}))
        if items:
            result |= items
    return frozenset(result)


total_weight = sum(weights)
single_group = total_weight // 3

g1_combinations = find_combination_of_weights(frozenset(weights), single_group, frozenset())
groups = []
print(len(g1_combinations))

# for g1_combination in g1_combinations:
#     g2_weights = set(weights) - set(g1_combination)
#     g2_combinations = find_combination_of_weights(frozenset(g2_weights), single_group, frozenset())
#     for g2_combination in g2_combinations:
#         g3_combination = tuple(set(g2_weights) - set(g2_combination))
#         qe_value = qe(g1_combination)
#         groups.append((qe_value, g1_combination, g2_combination, g3_combination))
#         print(len(groups))
#
# groups = sorted(groups, key=lambda g: g[0])
# groups = sorted(groups, key=lambda g: len(g[1]))
# print(groups[0][0])
