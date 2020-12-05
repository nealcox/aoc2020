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
    given = []
    for line in s:
        line = line.strip().split(" ")
        given.append(line)
    return given


if __name__ == "__main__":
    exit(main())
