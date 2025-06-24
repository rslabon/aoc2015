instructions = [
    "inc a",
    "jio a, +2",
    "tpl a",
    "inc a"
]

with open('../../resources/day23.txt') as f:
    instructions = f.read().strip().splitlines()


def execute(instructions, register):
    pc = 0
    while 0 <= pc < len(instructions):
        instruction = instructions[pc]
        if instruction.startswith('hlf'):
            r = instruction.replace('hlf ', '')
            register[r] = register[r] / 2
            pc += 1
        if instruction.startswith('tpl'):
            r = instruction.replace('tpl ', '')
            register[r] = register[r] * 3
            pc += 1
        if instruction.startswith('inc'):
            r = instruction.replace('inc ', '')
            register[r] = register[r] + 1
            pc += 1
        if instruction.startswith('jmp'):
            offset = instruction.replace('jmp ', '')
            offset = int(offset)
            pc += offset
        if instruction.startswith('jie'):
            r, offset = instruction.replace('jie ', '').split(',')
            if register[r] % 2 == 0:
                offset = int(offset)
                pc += offset
            else:
                pc += 1
        if instruction.startswith('jio'):
            r, offset = instruction.replace('jio ', '').split(',')
            if register[r] == 1:
                offset = int(offset)
                pc += offset
            else:
                pc += 1

    return register


def part1():
    print(execute(instructions, {"a": 0, "b": 0}))


def part2():
    print(execute(instructions, {"a": 1, "b": 0}))


part1()
part2()
