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
    joltage = 0
    diffs = defaultdict(int)
    for ad in adapters:
        diff = ad - joltage
        if diff > 3:
            raise ValueError(f"Cannot jump from {joltage} to {ad}")
        diffs[diff] += 1
        joltage += diff
    # now add final diff to device
    diffs[3] += 1

    return diffs[1] * diffs[3]


def get_nums(s):
    given = []
    for line in s.split("\n"):
        given.append(int(line))
    return given


if __name__ == "__main__":
    exit(main())
