import re
import sys


def main():
    if len(sys.argv) > 1:
        filename = sys.argv[1]
        preamble = int(sys.argv[2])
    else:
        filename = "input.txt"
        preamble = 25
    with open(filename) as f:
        input_text = f.read().strip()
    print(f"Answer: {calculate(input_text, preamble)}")


def calculate(input_text, preamble):
    given = get_nums(input_text)
    target = get_sum(given, preamble)
    print(f"Target: {target}")
    for start in range(len(given)):
        test_sum = given[start]
        for stop in range(start + 1, len(given)):
            end_num = given[stop]
            test_sum += end_num
            if test_sum == target:
                return max(given[start : stop + 1]) + min(given[start : stop + 1])
            elif test_sum > target:
                break


def get_sum(given, preamble):
    rest = given[preamble:]
    finished = False
    sums = []
    for i in range(preamble):
        s = []
        for j in range(preamble):
            if i != j:
                s.append(given[i] + given[j])
        sums.append(s)

    for i, n in enumerate(rest):
        found = False
        for x in sums:
            if n in x:
                found = True
                break
        if not found:
            return n
        sums.pop(0)
        s = []
        for j in range(preamble - 1):
            s.append(n + given[1 + i + j])
        sums.append(s)
    raise ValueError(
        f"No number isn't the sum of two " "of the previous {preamble} numbers"
    )


def get_nums(s):
    given = []
    r = re.compile(r"(\d+)")
    for line in s.split("\n"):
        for i in r.findall(line):
            given.append(int(i))
    return given


if __name__ == "__main__":
    exit(main())
