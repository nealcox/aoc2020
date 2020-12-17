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

    space = defaultdict(int)

    min_x, min_y, min_z = float("inf"), float("inf"), float("inf")
    max_x, max_y, max_z = -float("inf"), -float("inf"), -float("inf")
    max_z = 0
    min_z = 0
    for x, line in enumerate(given):
        for y, char in enumerate(line):
            if char == "#":
                min_x = min(x, min_x)
                min_y = min(y, min_y)
                max_x = max(x, max_x)
                max_y = max(y, max_y)
                space[x, y, 0] = 1

    print_space(space, min_x, min_y, min_z, max_x, max_y, max_z)
    p = (0, 0, 0)

    for cycle in range(1, 7):
        print(f"After {cycle} cycles:")

        next_space = defaultdict(int)
        keys = set(k for k in space.keys())
        min_x -= 1
        min_y -= 1
        max_z -= 1
        max_x += 1
        max_y += 1
        max_z += 1
        for x in range(min_x - 1, max_x + 2):
            for y in range(min_y - 1, max_y + 2):
                for z in range(min_z - 1, max_z + 2):
                    point = (x, y, z)
                    # print(f"Considering {point}")
                    active_neighbours = 0
                    for p1 in neighbours(point[0], point[1], point[2]):
                        # print(f"{p1}")
                        if space[p1] == 1:
                            # print(" is active")
                            active_neighbours += 1
                        # else:
                        # print(" is NOT active")
                    # print(f"{point} has {active_neighbours} active neighbours")
                    if space[point] == 1:
                        if active_neighbours == 2 or active_neighbours == 3:
                            next_space[point] = 1
                    else:
                        if active_neighbours == 3:
                            next_space[point] = 1
        space = defaultdict(int)
        min_x, min_y, min_z = float("inf"), float("inf"), float("inf")
        max_x, max_y, max_z = -float("inf"), -float("inf"), -float("inf")
        for point in next_space:
            if next_space[point] == 1:
                space[point] = 1
                min_x = min(point[0], min_x)
                min_y = min(point[1], min_y)
                min_z = min(point[2], min_z)
                max_x = max(point[0], max_x)
                max_y = max(point[1], max_y)
                max_z = max(point[2], max_z)

        # space = next_space
        answer = sum(space.values())
        print(answer)
        print_space(space, min_x, min_y, min_z, max_x, max_y, max_z)

    return answer


def neighbours(x, y, z):
    for dx in range(-1, 2):
        for dy in range(-1, 2):
            for dz in range(-1, 2):
                if dx != 0 or dy != 0 or dz != 0:
                    yield (x + dx, y + dy, z + dz)


def print_space(space, min_x, min_y, min_z, max_x, max_y, max_z):
    for z in range(min_z, max_z + 1):
        print(f"\nz = {z}")
        for x in range(min_x, max_x + 1):
            for y in range(min_y, max_y + 1):
                print(space[x, y, z], end="")
            print()

    pass


def parse(s):
    given = None
    given = partlines(s)
    # given = get_re(s)
    return given


def partlines(s):
    given = []
    for line in s.split("\n"):
        line = line.strip()
        given.append(line)
    return given


def get_one_int_per_line(s):
    ints = []
    for line in s.split("\n"):
        ints.append(int(i))
    return ints


def get_re(s):
    given = []
    r = re.compile(r"(\d+)")
    for line in s.split("\n"):
        res = []
        for i in r.findall(line):
            res.append(int(i))
        given.append(res)
    return given


if __name__ == "__main__":
    exit(main())
