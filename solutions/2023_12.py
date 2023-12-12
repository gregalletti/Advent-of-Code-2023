import time
from utils import print_blue, print_purple, download_input
import os.path
from functools import cache

# setup
YEAR = 2023
DAY = 12
start_time = time.time()
path = f"./inputs/{YEAR}_{DAY}.txt"

if not os.path.isfile(path):
    download_input(YEAR, DAY)

# common
@cache
def dp(springs, groups, curr_len):
    res = 0
    if not springs:
        # we closed everything, return True -> res + 1
        return len(groups) == 0 and curr_len == 0
    # 2 options when ?, check them both
    status = [".", "#"] if springs[0] == "?" else springs[0]
    for s in status:
        if s == "#":
            # still need to finish the group
            res += dp(springs[1:], groups, curr_len + 1)
        else:
            if curr_len > 0:
                # got the right value for the group
                if groups and groups[0] == curr_len:
                    res += dp(springs[1:], groups[1:], 0)
            else:
                # just go next
                res += dp(springs[1:], groups, 0)
    return res

# part 1
def part_1():
    res = 0
    for springs, groups in lines:
        # easier to stop
        springs += "."
        res += dp(springs, groups, 0)
    return res

# part 2
def part_2():
    res = 0
    for springs, groups in lines:
        # follow 5x requirements
        springs = (springs + "?") * 4 + springs + "."
        res += dp(springs, groups * 5, 0)
    return res

# parsing and execution
with open(path) as f:
    input = [line.split() for line in f.read().splitlines()]

    lines = [(springs, tuple(map(int, groups.split(",")))) for springs, groups in input]

    print_blue(part_1())
    print(f"Completed {YEAR}-{DAY} PART 1 in {time.time() - start_time} s\n")

    start_time = time.time()
    print_purple(part_2())
    print(f"Completed {YEAR}-{DAY} PART 2 in {time.time() - start_time} s")