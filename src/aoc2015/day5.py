from collections import Counter


def has_at_least3_vowels(s):
    c = Counter(s)
    count_vowels = 0
    for v in "aeiou":
        count_vowels += c.get(v, 0)

    return count_vowels >= 3


def has_double_letter(s):
    i = 1
    while i < len(s):
        if s[i] == s[i - 1]:
            return True

        i += 1

    return False


def has_prohibited(s):
    for p in ["ab", "cd", "pq", "xy"]:
        if s.find(p) > 0:
            return True

    return False


def is_nice_string(s):
    return has_at_least3_vowels(s) and has_double_letter(s) and not has_prohibited(s)


def has_repeating(s):
    i = 0
    widow = s[i:i + 3]
    while i + 3 <= len(s):
        if widow[0] == widow[2]:
            return True

        i += 1
        widow = s[i:i + 3]

    return False


def has_pair(s):
    i = 0
    widow = s[i:i + 2]
    while i + 2 < len(s):
        if widow in s[i + 2:]:
            return True

        i += 1
        widow = s[i:i + 2]

    return False


def is_nice_string2(s):
    return has_repeating(s) and has_pair(s)


def part1():
    with open("../../resources/day5.txt") as f:
        strings = f.read().strip().splitlines()

    count = 0
    for s in strings:
        if is_nice_string(s):
            count += 1

    print(count)


def part2():
    with open("../../resources/day5.txt") as f:
        strings = f.read().strip().splitlines()

    count = 0
    for s in strings:
        if is_nice_string2(s):
            count += 1

    print(count)


part1()
part2()
