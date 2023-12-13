import requests

# styles for print
class bcolors:
    OKPURPLE = '\033[95m'
    OKCYAN = '\033[96m'
    ENDC = '\033[0m'

# session cookie taken from browser after login
SESSION = "53616c7465645f5ffd1d7d3ce20554591df277d338f8d21ad58bdcd23568e106c0db3c5e5d98a2316664e5bd6c8f6bede2d1e29a58fd3c77af65d47f13fd0d6e"

def download_input(year, day):
    url = f"https://adventofcode.com/{year}/day/{day}/input"
    r = requests.get(url, cookies={'session': SESSION})
    with open(f"./inputs/{year}_{day}.txt", "w" ) as f:
        f.write(r.text)

def print_blue(text):
    print(f"{bcolors.OKCYAN}{text}{bcolors.ENDC}")

def print_purple(text):
    print(f"{bcolors.OKPURPLE}{text}{bcolors.ENDC}")

def create_solution():
    YEAR = 2023
    DAY = 13
    path = f"./solutions/{YEAR}_{DAY}.py"
    with open(path, "w") as f:
        f.write("")

# create_solution()