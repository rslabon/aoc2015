import hashlib


def part1():
    i = 0
    while True:
        hash = hashlib.md5(f"yzbqklnj{i}".encode('utf-8')).hexdigest()
        if hash.startswith("00000") and hash[5:6].isdigit():
            n = int(hash[5:6])
            if 1 <= n:
                print(i)
                break
        i += 1


def part2():
    i = 0
    while True:
        hash = hashlib.md5(f"yzbqklnj{i}".encode('utf-8')).hexdigest()
        if hash.startswith("000000") and hash[6:7].isdigit():
            n = int(hash[6:7])
            if 1 <= n:
                print(i)
                break
        i += 1


part1()
part2()
