import re
import time
from utils import print_1, print_2

YEAR = 2023
DAY = 3
start_time = time.time()

def get_directions(row, start, end, max_row, max_col):
    dirs = []
    # left
    if start > 0:
        start -= 1
        dirs.append((row, start))
    # right
    if end < max_col:
        end += 1
        dirs.append((row, end))
    # up
    if row > 0:
        for i in range(start, end+1):
            dirs.append((row-1,i))
    # down
    if row < max_row:
        for i in range(start, end + 1):
            dirs.append((row+1,i))
    return dirs

# part 1
def check_part(directions):
    for (r, c) in directions:
        cell = input[r][c]
        if not cell.isalnum() and cell != '.':
            return True
    return False

with open(f"./inputs/{YEAR}_{DAY}.txt") as f:
    input = (f.read().splitlines())
    res = 0
    for row, line in enumerate(input):
        numbers = re.findall("([0-9]+)", line)
        for n in numbers:
            start = line.find(n)
            end = start + len(n) - 1
            directions = get_directions(row, start, end, len(input) - 2, len(line) - 1)
            if check_part(directions):
                res += int(n)
            line = line.replace(n, '.' * len(n), 1)
    print(f"{YEAR}-{DAY} PART 1 in {time.time() - start_time} s")
    print_1(res)

# part 2
def check_gear(directions, n):
    for (r, c) in directions:
        cell = input[r][c]
        if cell == '*':
            return (r, c)
    return None

with open(f"./inputs/{YEAR}_{DAY}.txt") as f:
    input = (f.read().splitlines())
    res = 0
    gears = {}
    for row, line in enumerate(input):
        numbers = re.findall("([0-9]+)", line)
        for n in numbers:
            start = line.find(n)
            end = start + len(n) - 1
            directions = get_directions(row, start, end, len(input) - 2, len(line) - 1)
            g = check_gear(directions, n)
            if g:
                if g in gears:
                    gears[g].append(int(n))
                else:
                    gears[g] = [int(n)]
            line = line.replace(n, '.' * len(n), 1)
    for k in gears:
        if len(gears[k]) == 2:
            res += gears[k][0] * gears[k][1]
    print(f"{YEAR}-{DAY} PART 2 in {time.time() - start_time} s")
    print_2(res)