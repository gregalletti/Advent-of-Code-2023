import time
from utils import print_1, print_2, download_input

YEAR = 2023
DAY = 1
start_time = time.time()
download_input(YEAR, DAY)

# part 1
with open(f"./inputs/{YEAR}_{DAY}.txt" ) as f:
    input = (f.read().splitlines())
    res = 0
    # code goes here

    print(f"{YEAR}-{DAY} PART 1 in {time.time() - start_time} s")
    print_1(res)
    
# part 2
with open(f"./inputs/{YEAR}_{DAY}.txt" ) as f:
    input = (f.read().splitlines())
    res = 0
    # code goes here

    print(f"{YEAR}-{DAY} PART 2 in {time.time() - start_time} s")
    print_2(res)