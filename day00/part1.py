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
    given = parse(input_text)
    print(given)

    return answer


def parse(s):
    given = None
    # given = partlines(s)
    given = get_nums(s)
    return given


def partlines(s):
    given = []
    for line in s.split("\n"):
        line = line.strip()
        given.append(line)
    return given


def get_nums(s):
    given = []
    r = re.compile("(\d+)")
    for line in s.split("\n"):
        ints = []
        for i in r.findall(line):
            ints.append(int(i))
        given.append(ints)
    return given


if __name__ == "__main__":
    exit(main())
