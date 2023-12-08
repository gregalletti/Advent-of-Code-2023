import time
from utils import print_blue, print_purple, download_input
import os.path
import re

# setup
YEAR = 2023
DAY = 6
start_time = time.time()
path = f"./inputs/{YEAR}_{DAY}.txt"

if not os.path.isfile(path):
    download_input(YEAR, DAY)

# common
def compute_results(t, d):
    for hold_time in range(t):
        race_dist = hold_time * (t - hold_time)
        if race_dist > d:
            left = hold_time
            break
    for hold_time in range(t, 0, -1):
        race_dist = hold_time * (t - hold_time)
        if race_dist > d:
            right = hold_time
            break
    return right - left + 1

# part 1
def part_1():
    res = 1
    race_times = [int(x) for x in re.findall(f"([0-9]+)", input[0])]
    race_distances = [int(x) for x in re.findall(f"([0-9]+)", input[1])]
    for i in range(len(race_times)):
        res *= compute_results(race_times[i], race_distances[i])
    return res

# part 2
def part_2():
    res = 0
    race_time = int("".join([x for x in re.findall(f"([0-9]+)", input[0])]))
    race_distance = int("".join([x for x in re.findall(f"([0-9]+)", input[1])]))
    res = compute_results(race_time, race_distance)
    return res

# parsing and execution
with open(path) as f:
    input = (f.read().splitlines())
    
    print_blue(part_1())
    print(f"Completed {YEAR}-{DAY} PART 1 in {time.time() - start_time} s\n")

    start_time = time.time()
    print_purple(part_2())
    print(f"Completed {YEAR}-{DAY} PART 2 in {time.time() - start_time} s")