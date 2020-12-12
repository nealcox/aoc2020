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

    given = get_re(input_text)
    dirs = "ESWN"
    dir_num = 0
    pointing = "E"
    x = 0
    y = 0
    dxdys = {"N": (1, 0), "E": (0, 1), "W": (0, -1), "S": (-1, 0)}
    for d, i in given:
        if d in "NSEW":
            dy, dx = dxdys[d]
            x = x + i * dx
            y = y + i * dy
        elif d in "R":
            dir_num = (dir_num + (i // 90)) % 4
            pointing = dirs[dir_num]
        elif d in "L":
            dir_num = (dir_num - (i // 90)) % 4
            pointing = dirs[dir_num]
        elif d in "F":
            dy, dx = dxdys[pointing]
            x = x + i * dx
            y = y + i * dy
        else:
            raise ValueError(f"Unknown command {d}{i}")
    return abs(x) + abs(y)


def get_re(s):
    res = []
    r = re.compile(r"^(.)(\d+)")
    for line in s.split("\n"):
        for d, i in r.findall(line):
            res.append((d, int(i)))
    return res


if __name__ == "__main__":
    exit(main())
