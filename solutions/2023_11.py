import time
from utils import print_blue, print_purple, download_input
import os.path
from itertools import combinations

# setup
YEAR = 2023
DAY = 11
start_time = time.time()
path = f"./inputs/{YEAR}_{DAY}.txt"

if not os.path.isfile(path):
    download_input(YEAR, DAY)

# common
def parse_input():
    global rows_to_expand, cols_to_expand
    rows_to_expand = [i for i, row in enumerate(input) if '#' not in row]
    cols_to_expand = [x for x, col in enumerate(zip(*input)) if '#' not in col]

def get_expanded_coordinates(pos, e):
    empty_cols = sum([1 for col in cols_to_expand if col < pos[0]])
    empty_rows = sum([1 for row in rows_to_expand if row < pos[1]])
    return (pos[0] + empty_cols * (e - 1), pos[1] + empty_rows * (e - 1))

def manhattan_distance(start, end):
    return abs(start[0] - end[0]) + abs(start[1] - end[1])

def get_shortest_paths(e):
    galaxies = []
    for r, row in enumerate(input):
        for c, char in enumerate(row):
            if char == '#':
                rr, cc = get_expanded_coordinates((r, c), e)
                galaxies.append((rr, cc))

    shortest_paths = [manhattan_distance(g1, g2) for g1, g2 in combinations(galaxies, 2)]
    return sum(shortest_paths)

# part 1
def part_1():
    exp = 2
    return get_shortest_paths(exp)

# part 2 - just change the expansion
def part_2():
    exp = 10e6
    return int(get_shortest_paths(exp))

# parsing and execution
with open(path) as f:
    input = (f.read().splitlines())
    
    parse_input()

    print_blue(part_1())
    print(f"Completed {YEAR}-{DAY} PART 1 in {time.time() - start_time} s\n")

    start_time = time.time()
    print_purple(part_2())
    print(f"Completed {YEAR}-{DAY} PART 2 in {time.time() - start_time} s")