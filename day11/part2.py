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
    layout = to_dict(given)

    rounds = 0
    changed = True
    while changed:
        new_layout = defaultdict(lambda: "L")
        changed = False
        rounds += 1
        for r in range(rows):
            for c in range(cols):
                if layout[r, c] == "L" and occupied(r, c, layout) == 0:
                    changed = True
                    new_layout[r, c] = "#"
                elif layout[r, c] == "#" and occupied(r, c, layout) >= 5:
                    changed = True
                    new_layout[r, c] = "L"
                else:
                    new_layout[r, c] = layout[r, c]
        layout = new_layout
        print(rounds)
        pprint(layout, rows, cols)
    occ = 0
    for seat in layout.values():
        if seat == "#":
            occ += 1

    return occ


def pprint(layout, rows, cols):
    for r in range(rows):
        for c in range(cols):
            print(layout[r, c], end="")
        print()
    print()


def occupied(r0, c0, layout):
    occu = 0
    for dx in range(-1, 2):
        for dy in range(-1, 2):
            if dx != 0 or dy != 0:
                r = r0 + dy
                c = c0 + dx
                s = layout[r, c]
                while s not in "L#":
                    r = r + dy
                    c = c + dx
                    s = layout[r, c]

                if s == "#":
                    occu += 1
    return occu


def to_dict(l):
    layout = defaultdict(lambda: "L")
    for r in range(len(l)):
        for c in range(len(l[0])):
            layout[r, c] = l[r][c]
    return layout


def parselines(s):
    given = []
    for line in s.split("\n"):
        line = [c for c in line.strip()]
        given.append(line)
    return given


if __name__ == "__main__":
    exit(main())
