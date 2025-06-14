import functools


@functools.cache
def say(number):
    s = str(number)
    c = 1
    i = 1
    result = ""
    while i < len(s):
        if s[i] == s[i - 1]:
            c += 1
        else:
            result += f"{c}{s[i - 1]}"
            c = 1

        i += 1

    result += f"{c}{s[i - 1]}"

    return result


def part1():
    n = 1321131112
    for _ in range(0, 40):
        n = say(n)

    print(len(str(n)))


def part2():
    n = 1321131112
    for _ in range(0, 50):
        n = say(n)

    print(len(str(n)))


part1()
part2()
