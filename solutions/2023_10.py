import time
from utils import print_blue, print_purple, download_input
import os.path
import numpy as np

# setup
YEAR = 2023
DAY = 10
start_time = time.time()
path = f"./inputs/{YEAR}_{DAY}.txt"

if not os.path.isfile(path):
    download_input(YEAR, DAY)

# common
moves = {
    "|": "UD",
    "-": "LR",
    "L": "UR",
    "J": "UL",
    "7": "DL",
    "F": "DR",
    'S': "UDLR",
}

directions = {
    "U": (-1, 0),
    "D": (1, 0),
    "L": (0, -1),
    "R": (0, 1),
}

def parse_input(input):
    m = [[cell for cell in row] for row in input]
    r = len(m)
    c = len(m[0])
    return m, r, c

def get_start():
    for i in range(rows):
        for j in range(cols):
            place = maze[i][j]
            if place == 'S':
                return (i, j)

def make_move(curr, direction):
    r, c = directions[direction]
    next_r, next_c = curr[0] + r, curr[1] + c
    if next_r >= 0 and next_r < len(maze):
        if next_c >= 0 or next_c < len(maze[i + r]):
            if maze[next_r][next_c] in moves:
                next = (next_r, next_c)
                return next, moves[maze[next_r][next_c]]
    return None, None

def get_opposite(dir):
    if dir == 'U': return 'D'
    if dir == 'D': return 'U'
    if dir == 'L': return 'R'
    return 'L'

# part 1
def part_1():
    v = {}
    q = [ (start, 0) ]
    while q:
        curr, distance = q.pop(0)
        if curr in v:
            continue
        v[curr] = distance
        for dir in moves[maze[curr[0]][curr[1]]]:
            next, next_dirs = make_move(curr, dir)
            if not next:
                continue
            if get_opposite(dir) in next_dirs:
                q.append((next, distance + 1))
    return max(v.values())

# part 2
def shoelace_formula(path):
    x, y = zip(*path)
    return 0.5 * abs(
        sum(x[i] * y[i - 1] - x[i - 1] * y[i] for i in range(len(path)))
    )

def pick_theorem(a, b):
    return int(a - b / 2 + 1)

def part_2():
    v = {}
    q = [ (start, 0) ]
    while q:
        curr, distance = q.pop(0)
        if curr in v:
            continue
        v[curr] = distance
        for dir in moves[maze[curr[0]][curr[1]]]:
            next, next_dirs = make_move(curr, dir)
            if not next:
                continue
            if get_opposite(dir) in next_dirs:
                q.append((next, distance + 1))
    # v is now the list of nodes of the loop
    loop = list(v.keys())
    area = shoelace_formula(loop)
    return pick_theorem(area, len(loop))

# parsing and execution
with open(path) as f:
    input = (f.read().splitlines())

    maze, rows, cols = parse_input(input)

    start = get_start()

    print_blue(part_1())
    print(f"Completed {YEAR}-{DAY} PART 1 in {time.time() - start_time} s\n")

    start_time = time.time()
    print_purple(part_2())
    print(f"Completed {YEAR}-{DAY} PART 2 in {time.time() - start_time} s")