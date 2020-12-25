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
    def expand(rule):
        if rule.startswith('"'):
            return rule.strip('"')
        else:
            parts = rule.split()
            reg = "".join("|" if part == "|" else expand(rules[part]) for part in parts)
            return f"({reg})"

    rules = defaultdict(list)
    rules_s, messages = input_text.split("\n\n")
    for i, rule in enumerate(rules_s.split("\n")):
        rule_num, rule_def = rule.split(": ")
        rules[rule_num] = rule_def

    rule0 = expand(rules["0"])
    print(rule0)
    reg0 = re.compile(rule0)

    num_matches = 0
    for message in messages.split("\n"):
        if reg0.fullmatch(message):
            num_matches += 1
    return num_matches


if __name__ == "__main__":
    exit(main())
