import time
from utils import print_blue, print_purple, download_input
import os.path
from collections import Counter

# setup
YEAR = 2023
DAY = 7
start_time = time.time()
path = f"./inputs/{YEAR}_{DAY}.txt"

if not os.path.isfile(path):
    download_input(YEAR, DAY)

# common
def parse_input():
    hands = {}
    for line in input:
        hands[line.split()[0]] = int(line.split()[1])
    return hands

def get_hand_score(hand, part):
    freq = Counter(hand)
    j_count = freq['J']
    
    if part == 2 and j_count != 0:
        freq['J'] = 0
        most_common_char, most_common_count = freq.most_common(1)[0]
        new_count = most_common_count + j_count
        freq[most_common_char] = new_count

    count = freq.values()
    if 5 in count:
        # five of a kind
        return 7
    if 4 in count:
        # four of a kind
        return 6
    if 3 in count:
        if 2 in count:
            # full house
            return 5
        else:
            # three of a kind
            return 4
    if 2 in count:
        if len(count) == 3 or (len(count) == 4 and j_count != 0):
            # two couple
            return 3 
        else:
            # one couple
            return 2 
    # high card
    return 1

def split_by_score(part):
    splits = [ [] for _ in range(7) ]
    for hand in hands.keys():
        score = get_hand_score(hand, part)
        splits[score-1].append(hand)
    return splits

def calculate_points(all_hands_by_score, part):
    res = 0
    ranked_hands = []
    for hands_by_score in all_hands_by_score:
        hands_by_score.sort(key=lambda h:solve_tie(h, part))
        ranked_hands += hands_by_score
    for rank, hand in enumerate(ranked_hands):
        res += (rank + 1) * hands[hand]
    return res

def solve_tie(hand, part):
    if part == 1:
        return [cards_1.get(h, 0) for h in hand]
    return [cards_2.get(h, 0) for h in hand]

# part 1
cards_1 = {'A': 13, 'K': 12, 'Q': 11, 'J': 10, 'T': 9, '9': 8, '8': 7, '7': 6, '6': 5, '5': 4, '4': 3, '3': 2, '2': 1}

def part_1():
    all_hands_by_score = split_by_score(1)
    return calculate_points(all_hands_by_score, 1)

# part 2
cards_2 = {'A': 13, 'K': 12, 'Q': 11, 'J': 0, 'T': 9, '9': 8, '8': 7, '7': 6, '6': 5, '5': 4, '4': 3, '3': 2, '2': 1}

def part_2():
    all_hands_by_score = split_by_score(2)
    return calculate_points(all_hands_by_score, 2)

# parsing and execution
with open(path) as f:
    input = (f.read().splitlines())

    hands = parse_input()

    print_blue(part_1())
    print(f"Completed {YEAR}-{DAY} PART 1 in {time.time() - start_time} s\n")

    start_time = time.time()
    print_purple(part_2())
    print(f"Completed {YEAR}-{DAY} PART 2 in {time.time() - start_time} s")