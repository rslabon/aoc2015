import functools
import itertools

weapons = [(8, 4, 0), (10, 5, 0), (25, 6, 0), (40, 7, 0), (74, 8, 0)]
armors = [(13, 0, 1), (31, 0, 2), (53, 0, 3), (75, 0, 4), (102, 0, 5)]
rings = [(25, 1, 0), (50, 2, 0), (100, 3, 0), (20, 0, 1), (40, 0, 2), (80, 0, 3)]
boss = (109, 8, 2)


@functools.cache
def play(player, boss, player_turn):
    phit_points, pdamage, parmor = player
    bhit_points, bdamage, barmor = boss

    if player_turn:
        bhit_points = bhit_points + barmor - pdamage
        if bhit_points <= 0:
            return True
        return play((phit_points, pdamage, parmor), (bhit_points, bdamage, barmor), False)
    else:
        phit_points = phit_points + parmor - bdamage
        if phit_points <= 0:
            return False
        return play((phit_points, pdamage, parmor), (bhit_points, bdamage, barmor), True)


def part1():
    min_cost = float("inf")
    for weapon in weapons:
        wcost, wdamage, _ = weapon
        only_weapon_play = play((100, wdamage, 0), boss, True)
        if only_weapon_play:
            min_cost = min(min_cost, wcost)

        for ring in rings:
            rcost, rdemage, rarmor = ring
            one_ring_play = play((100, rdemage + wdamage, rarmor), boss, True)
            if one_ring_play:
                min_cost = min(min_cost, wcost + rcost)

        for r1, r2 in itertools.combinations(rings, 2):
            r1cost, r1demage, r1armor = r1
            r2cost, r2demage, r2armor = r2
            two_ring_play = play((100, r1demage + r2demage + wdamage, r1armor + r2armor), boss, True)
            if two_ring_play:
                min_cost = min(min_cost, wcost + r1cost + r2cost)

        for armor in armors:
            acost, _, armor = armor
            armor_play = play((100, wdamage, armor), boss, True)
            if armor_play:
                min_cost = min(min_cost, wcost + acost)
            for ring in rings:
                rcost, rdemage, rarmor = ring
                one_ring_play = play((100, rdemage + wdamage, rarmor + armor), boss, True)
                if one_ring_play:
                    min_cost = min(min_cost, wcost + acost + rcost)
            for r1, r2 in itertools.combinations(rings, 2):
                r1cost, r1demage, r1armor = r1
                r2cost, r2demage, r2armor = r2
                two_ring_play = play((100, r1demage + r2demage + wdamage, r1armor + r2armor + armor), boss, True)
                if two_ring_play:
                    min_cost = min(min_cost, wcost + acost + r1cost + r2cost)

    print(min_cost)


def part2():
    max_cost = float("-inf")
    for weapon in weapons:
        wcost, wdamage, _ = weapon
        only_weapon_play = play((100, wdamage, 0), boss, True)
        if not only_weapon_play:
            max_cost = max(max_cost, wcost)

        for ring in rings:
            rcost, rdemage, rarmor = ring
            one_ring_play = play((100, rdemage + wdamage, rarmor), boss, True)
            if not one_ring_play:
                max_cost = max(max_cost, wcost + rcost)

        for r1, r2 in itertools.combinations(rings, 2):
            r1cost, r1demage, r1armor = r1
            r2cost, r2demage, r2armor = r2
            two_ring_play = play((100, r1demage + r2demage + wdamage, r1armor + r2armor), boss, True)
            if not two_ring_play:
                max_cost = max(max_cost, wcost + r1cost + r2cost)

        for armor in armors:
            acost, _, armor = armor
            armor_play = play((100, wdamage, armor), boss, True)
            if not armor_play:
                max_cost = max(max_cost, wcost + acost)
            for ring in rings:
                rcost, rdemage, rarmor = ring
                one_ring_play = play((100, rdemage + wdamage, rarmor + armor), boss, True)
                if not one_ring_play:
                    max_cost = max(max_cost, wcost + acost + rcost)
            for r1, r2 in itertools.combinations(rings, 2):
                r1cost, r1demage, r1armor = r1
                r2cost, r2demage, r2armor = r2
                two_ring_play = play((100, r1demage + r2demage + wdamage, r1armor + r2armor + armor), boss, True)
                if not two_ring_play:
                    max_cost = max(max_cost, wcost + acost + r1cost + r2cost)

    print(max_cost)


part1()
part2()
