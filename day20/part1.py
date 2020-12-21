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
    given = input_text.split("\n\n")
    tiles = {}
    edges = defaultdict(list)
    r = re.compile("\\d+")
    for tile in given:
        tile = tile.split("\n")
        tile_num = int(r.search(tile[0]).group(0))
        print(tile[0], tile_num)
        tile_edges = [
            tile[1],
            tile[-1],
            "".join([l[0] for l in tile[1:]]),
            "".join([l[-1] for l in tile[1:]]),
        ]
        print(tile_edges)
        for e in tile_edges:
            edges[e].append(tile_num)
            edges[e[len(e) :: -1]].append(tile_num)
        tiles[tile_num] = sorted(tile_edges)

    for edge, l in edges.items():
        print(edge, len(l))
    corners = []
    for tile in tiles:
        print(tile)
        num_edges = 0
        for e in tiles[tile]:
            print(e, len(edges[e]))
            if len(edges[e]) == 1:
                num_edges += 1
        print(tile, num_edges)
        if num_edges == 2:
            corners.append(tile)
    print(f"corners: {corners}")
    ans = 1
    for c in corners:
        ans *= c

    print(len(given))

    return ans


def parse(s):
    given = None
    # given = partlines(s)
    given = get_one_int_per_line(s)
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
