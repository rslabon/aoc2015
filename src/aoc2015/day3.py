with open("../../resources/day3.txt") as f:
    moves = f.read().strip()


# moves = "^v^v^v^v^v"
# moves = "^>v<"
# moves = "^v"

def count_houses(moves):
    x, y = 0, 0
    path = [(x, y)]
    for move in moves:
        if move == ">":
            x += 1
        if move == "<":
            x -= 1
        if move == "v":
            y += 1
        if move == "^":
            y -= 1

        path.append((x, y))

    return set(path)


def part1():
    print(len(count_houses(moves)))


def part2():
    houses = count_houses(moves[::2]) | count_houses(moves[1::2])
    print(len(houses))


part1()
part2()
