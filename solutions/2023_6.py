import time
from utils import print_1, print_2, download_input
import os.path
import re

YEAR = 2023
DAY = 6
start_time = time.time()
path = f"./inputs/{YEAR}_{DAY}.txt"

if not os.path.isfile(path):
    download_input(YEAR, DAY)

# part 1
def compute_results(t, d):
    wins = 0
    for hold_time in range(t):
        race_dist = hold_time * (t - hold_time)
        if race_dist > d:
            wins += 1
    return wins 

with open(path) as f:
    input = (f.read().splitlines())
    res = 1
    race_times = [int(x) for x in re.findall(f"([0-9]+)", input[0])]
    race_distances = [int(x) for x in re.findall(f"([0-9]+)", input[1])]
    for i in range(len(race_times)):
        res *= compute_results(race_times[i], race_distances[i])
    print(f"{YEAR}-{DAY} PART 1 in {time.time() - start_time} s")
    print_1(res)

# part 2
def compute_results_better(t, d):
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

with open(path) as f:
    input = (f.read().splitlines())
    res = 0
    race_time = int("".join([x for x in re.findall(f"([0-9]+)", input[0])]))
    race_distance = int("".join([x for x in re.findall(f"([0-9]+)", input[1])]))
    res = compute_results_better(race_time, race_distance)
    print(f"{YEAR}-{DAY} PART 2 in {time.time() - start_time} s")
    print_2(res)