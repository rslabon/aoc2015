def combinations(items, t):
    if t == 0:
        return []
    if t == len(items):
        return items

    j = 1
    c = [0]
    while j <= (t + 2):
        c.append(j - 1)
        j += 1

    n = len(items)
    c[t + 1] = n
    c[t + 2] = 0

    result = []
    while True:
        combination = []
        for i in range(1, t + 1):
            combination.append(items[c[i]])
        result.append(combination)

        j = 1
        while c[j] + 1 == c[j + 1]:
            c[j] = j - 1
            j += 1
        if j > t:
            break
        c[j] += 1

    return result


print(combinations([1, 2, 3, 4, 5], 3))
