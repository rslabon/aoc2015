def increment(s):
    result = list(reversed(s))
    i = 0
    carry = 1
    while i < len(result) and carry == 1:
        next_char = ord(result[i]) - 97 + carry
        if next_char > 25:
            next_char = 0
            carry = 1
        else:
            carry = 0

        result[i] = chr(97 + next_char)
        i += 1

    return "".join(reversed(result))


def contains_increasing_letters(s):
    i = 0
    while i <= len(s) - 3:
        window = s[i:i + 3]
        if ord(window[2]) - ord(window[1]) == 1 and ord(window[1]) - ord(window[0]) == 1:
            return True
        i += 1

    return False


def has_illegal_letters(s):
    return "l" in s or "o" in s or "i" in s


def has_pairs(s):
    i = 0
    pairs = set()
    while i < len(s):
        j = i + 1
        while j < len(s) and s[j] == s[i]:
            j += 1
        block = s[i: j]
        i = j
        if len(block) == 2:
            pairs.add(block)

    return len(pairs) > 1


def confirm_policy(s):
    return contains_increasing_letters(s) and not has_illegal_letters(s) and has_pairs(s)


def next_password(s):
    done = False
    while not done:
        s = increment(s)
        done = confirm_policy(s)

    return s


def part1():
    print(next_password("vzbxkghb"))


def part2():
    print(next_password("vzbxxyzz"))


part1()
part2()
