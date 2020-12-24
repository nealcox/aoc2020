import re
import sys
from collections import deque
from itertools import permutations


TURNS = 100


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
    cups = [int(c) for c in input_text.strip()]
    current = 0
    l = len(cups)
    for turn in range(1, TURNS + 1):
        current_cup = cups[current]
        if current > l - 4:
            cups = cups[current:] + cups[:current]
            current = 0
        picked = cups[current + 1 : current + 4]
        cups = cups[: current + 1] + cups[current + 4 :]
        destination = cups[current] - 1
        if destination < 1:
            destination = max(cups)
        while destination in picked:
            destination -= 1
            if destination < 1:
                destination = max(cups)
        idx = cups.index(destination)
        cups = cups[: idx + 1] + picked + cups[idx + 1 :]
        current = (cups.index(current_cup) + 1) % l

    idx = cups.index(1)
    cups = cups[idx + 1 :] + cups[:idx]
    answer = "".join(str(cup) for cup in cups)

    return answer


if __name__ == "__main__":
    exit(main())
