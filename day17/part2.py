import re
import sys
from collections import defaultdict
from itertools import permutations

NUM_CYCLES = 6


def main():
    if len(sys.argv) > 1:
        filename = sys.argv[1]
    else:
        filename = "input.txt"
    with open(filename) as f:
        input_text = f.read().strip()
    print(f"Answer: {calculate(input_text)}")


def calculate(input_text):

    given = input_text.split()
    space = defaultdict(int)

    min_x, min_y = float("inf"), float("inf")
    max_x, max_y = -float("inf"), -float("inf")
    min_z, max_z, min_w, max_w = 0, 0, 0, 0
    for x, line in enumerate(given):
        for y, char in enumerate(line):
            if char == "#":
                min_x = min(x, min_x)
                min_y = min(y, min_y)
                max_x = max(x, max_x)
                max_y = max(y, max_y)
                space[x, y, 0, 0] = 1

    for cycle in range(1, NUM_CYCLES + 1):
        print(f"After {cycle} cycles:")

        next_space = defaultdict(int)
        keys = set(k for k in space.keys())
        for x in range(min_x - 1, max_x + 2):
            for y in range(min_y - 1, max_y + 2):
                for z in range(min_z - 1, max_z + 2):
                    for w in range(min_w - 1, max_w + 2):
                        point = (x, y, z, w)
                        active_neighbours = 0
                        for p1 in neighbours(point[0], point[1], point[2], point[3]):
                            if space[p1] == 1:
                                active_neighbours += 1
                        if space[point] == 1:
                            if active_neighbours == 2 or active_neighbours == 3:
                                next_space[point] = 1
                        else:
                            if active_neighbours == 3:
                                next_space[point] = 1
        space = defaultdict(int)
        min_x, min_y, min_z, min_w = (
            float("inf"),
            float("inf"),
            float("inf"),
            float("inf"),
        )
        max_x, max_y, max_z, max_w = (
            -float("inf"),
            -float("inf"),
            -float("inf"),
            -float("inf"),
        )
        for point in next_space:
            if next_space[point] == 1:
                space[point] = 1
                min_x = min(point[0], min_x)
                min_y = min(point[1], min_y)
                min_z = min(point[2], min_z)
                min_w = min(point[3], min_w)
                max_x = max(point[0], max_x)
                max_y = max(point[1], max_y)
                max_z = max(point[2], max_z)
                max_w = max(point[3], max_w)

        answer = sum(space.values())
        print(answer)

    return answer


def neighbours(x, y, z, w):
    for dx in range(-1, 2):
        for dy in range(-1, 2):
            for dz in range(-1, 2):
                for dw in range(-1, 2):
                    if dx != 0 or dy != 0 or dz != 0 or dw != 0:
                        yield (x + dx, y + dy, z + dz, w + dw)


if __name__ == "__main__":
    exit(main())
