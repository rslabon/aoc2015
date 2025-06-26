from collections import deque

grid = {
    (1, 1): 20151125
}


def generate_code(max_row, max_col):
    q = deque([(1, 1, 20151125)])

    while q:
        r, c, code = q.popleft()

        grid[r, c] = code

        if r == max_row and c == max_col:
            break

        if r == 1:
            q.append((c + 1, 1, code * 252533 % 33554393))
        else:
            q.append((r - 1, c + 1, code * 252533 % 33554393))


generate_code(2978, 3083)
print(grid[(2978, 3083)])
