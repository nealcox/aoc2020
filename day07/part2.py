import re
import sys
from collections import defaultdict


def main():
    if len(sys.argv) > 1:
        filename = sys.argv[1]
    else:
        filename = "input.txt"
    with open(filename) as f:
        input_text = f.read().strip()
    print(f"Answer: {calculate(input_text)}")


def calculate(input_text):
    holders = parse(input_text)
    my_bag = "shiny gold"
    return recursive(holders, my_bag)


def recursive(holders, bt):
    holds = 0
    for bags in holders[bt]:
        holds += bags[0] * (1 + recursive(holders, bags[1]))
    return holds


def parse(s):
    r = re.compile(r"(\d) (\w+ \w+) bag")
    holders = defaultdict(set)
    for line in s.split("\n"):
        holder = re.match(r"^(\w+ \w+)", line).group()
        holdees = r.findall(line)
        for bt in holdees:
            num_n_type = (int(bt[0]), bt[1])
            holders[holder].add((int(bt[0]), bt[1]))
    return holders


if __name__ == "__main__":
    exit(main())
