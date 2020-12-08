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

    program = parse(input_text)
    finished = False
    l = len(program)
    for i, (ins, v) in enumerate(program):
        print(f"{i} / {l} ({int((i*100)/l)}%)\033[20D\033[1A")
        attempted = program[:]
        if ins == "nop":
            attempted[i] = ("jmp", v)
            acc, looped = run(attempted)
        elif ins == "jmp":
            attempted[i] = ("nop", v)
            acc, looped = run(attempted)
        elif ins == "acc":
            looped = True
        else:
            raise ValueError
        if not looped:
            print()
            return acc
    return "No answer found"


def run(program):
    acc = 0
    pc = 0
    seen = []
    finished = False
    looped = False

    while not finished:
        seen.append(pc)
        ins, val = program[pc]
        if ins == "nop":
            pc += 1
        elif ins == "acc":
            acc += val
            pc += 1
        elif ins == "jmp":
            pc += val
        else:
            ValueError(f"Bad instruction at position {pc}: {ins} {v}")
        if pc in seen:
            looped = True
            finished = True
        if pc >= len(program):
            finished = True

    return acc, looped


def parse(s):
    r = re.compile(r"(\w+) ([+-]\d+)")
    given = []
    for ins, v in r.findall(s):
        given.append((ins, int(v)))
    return given


if __name__ == "__main__":
    exit(main())
