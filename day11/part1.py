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

    given = parselines(input_text)
    rows = len(given)
    cols = len(given[0])
    print(given)
    layout = defaultdict(str)
    for r in range(len(given)):
        for c in range(len(given[0])):
            layout[r, c] = given[r][c]

    rounds = 0
    changed = True
    while changed:
        new_layout = defaultdict(str)
        changed = False
        rounds += 1
        for r in range(rows):
            for c in range(cols):
                if layout[r, c] == "L" and occupied(r, c, layout) == 0:
                    changed = True
                    new_layout[r, c] = "#"
                elif layout[r, c] == "#" and occupied(r, c, layout) >= 4:
                    changed = True
                    new_layout[r, c] = "L"
                else:
                    new_layout[r, c] = layout[r, c]
        layout = new_layout
        print(rounds)
        pprint(layout, rows, cols)
    return sum(1 for s in layout.values() if s == "#")


def pprint(layout, rows, cols):
    for r in range(rows):
        for c in range(cols):
            print(layout[r, c], end="")
        print()
    print()


def occupied(r, c, layout):
    occu = 0
    for dx in range(-1, 2):
        for dy in range(-1, 2):
            if dx != 0 or dy != 0:
                if layout[r + dy, c + dx] == "#":
                    occu += 1
    return occu


def parselines(s):
    given = []
    for line in s.split("\n"):
        line = [c for c in line.strip()]
        given.append(line)
    return given


if __name__ == "__main__":
    exit(main())
