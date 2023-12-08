import time
from utils import print_blue, print_purple, download_input
import os.path
import re
import math

# setup
YEAR = 2023
DAY = 8
start_time = time.time()
path = f"./inputs/{YEAR}_{DAY}.txt"

if not os.path.isfile(path):
    download_input(YEAR, DAY)
    
# part 1
def part_1(start_node):
    # just simulate
    res = 0
    current_node = start_node
    ins = instructions
    # only because we know it's not endless
    while True:
        current_node = nodes[current_node][0] if ins[res] == 'L' else nodes[current_node][1]
        res += 1
        if res == len(ins):
            ins += instructions
        if current_node[-1] == 'Z':
            return res
        
# part 2
def part_2():
    # just simulate
    res = []
    current_nodes = [node for node in nodes.keys() if node[-1] == 'A']
    # only because we know it's not endless
    for node in current_nodes:
        res.append(part_1(node))
    return math.lcm(*res)

# parsing and execution
with open(path) as f:
    input = (f.read().splitlines())
    
    instructions = input[0]
    nodes = {}
    for line in input[2:]:
        line_split = re.findall(f"([A-Za-z]+)", line)
        nodes[line_split[0]] = line_split[1:]

    print_blue(part_1('AAA'))
    print(f"Completed {YEAR}-{DAY} PART 1 in {time.time() - start_time} s\n")

    start_time = time.time()
    print_purple(part_2())
    print(f"Completed {YEAR}-{DAY} PART 2 in {time.time() - start_time} s")