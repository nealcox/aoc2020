import sys
from collections import Counter
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
    answer = 0
    given = parse(input_text)
    for group in given:
        c = Counter(group)
        if "\n" in c:
            del c["\n"]
        answer += len(c)
    return answer


def parse(s):
    groups = s.split("\n\n")
    return groups


if __name__ == "__main__":
    exit(main())
