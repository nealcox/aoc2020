import re
import sys
from collections import defaultdict
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

    answer = None
    program = parse(input_text)
    acc = 0
    pc = 0
    seen = []
    finished = False

    while not finished:
        seen.append(pc)
        ins, val = program[pc]
        if ins == "nop":
            pc += 1
        elif ins == "acc":
            acc += val[0]
            pc += 1
        elif ins == "jmp":
            pc += val[0]
        else:
            ValueError(f"Bad instruction at position {pc}: {ins} {v}")
        if pc in seen:
            finished = True
    return acc


def parse(s):
    given = []
    for line in s.split("\n"):
        print(line)
        words = line.split()
        ins = words[0]
        vals = []
        for v in words[1:]:
            try:
                vals.append(int(v))
            except ValueError:
                vals.append(v)
        given.append((ins, tuple(vals)))
    return given


if __name__ == "__main__":
    exit(main())
