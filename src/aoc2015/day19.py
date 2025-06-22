with open("../../resources/day19.txt") as f:
    transitions_block, molecules = f.read().strip().split("\n\n")

transitions = []
for line in transitions_block.strip().splitlines():
    transition_from, transition_to = line.split(" => ")
    transitions.append((transition_from.strip(), transition_to.strip()))


def calibrate(transitions, molecules):
    if len(molecules) == 0 or len(transitions) == 0:
        return set()

    transition_from, transition_to = transitions[0]
    i = 0
    result = set()
    while i < len(molecules):
        if molecules[i:i + len(transition_from)] == transition_from:
            value = molecules[0:i] + transition_to + molecules[i + len(transition_from):]
            result.add(value)
            i += len(transition_from)
        else:
            i += 1

    return result | calibrate(transitions[1:], molecules)


def replacements(transitions, molecules):
    value = molecules
    r = 0
    while True:
        change = False
        for transition_to, transition_from in transitions:
            index = value.find(transition_from)
            if index >= 0:
                value = value[0:index] + transition_to + value[index + len(transition_from):]
                r += 1
                change = True
        if not change:
            break

    return r


def part1():
    print(len(calibrate(transitions, molecules)))


def part2():
    transitions.sort(key=lambda t: len(t[1]), reverse=True)
    print(replacements(transitions, molecules))


part1()
part2()
