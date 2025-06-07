with open("../../resources/day8.txt", "r") as f:
    lines = f.read().splitlines()


# lines = ['""', '"abc"', '"aaa\\"aaa"', '"\\x27"']


def chars(s):
    return len(eval(s))


def codes(s):
    return len(s)


def encode_codes(s):
    ss = s.replace("\\", "\\\\").replace("\"", "\\\"")
    return len(f"\"{ss}\"")


def part1():
    total = 0
    for line in lines:
        total += codes(line) - chars(line)

    print(total)


def part2():
    total = 0
    for line in lines:
        total += encode_codes(line) - codes(line)

    print(total)


part1()
part2()
