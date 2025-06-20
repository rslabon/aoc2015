with open("../../resources/day18.txt") as f:
    lines = f.read().strip().splitlines()


def create_grid(lines):
    grid = dict()
    for row, line in enumerate(lines):
        for col, val in enumerate(line):
            if val == "#":
                grid[row, col] = 1
            else:
                grid[row, col] = 0

    return grid


def next_step(grid, part2):
    if part2:
        grid[0, 0] = 1
        grid[0, 99] = 1
        grid[99, 0] = 1
        grid[99, 99] = 1

    new_grid = dict()
    for (row, col), v in grid.items():
        on_count = 0
        off_count = 0
        for rx, cx in [[1, 0], [0, 1], [-1, 0], [0, -1], [-1, -1], [-1, 1], [1, -1], [1, 1]]:
            if (row + rx, col + cx) not in grid:
                continue
            if grid[(row + rx, col + cx)] == 0:
                off_count += 1
            else:
                on_count += 1
        if grid[row, col] == 1:
            if 2 <= on_count <= 3:
                new_grid[row, col] = 1
            else:
                new_grid[row, col] = 0

        if grid[row, col] == 0:
            if on_count == 3:
                new_grid[row, col] = 1
            else:
                new_grid[row, col] = 0

    if part2:
        new_grid[0, 0] = 1
        new_grid[0, 99] = 1
        new_grid[99, 0] = 1
        new_grid[99, 99] = 1

    return new_grid


def part1():
    grid = create_grid(lines)
    for i in range(0, 100):
        grid = next_step(grid, False)

    on_count = len([v for v in grid.values() if v == 1])
    print(on_count)


def part2():
    grid = create_grid(lines)
    for i in range(0, 100):
        grid = next_step(grid, True)

    on_count = len([v for v in grid.values() if v == 1])
    print(on_count)


part1()
part2()
