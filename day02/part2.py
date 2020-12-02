import re
import sys


def main():
    if len(sys.argv) > 1:
        input_file = sys.argv[1]
    else:
        input_file = "input.txt"
    given = setup(input_file)
    print(f"Answer: {run(given)}")


def run(given):
    answer = 0
    for line in given:
        a = line[-1][line[0] - 1]
        b = line[-1][line[1] - 1]
        if (a == line[2]) ^ (b == line[2]):
            answer += 1
    return answer


def setup(filename):
    given = []
    r_exp = re.compile("-|: | |\n")
    with open(filename) as f:
        for line in f:
            line = r_exp.split((line.strip()))
            line[0] = int(line[0])
            line[1] = int(line[1])
            given.append(line)
    return given


if __name__ == "__main__":
    exit(main())
