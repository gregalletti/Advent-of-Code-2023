import time
from utils import print_blue, print_purple, download_input
import os.path

# setup
YEAR = 2023
DAY = 5
start_time = time.time()
path = f"./inputs/{YEAR}_{DAY}.txt"

if not os.path.isfile(path):
    download_input(YEAR, DAY)

# common
def common_function():
    pass

# part 1
def part_1():
    pass

# part 2
def part_2():
    pass

# parsing and execution
with open(path) as f:
    input = (f.read().splitlines())
    
    print_blue(part_1())
    print(f"Completed {YEAR}-{DAY} PART 1 in {time.time() - start_time} s\n")

    print_purple(part_2())
    print(f"Completed {YEAR}-{DAY} PART 2 in {time.time() - start_time} s")