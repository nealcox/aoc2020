import re
import sys
from collections import deque
from itertools import permutations


TURNS = 10_000_000
NUM_CUPS = 1_000_000


def main():
    if len(sys.argv) > 1:
        filename = sys.argv[1]
    else:
        filename = "input.txt"
    with open(filename) as f:
        input_text = f.read().strip()
    print(f"Answer: {calculate(input_text)}")


def get_cups(input_text):
    input_text = input_text.strip()
    for i in range(NUM_CUPS):
        if i < len(input_text):
            this_cup = int(input_text[i])
        else:
            this_cup = next_cup
        if i < len(input_text) - 1:
            next_cup = int(input_text[(i + 1)])
        elif i < NUM_CUPS - 1:
            next_cup = (i + 1) % NUM_CUPS + 1
        else:
            next_cup = int(input_text[0])
        yield this_cup, next_cup


def calculate(input_text):

    cups = {}
    current = None
    for cup, next_cup in get_cups(input_text.strip()):
        cups[cup] = next_cup
        if not current:
            current = cup
    max_cup = max(cups)
    num_cups = len(cups)
    for i in range(1, TURNS + 1):
        next_three = [cups[current]]
        for _ in range(2):
            next_three.append(cups[next_three[-1]])
        destination = current - 1
        if destination not in cups:
            destination = max_cup
        while destination in next_three:
            destination -= 1
            if destination not in cups.keys():
                destination = max_cup
        cups[current] = cups[next_three[-1]]
        cups[next_three[-1]] = cups[destination]
        cups[destination] = next_three[0]
        current = cups[current]

    first = cups[1]
    second = cups[first]
    return first * second


if __name__ == "__main__":
    exit(main())
