import re
import sys
from collections import defaultdict
from functools import lru_cache
from itertools import permutations


def main():
    if len(sys.argv) > 1:
        filename = sys.argv[1]
    else:
        filename = "input.txt"
    with open(filename) as f:
        input_text = f.read().strip()
    print(f"Answer: {calculate(input_text)}")


def calculate(input_text):
    def expand(rule_num):
        rule = rules[rule_num]
        if rule.startswith('"'):
            return rule.strip('"')
        else:
            parts = rule.split()
            reg = "".join("|" if part == "|" else expand(part) for part in parts)
            return f"({reg})"

    rules = defaultdict(list)
    rules_s, messages = input_text.split("\n\n")
    for i, rule in enumerate(rules_s.split("\n")):
        rule_num, rule_def = rule.split(": ")
        rules[rule_num] = rule_def

    # 8: 42 | 42 8            ie one or more (42)
    # 11: 42 31 | 42 11 31    ie one or more (42) and same number of (31)
    # rule 0
    # 0: 8 11
    reg_42 = re.compile(expand("42"))
    reg_31 = re.compile(expand("31"))
    num_matches = 0
    for message in messages.split("\n"):
        pos = 0
        num42s = 0
        num31s = 0
        match = reg_42.match(message, pos)
        while match:
            num42s += 1
            pos = match.end()
            match = reg_42.match(message, pos)
        match = reg_31.match(message, pos)
        while match:
            num31s += 1
            pos = match.end()
            match = reg_31.match(message, pos)

        if pos == len(message) and num42s > num31s > 0:
            print(message)
            num_matches += 1
    return num_matches


if __name__ == "__main__":
    exit(main())
