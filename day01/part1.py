import sys
from collections import Counter
from collections import defaultdict
from itertools import permutations


def main():
    if len(sys.argv) > 1:
        input_file = sys.argv[1]
    else:
        input_file = "input.txt"

    given = setup(input_file)
    run(given)


def run(given):
    for i in range(len(given) - 1):
        for j in range(i, len(given)):
            if given[i] + given[j] == 2020:
                print(
                    f"{given[i]} + {given[j]} == 2020, "
                    f"{given[i]} * {given[j]} = {given[i]* given[j]}"
                )


def setup(filename):
    with open(filename) as f:
        given = f.read().strip().split()
    return [int(g) for g in given]


if __name__ == "__main__":
    exit(main())
