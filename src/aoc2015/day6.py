import re

with open("../../resources/day6.txt") as f:
    lines = f.read().strip().splitlines()


def part1():
    grid = []
    for row in range(0, 1000):
        grid.append([])
        for col in range(0, 1000):
            grid[row].append(False)

    def turn_on(grid, x0, y0, x1, y1):
        for x in range(x0, x1 + 1):
            for y in range(y0, y1 + 1):
                grid[x][y] = True

    def turn_off(grid, x0, y0, x1, y1):
        for x in range(x0, x1 + 1):
            for y in range(y0, y1 + 1):
                grid[x][y] = False

    def toggle(grid, x0, y0, x1, y1):
        for x in range(x0, x1 + 1):
            for y in range(y0, y1 + 1):
                grid[x][y] = not grid[x][y]

    for line in lines:
        if line.startswith("turn on"):
            x0, y0, x1, y1 = re.findall(r"turn on (\d+),(\d+) through (\d+),(\d+)", line)[0]
            turn_on(grid, int(x0), int(y0), int(x1), int(y1))
        if line.startswith("turn off"):
            x0, y0, x1, y1 = re.findall(r"turn off (\d+),(\d+) through (\d+),(\d+)", line)[0]
            turn_off(grid, int(x0), int(y0), int(x1), int(y1))
        if line.startswith("toggle"):
            x0, y0, x1, y1 = re.findall(r"toggle (\d+),(\d+) through (\d+),(\d+)", line)[0]
            toggle(grid, int(x0), int(y0), int(x1), int(y1))

    lit = 0
    for x in range(0, 1000):
        for y in range(0, 1000):
            if grid[x][y]:
                lit += 1

    print(lit)


def part2():
    grid = []
    for row in range(0, 1000):
        grid.append([])
        for col in range(0, 1000):
            grid[row].append(0)

    def turn_on(grid, x0, y0, x1, y1):
        for x in range(x0, x1 + 1):
            for y in range(y0, y1 + 1):
                grid[x][y] += 1

    def turn_off(grid, x0, y0, x1, y1):
        for x in range(x0, x1 + 1):
            for y in range(y0, y1 + 1):
                grid[x][y] -= 1
                grid[x][y] = max(0, grid[x][y])

    def toggle(grid, x0, y0, x1, y1):
        for x in range(x0, x1 + 1):
            for y in range(y0, y1 + 1):
                grid[x][y] += 2

    for line in lines:
        if line.startswith("turn on"):
            x0, y0, x1, y1 = re.findall(r"turn on (\d+),(\d+) through (\d+),(\d+)", line)[0]
            turn_on(grid, int(x0), int(y0), int(x1), int(y1))
        if line.startswith("turn off"):
            x0, y0, x1, y1 = re.findall(r"turn off (\d+),(\d+) through (\d+),(\d+)", line)[0]
            turn_off(grid, int(x0), int(y0), int(x1), int(y1))
        if line.startswith("toggle"):
            x0, y0, x1, y1 = re.findall(r"toggle (\d+),(\d+) through (\d+),(\d+)", line)[0]
            toggle(grid, int(x0), int(y0), int(x1), int(y1))

    brightness = 0
    for x in range(0, 1000):
        for y in range(0, 1000):
            brightness += grid[x][y]

    print(brightness)


# part1()
part2()
