import time
from utils import print_blue, print_purple, download_input
import os.path

# setup
YEAR = 2023
DAY = 9
start_time = time.time()
path = f"./inputs/{YEAR}_{DAY}.txt"

if not os.path.isfile(path):
    download_input(YEAR, DAY)

# common
def parse_input(input):
    seq = []
    for line in input:
        seq.append([int(s) for s in line.split()])
    return seq

# part 1
def get_sequence_value(sequence):
    seq = sequence
    last_nums = [seq[-1]]
    while not all([ v == 0 for v in seq ]):
        seq = [j-i for i,j in zip(seq, seq[1:])]
        last_nums.append(seq[-1])
    return sum(last_nums)

def part_1():
    res = 0
    for seq in sequences:
        res += get_sequence_value(seq)
    return res

# part 2
def diff(list):
    res = 0
    for i in range(1, len(list)):
        res = list[i] - res
    return res

def get_sequence_value_p2(sequence):
    seq = sequence
    first_nums = [seq[0]]
    while not all([ v == 0 for v in seq ]):
        seq = [j-i for i,j in zip(seq, seq[1:])]
        first_nums.append(seq[0])
    return diff(first_nums[::-1])

def part_2():
    res = 0
    for seq in sequences:
        res += get_sequence_value_p2(seq)
    return res

# parsing and execution
with open(path) as f:
    input = (f.read().splitlines())
    sequences = parse_input(input)

    print_blue(part_1())
    print(f"Completed {YEAR}-{DAY} PART 1 in {time.time() - start_time} s\n")

    start_time = time.time()
    print_purple(part_2())
    print(f"Completed {YEAR}-{DAY} PART 2 in {time.time() - start_time} s")