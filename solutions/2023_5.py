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
def parse_input():
    all_maps = []
    lines = [l for l in input if l != '']
    seeds = [int(s) for s in lines[0].split()[1:]]
    for line in lines[1:]:
        if 'map' in line:
            all_maps.append([])
        else:
            all_maps[-1].append([int(l) for l in line.split()])
    return seeds, all_maps

# part 1
def get_mapping(start, maps):
    for map in maps:
        for m in map:
            map_end = m[1] + m[2]
            diff = m[0] - m[1]
            if start >= m[1] and start < map_end:
                start += diff
                break
    return start

def part_1():
    res = []
    for s in seeds:
        res.append(get_mapping(s, all_maps))
    return res

# part 2
def get_mapping_p2(pairs, maps):
    tmp = []
    for map in maps:
        while pairs:
            pair_start, pair_end = pairs.pop()
            for m in map:
                map_end = m[1] + m[2]
                diff = m[0] - m[1]
                if map_end <= pair_start or pair_end <= m[1]:
                    continue
                if pair_start < m[1]:
                    pairs.append([pair_start, m[1]])
                    pair_start = m[1]
                if map_end < pair_end:
                    pairs.append([map_end, pair_end])
                    pair_end = map_end
                tmp.append([pair_start + diff, pair_end + diff])
                break
            else:
                tmp.append([pair_start, pair_end])
        pairs = tmp
        tmp = []
    return pairs

def part_2():
    res = []
    for i in range(0, len(seeds), 2):
        pairs = [[seeds[i], seeds[i + 1] + seeds[i]]]
        res += get_mapping_p2(pairs, all_maps)
    return res

# parsing and execution
with open(path) as f:
    input = (f.read().splitlines())

    seeds, all_maps = parse_input()
    
    print_blue(min(part_1()))
    print(f"Completed {YEAR}-{DAY} PART 1 in {time.time() - start_time} s\n")

    start_time = time.time()
    print_purple(min(r[0] for r in part_2()))
    print(f"Completed {YEAR}-{DAY} PART 2 in {time.time() - start_time} s")