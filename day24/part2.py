import sys
from collections import defaultdict
from fractions import Fraction


def main():
    if len(sys.argv) > 1:
        filename = sys.argv[1]
    else:
        filename = "input.txt"
    with open(filename) as f:
        input_text = f.read().strip()
    print(f"Answer: {calculate(input_text)}")


HALF = Fraction(1, 2)
WHITE = False
BLACK = True

deltas = {
    "e": (1, 0),
    "w": (-1, 0),
    "se": (HALF, -1),
    "sw": (-HALF, -1),
    "ne": (HALF, 1),
    "nw": (-HALF, 1),
}


def neigbours(tile):
    x, y = tile
    for direction in deltas:
        yield x + deltas[direction][0], y + deltas[direction][1]


def calculate(input_text):

    lines = input_text.strip().split("\n")
    tiles = defaultdict(bool)
    for line in lines:
        x, y = 0, 0
        i = 0
        while i < len(line):
            move = line[i]
            if move == "s" or move == "n":
                i += 1
                move += line[i]
            x += deltas[move][0]
            y += deltas[move][1]
            i += 1
        tiles[x, y] = not tiles[x, y]

    for day in range(1, 101):
        print(f"Day {day}")
        new_tiles = defaultdict(bool)
        black_neighbours = defaultdict(int)

        # Mark
        for tile, colour in tiles.items():
            if colour == BLACK:
                for neigbour in neigbours(tile):
                    black_neighbours[neigbour] += 1

        for tile in black_neighbours:
            if tile not in tiles:
                tiles[tile] = WHITE

        # Sweep
        for tile, colour in tiles.items():
            if colour == BLACK:
                if black_neighbours[tile] == 1 or black_neighbours[tile] == 2:
                    new_tiles[tile] = BLACK
            #                else:
            #                    new_tiles[tile] == WHITE
            else:
                if black_neighbours[tile] == 2:
                    new_tiles[tile] = BLACK
        #                else:
        #                    new_tiles[tile] == WHITE
        tiles = new_tiles

    return sum(tiles.values())


if __name__ == "__main__":
    exit(main())
