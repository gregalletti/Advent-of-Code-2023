import time
from utils import print_blue, print_purple, download_input
import os.path

# setup
YEAR = 2023
DAY = 13
start_time = time.time()
path = f"./inputs/{YEAR}_{DAY}.txt"

if not os.path.isfile(path):
    download_input(YEAR, DAY)

# common
def count_differences(l1, l2):
    d = 0
    for i in range(len(l1)):
        if l1[i] != l2[i]:
            d += 1
    return d

def find_horizontal_mirror(pattern, smudge=0):
    rows = len(pattern)
    all_lines = []
    for r in range(rows - 1):
        mirror_range = min(r + 1, rows - (r + 1))
        type = is_mirror(pattern, r, mirror_range, smudge)
        if smudge:
            if type == 1:
                # old line
                all_lines.append((r + 1, 'old'))
            elif type == 2:
                # new line found
                all_lines.append((r + 1, 'new'))
        else:
            if type == 1:
                return r + 1
    return all_lines if smudge else None

def is_mirror(pattern, r, mirror_range, smudge=0):
    new = False
    for i in range(mirror_range):
        diff = count_differences(pattern[r - i], pattern[r + i + 1])
        if diff == 0:
            continue
        elif diff == 1 and smudge:
            if new:
                return 0
            new = True
            continue
        else:
            return 0
    return 2 if new else 1

# part 1
def part_1():
    res = 0
    for pattern in input:
        h = find_horizontal_mirror(pattern)
        if h is not None:
            res += 100 * h
        else:
            transposed = [''.join(s) for s in zip(*pattern)]
            v = find_horizontal_mirror(transposed)
            res += v
    return res

# part 2
def part_2():
    res = 0
    for pattern in input:
        tmp = 0
        found = False
        h = find_horizontal_mirror(pattern, 1)
        for t in h:
            if t[1] == 'new':
                # new line found here, no need to check further
                found = True
                tmp = 100 * t[0]
                break
            else:
                # keep the old value for now, replaced if there is a new vertical line
                tmp = 100 * t[0]
        if not found:
            transposed = [''.join(s) for s in zip(*pattern)]
            v = find_horizontal_mirror(transposed, 1)
            for t in v:
                if t[1] == 'new':
                    # found it
                    found = True
                    tmp = t[0]
                    break
                else:
                    # keep the old value
                    tmp = t[0]
        res += tmp
    return res

# parsing and execution
with open(path) as f:
    input = [line.splitlines() for line in f.read().split("\n\n")]

    print_blue(part_1())
    print(f"Completed {YEAR}-{DAY} PART 1 in {(time.time() - start_time) * 1000} ms\n")

    start_time = time.time()
    print_purple(part_2())
    print(f"Completed {YEAR}-{DAY} PART 2 in {(time.time() - start_time) * 1000} ms")