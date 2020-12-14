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
    given = get_re(input_text)
    memory = defaultdict(int)
    for mask in given:
        for mem, val in given[mask]:
            memory[mem] = maskate(mask, val)
    return sum(memory.values())


def maskate(mask, val):
    or_mask = int(mask.replace("X", "0"), base=2)
    and_mask = int(mask.replace("X", "1"), base=2)
    val = val & and_mask
    val = val | or_mask
    return val


def get_re(s):
    given = defaultdict(list)
    r_mem = re.compile(r"(\d+)")
    for line in s.split("\n"):
        if line.startswith("mask"):
            curr_mask = line[7:]
        else:
            vals = r_mem.findall(line)
            given[curr_mask].append((int(vals[0]), int(vals[1])))
    return given


if __name__ == "__main__":
    exit(main())
