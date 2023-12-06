import time
from utils import print_1, print_2, download_input
import os.path

YEAR = 2023
DAY = 5
start_time = time.time()
path = f"./inputs/{YEAR}_{DAY}.txt"

if not os.path.isfile(path):
    download_input(YEAR, DAY)

# part 1


with open(path) as f:
    input = (f.read().splitlines())
    res = 0

    print(f"{YEAR}-{DAY} PART 1 in {time.time() - start_time} s")
    print_1(res)

# part 2


with open(path) as f:
    input = (f.read().splitlines())
    res = 0
    
    print(f"{YEAR}-{DAY} PART 2 in {time.time() - start_time} s")
    print_2(res)