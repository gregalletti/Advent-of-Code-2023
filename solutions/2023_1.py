import time
from utils import print_1, print_2

YEAR = 2023
DAY = 1
start_time = time.time()

# part 1
numbers = {'1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}

with open(f"./inputs/{YEAR}_{DAY}.txt" ) as f:
    input = (f.read().splitlines())
    res = 0
    left = ""
    right = ""
    for line in input:
        calibration = 0
        for i in range(0, len(line)):
            for j in range(i, len(line)):
                if line[i:j+1] in numbers:
                    if not left:
                        left = line[i:j+1]
                    right = line[i:j+1]
        calibration = numbers[left] * 10 + numbers[right]
        left = ""
        res += calibration
    print(f"{YEAR}-{DAY} PART 1 in {time.time() - start_time} s")
    print_1(res)

# part 2 - just change the dict
numbers = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}

with open(f"./inputs/{YEAR}_{DAY}.txt" ) as f:
    input = (f.read().splitlines())
    res = 0
    left = ""
    right = ""
    for line in input:
        calibration = 0
        for i in range(0, len(line)):
            for j in range(i, len(line)):
                if line[i:j+1] in numbers:
                    if not left:
                        left = line[i:j+1]
                    right = line[i:j+1]
        calibration = numbers[left] * 10 + numbers[right]
        left = ""
        res += calibration
    print(f"{YEAR}-{DAY} PART 2 in {time.time() - start_time} s")
    print_2(res)