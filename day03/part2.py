import sys


def main():
    if len(sys.argv) > 1:
        input_file = sys.argv[1]
    else:
        input_file = "input.txt"
    given = setup(input_file)
    print(f"Answer: {run(given)}")


def run(forest):
    cols = len(forest[0])
    total_trees = 1
    for (right, down) in ((1, 1), (3, 1), (5, 1), (7, 1), (1, 2)):
        r, c = 0, 0
        num_trees_for_slope = 0
        while True:
            r = r + down
            c = c + right
            if r >= len(forest):
                break
            if forest[r][c % cols] == "#":
                num_trees_for_slope += 1
        total_trees *= num_trees_for_slope
    return total_trees


def setup(filename):
    given = []
    with open(filename) as f:
        for line in f:
            given.append(line.strip())
    return given


if __name__ == "__main__":
    exit(main())
