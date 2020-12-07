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
    to_check = []
    to_check.append(my_bag)
    can_hold_gold = set()
    while to_check:
        checking = to_check.pop()
        can_hold_gold.add(checking)
        for bt in holders[checking]:
            if bt not in can_hold_gold:
                to_check.append(bt)
    can_hold_gold.remove(my_bag)
    return len(can_hold_gold)


def parse(s):
    r = re.compile(r"\d (\w+ \w+) bag")
    holders = defaultdict(set)
    for line in s.split("\n"):
        holder = re.match(r"^(\w+ \w+)", line).group()
        holdees = r.findall(line)
        for bt in holdees:
            holders[bt].add(holder)
    return holders


if __name__ == "__main__":
    exit(main())
