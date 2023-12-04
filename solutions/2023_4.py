import re
import time
from utils import print_1, print_2

YEAR = 2023
DAY = 4
start_time = time.time()

# part 1
with open(f"./inputs/{YEAR}_{DAY}.txt" ) as f:
    input = (f.read().splitlines())
    res = 0
    for line in input:
        score = 0
        winning = [int(s) for s in re.findall('([0-9]+)', line.split("|")[0])][1:]
        card = [int(s) for s in re.findall('([0-9]+)', line.split("|")[1])]
        for w in winning:
            if w in card:
                if score:
                    score *= 2 
                else:
                    score = 1
        res += score
    print(f"{YEAR}-{DAY} PART 1 in {time.time() - start_time} s")
    print_1(res)

# part 2
with open(f"./inputs/{YEAR}_{DAY}.txt" ) as f:
    input = (f.read().splitlines())
    counter = [1] * len(input)
    for i,line in enumerate(input):
        score = 0
        winning = [int(s) for s in re.findall('([0-9]+)', line.split("|")[0])][1:]
        card = [int(s) for s in re.findall('([0-9]+)', line.split("|")[1])]
        for w in winning:
            if w in card:
                score += 1 
        for j in range(i+1, i+score+1):
            counter[j] += counter[i]
    res = sum(counter)
    print(f"{YEAR}-{DAY} PART 2 in {time.time() - start_time} s")
    print_2(res)