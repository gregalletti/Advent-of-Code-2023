import re
import time

YEAR = 2023
DAY = 5
start_time = time.time()

# part 1
with open(f"./inputs/{YEAR}_{DAY}.txt" ) as f:
    input = (f.read().splitlines())
    res = 0
    print(f"{YEAR} {DAY} part 1 Result: {res} in {time.time() - start_time} s")

# part 2
with open(f"./inputs/{YEAR}_{DAY}.txt" ) as f:
    input = (f.read().splitlines())
    res = 0
    print(f"{YEAR} {DAY} part 2 Result: {res} in {time.time() - start_time} s")