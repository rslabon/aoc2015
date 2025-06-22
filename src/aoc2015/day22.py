import functools

boss = (51, 9)
spells = [
    ("Magic Missile", 53,
     lambda player, boss: ((player), (boss[0] - 4, boss[1])),
     lambda player, boss: (player, boss),
     0),
    ("Drain", 73,
     lambda player, boss: ((player[0] + 2, player[1], player[2], player[3]), (boss[0] - 2, boss[1])),
     lambda player, boss: (player, boss),
     0),
    ("Shield", 113,
     lambda player, boss: ((player[0], player[1], 7, player[3]), boss),
     lambda player, boss: ((player[0], player[1], 0, player[3]), boss),
     6),
    ("Poison", 173,
     lambda player, boss: ((player), (boss[0] - 3, boss[1])),
     lambda player, boss: (player, boss),
     6),
    ("Recharge", 229,
     lambda player, boss: ((player[0], player[1] + 101, player[2], player[3]), boss),
     lambda player, boss: (player, boss),
     5),
]


def choose_spells(player, effects):
    _, mana, _, _ = player
    return [spell for spell in spells if spell[0] not in effects.keys() and mana >= spell[1]]


def freezedict(d):
    return tuple(d.items())


def unfreezedict(d):
    return dict(d)


@functools.cache
def play(player, boss, player_turn, effects, hard):
    if hard and player_turn:
        phit_points, pmana, parmor, pspend = player
        player = (phit_points - 1, pmana, parmor, pspend)
        if player[0] <= 0:
            return False, None

    wears_off_effects = set()
    effects = unfreezedict(effects)
    for name, (turn, fn, undo_fn) in effects.items():
        player, boss = fn(player, boss)
        turn -= 1
        if turn == 0:
            wears_off_effects.add(name)
            player, boss = undo_fn(player, boss)
        else:
            effects[name] = (turn, fn, undo_fn)

        bhit_points, bdamage = boss
        if bhit_points <= 0:
            return True, player[3]

    for name in wears_off_effects:
        del effects[name]

    if player_turn:
        spells = choose_spells(player, effects)
        if not spells:
            return False, None

        min_spend = float("inf")
        won = False
        for spell in spells:
            copy_effects = effects.copy()
            copy_player = player
            copy_boss = boss
            spell_name, spell_cost, spell_fn, spell_undo_fn, spell_turn = spell
            if spell_turn > 0:
                copy_effects[spell_name] = (spell_turn, spell_fn, spell_undo_fn)
            else:
                copy_player, copy_boss = spell_fn(copy_player, copy_boss)

            phit_points, pmana, parmor, pspend = copy_player
            copy_player = (phit_points, pmana - spell_cost, parmor, pspend + spell_cost)
            bhit_points, bdamage = copy_boss
            if bhit_points <= 0:
                return True, copy_player[3]

            player_won, player_spend = play(copy_player, copy_boss, False, freezedict(copy_effects), hard)
            if player_won:
                won = True
                min_spend = min(min_spend, player_spend)

        if won:
            return True, min_spend
        else:
            return False, None
    else:
        bhit_points, bdamage = boss
        phit_points, pmana, parmor, pspend = player
        phit_points = phit_points - max(1, (bdamage - parmor))
        if phit_points <= 0:
            return False, None

        return play((phit_points, pmana, parmor, pspend), boss, True, freezedict(effects.copy()), hard)


def part1():
    print(play((50, 500, 0, 0), boss, True, freezedict({}), False))


def part2():
    print(play((50, 500, 0, 0), boss, True, freezedict({}), True))


part1()
part2()
