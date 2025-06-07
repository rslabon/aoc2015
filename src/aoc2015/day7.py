lines = """
123 -> x
456 -> y
x AND y -> d
x OR y -> e
x LSHIFT 2 -> f
y RSHIFT 2 -> g
NOT x -> h
NOT y -> i
NOT d -> j
""".strip().splitlines()

with open("../../resources/day7.txt") as f:
    lines = f.read().strip().splitlines()


def apply(env, name):
    if not name in env:
        return int(name)
    if callable(env[name]):
        env[name] = env[name]()
        return env[name]
    return env[name]


def eval(env, expression):
    if expression.isdigit():
        return lambda: int(expression)
    elif "AND" in expression:
        op1, op2 = expression.split(" AND ")
        return lambda: apply(env, op1) & apply(env, op2)
    elif "OR" in expression:
        op1, op2 = expression.split(" OR ")
        return lambda: apply(env, op1) | apply(env, op2)
    elif "NOT" in expression:
        op = expression.replace("NOT ", "")
        return lambda: 65535 - apply(env, op)
    elif "LSHIFT" in expression:
        op1, op2 = expression.split(" LSHIFT ")
        return lambda: apply(env, op1) << int(op2)
    elif "RSHIFT" in expression:
        op1, op2 = expression.split(" RSHIFT ")
        return lambda: apply(env, op1) >> int(op2)
    else:
        return lambda: apply(env, expression)


env = dict()


def part1():
    env = dict()
    for line in lines:
        left, right = line.split(" -> ")
        env[right] = eval(env, left)

    return apply(env, "a")


def part2():
    env = dict()
    for line in lines:
        left, right = line.split(" -> ")
        if right == "b":
            left = str(part1())
        env[right] = eval(env, left)

    return apply(env, "a")


print(part1())
print(part2())
