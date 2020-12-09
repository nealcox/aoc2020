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
    adapters = sorted(get_nums(input_text))
    joltages = [0] + adapters + [adapters[-1] + 3]
    # The number of ways to get to n is the sum of the ways to get to
    # n-3, n-2 and n-1 (if they are in the list).
    ways = defaultdict(int)
    ways[0] = 1  # only one way to start
    for j in joltages:
        for prev in range(j - 3, j):
            ways[j] += ways[prev]
    return ways[joltages[-1]]


def get_nums(s):
    given = []
    for line in s.split("\n"):
        given.append(int(line))
    return given


if __name__ == "__main__":
    exit(main())
