import re
import math
import time
from utils import print_1, print_2

YEAR = 2023
DAY = 2
start_time = time.time()

# part 1
bag = {'red': 12, 'green': 13, 'blue': 14}

with open(f"./inputs/{YEAR}_{DAY}.txt" ) as f:
    input = (f.read().splitlines())
    res = 0
    for line in input:
        ok = True
        game_num = int(re.findall("Game ([0-9]+)", line)[0])
        for color in bag:
            max_color = max([int(x) for x in re.findall(f"([0-9]+) {color}", line)])
            if max_color > bag[color]:
                ok = False
        if ok:        
            res += game_num
    print(f"{YEAR}-{DAY} PART 1 in {time.time() - start_time} s")
    print_1(res)

# part 2
bag = ['red', 'green', 'blue']

with open(f"./inputs/{YEAR}_{DAY}.txt" ) as f:
    input = (f.read().splitlines())
    res = 0
    for line in input:
        game = {}
        for color in bag:
            game[color] = max([int(x) for x in re.findall(f"([0-9]+) {color}", line)])
        res += math.prod(game.values())
    print(f"{YEAR}-{DAY} PART 2 in {time.time() - start_time} s")
    print_2(res)