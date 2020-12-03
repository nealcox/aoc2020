import sys
from collections import defaultdict
from itertools import permutations


def main():
    if len(sys.argv) > 1:
        input_file = sys.argv[1]
    else:
        input_file = "input.txt"
    given = setup(input_file)
    print(f"Answer: {run(given)}")


def run(forest):
    cols = len(forest[0])
    r, c = 0, 0
    num_trees = 0
    while True:
        r = r + 1
        c = c + 3
        if r >= len(forest):
            break
        if forest[r][c % cols] == "#":
            num_trees += 1
    return num_trees


def setup(filename):
    given = []
    with open(filename) as f:
        for line in f:
            given.append(line.strip())
    return given


if __name__ == "__main__":
    exit(main())
