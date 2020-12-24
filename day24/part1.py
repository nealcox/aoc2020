import sys
from collections import defaultdict
from fractions import Fraction


def main():
    if len(sys.argv) > 1:
        filename = sys.argv[1]
    else:
        filename = "input.txt"
    with open(filename) as f:
        input_text = f.read().strip()
    print(f"Answer: {calculate(input_text)}")


HALF = Fraction(1, 2)
WHITE = False
BLACK = True

deltas = {
    "e": (1, 0),
    "w": (-1, 0),
    "se": (HALF, -1),
    "sw": (-HALF, -1),
    "ne": (HALF, 1),
    "nw": (-HALF, 1),
}


def calculate(input_text):
    lines = input_text.strip().split("\n")
    tiles = defaultdict(bool)
    for line in lines:
        x, y = 0, 0
        i = 0
        while i < len(line):
            move = line[i]
            if move == "s" or move == "n":
                i += 1
                move += line[i]
            x += deltas[move][0]
            y += deltas[move][1]
            i += 1
        tiles[x, y] = not tiles[x, y]

    return sum(tiles.values())


if __name__ == "__main__":
    exit(main())
