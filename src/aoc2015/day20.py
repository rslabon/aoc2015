import math


def dividers(n):
    result = []
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            if n // i == i:
                result.append(i)
            else:
                result.append(n // i)
                result.append(i)
    return result


def part1():
    i = 1
    while i <= 36000000:
        divs = dividers(i)
        s = sum([d * 10 for d in divs])
        if s >= 36000000:
            print(i)
            break
        i += 1


def part2():
    i = 1
    visited = {}
    while i <= 36000000:
        divs = dividers(i)
        s = 0
        for d in divs:
            if d not in visited:
                visited[d] = 0
            if visited[d] == 50:
                continue
            visited[d] += 1
            s += d * 11

        if s >= 36000000:
            print(i)
            break
        i += 1


# part1()
part2()
