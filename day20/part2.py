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

    ################################################################
    borderlessimage = get_image(given)

    for i, l in enumerate(borderlessimage):
        print(i, l)

    # ans = roughness(borderlessimage)

    return answer


def roughness(search_image):
    #
    #     "                  #"
    #     "#    ##    ##    ###"
    #     " #  #  #  #  #  #"
    #
    r0 = re.compile(".{18}[#O]")
    r1 = re.compile("[#O].{4}[#O][#O].{4}[#O][#O].{4}[#O][#O][#O]")
    r2 = re.compile(".[#O]..[#O]..[#O]..[#O]..[#O]..[#O]")

    im = search_image[:]
    im_rev = im[:].reverse()
    for image in [im, im_rev]:
        for rotation in range(4):
            print(rotation)
            for i, line in enumerate(im[1:-1], start=1):
                ms = r1.findall(line)
                if ms:
                    print(i, line)
                    print(ms)
            im = rotate(im)

    return 0


def rotate(im):
    new_im = []
    for i in range(len(im)):
        new_im.append([])
        for j in range(len(im)):
            new_im[-1].append(im[j][i])
    return ["".join(l) for l in new_im]


def get_image(given):
    if len(given) == 9:
        size = 3
    elif len(given) == 144:
        size = 12
    else:
        raise ValueError(f"Length of input {len(given)}")
    tiles = {}
    edges = defaultdict(list)
    tile_images = []
    tile_images_index = {}
    regex = re.compile("\\d+")
    for tile in given:
        tile = tile.split("\n")
        tile_size = len(tile[1])
        tile_num = int(regex.search(tile[0]).group(0))
        tile_edges = [
            tile[1],
            tile[-1],
            "".join([l[0] for l in tile[1:]]),
            "".join([l[-1] for l in tile[1:]]),
        ]
        reversed_edges = []
        for e in tile_edges:
            reversed_edges.append(e[len(e) :: -1])
        tile_edges = tile_edges + reversed_edges

        for e in tile_edges:
            edges[e].append(tile_num)
        tiles[tile_num] = tile_edges
        tile_image_l = []
        for r in tile[1:]:
            tile_image_l.append([])
            for c in r:
                tile_image_l[-1].append(c)
        tile_images.append(tile_image_l)
        tile_images_index[tile_num] = len(tile_images) - 1

    corners = []
    topleft = None
    for tile in tiles:
        num_edges = 0
        for e in tiles[tile]:
            if len(edges[e]) == 1:
                num_edges += 1
        if num_edges == 4:
            corners.append(tile)

            top = tiles[tile][0]
            left = tiles[tile][2]
            if len(edges[top]) == 1 and len(edges[left]) == 1:
                topleft = tile
    c = corners[0]
    while not topleft:
        t = tile_images[tile_images_index[c]][:]
        t2 = []
        for _ in range(tile_size):
            t2.append([])
        for i in range(tile_size):
            for j in range(tile_size):
                t2[i].append(t[tile_size - j - 1][i])
        tile_images[tile_images_index[c]] = t2
        tiles[c] = [
            tiles[c][6],
            tiles[c][7],
            tiles[c][1],
            tiles[c][0],
            tiles[c][2],
            tiles[c][3],
            tiles[c][5],
            tiles[c][4],
        ]

        top = tiles[c][0]
        left = tiles[c][2]
        if len(edges[top]) == 1 and len(edges[left]) == 1:
            topleft = c

    image = []
    used_tiles = []
    for _ in range(size):
        image.append([])
    for r in range(0, size):
        for c in range(0, size):
            if r == 0 and c == 0:
                image[r].append(topleft)
                used_tiles.append(topleft)
            elif r == 0:
                lr_match = tiles[image[r][c - 1]][3]
                matches = edges[lr_match]
                matches.remove(image[r][c - 1])
                assert len(matches) == 1
                match = matches[0]
                used_tiles.append(match)
                idx = tiles[match].index(lr_match)
                if idx == 0:  # top matches so flip diagonally
                    t = tile_images[tile_images_index[match]]
                    for i in range(size):
                        for j in range(size):
                            t[i][j], t[j][i] = t[j][i], t[i][j]
                    tile_images[tile_images_index[match]] = t

                elif idx == 2:  # left, so matches as is
                    pass

                elif idx == 3:  # flip about vertical axis
                    t = tile_images[tile_images_index[match]][:]
                    t2 = []
                    for _ in range(tile_size):
                        t2.append([])
                    for i in range(tile_size):
                        for j in range(tile_size):
                            t2[i].append(t[i][tile_size - 1 - j])
                    tiles[match] = [
                        tiles[match][4],
                        tiles[match][5],
                        tiles[match][3],
                        tiles[match][2],
                        tiles[match][0],
                        tiles[match][1],
                        tiles[match][7],
                        tiles[match][6],
                    ]
                    tile_images[tile_images_index[match]] = t2

                elif idx == 4:  # rotate 90 anti clockwise
                    t = tile_images[tile_images_index[match]][:]
                    t2 = []
                    for _ in range(tile_size):
                        t2.append([])
                    for i in range(tile_size):
                        for j in range(tile_size):
                            t2[i].append(t[j][tile_size - 1 - i])
                    tiles[match] = [
                        tiles[match][3],
                        tiles[match][2],
                        tiles[match][4],
                        tiles[match][5],
                        tiles[match][7],
                        tiles[match][6],
                        tiles[match][0],
                        tiles[match][1],
                    ]

                    tile_images[tile_images_index[match]] = t2

                elif (
                    idx == 5
                ):  # bottom_reversed matches flip about top right,bottom left
                    t = tile_images[tile_images_index[match]][:]
                    t2 = []
                    for _ in range(tile_size):
                        t2.append([])
                    for i in range(tile_size):
                        for j in range(tile_size):
                            t2[i].append(t[tile_size - 1 - j][tile_size - 1 - i])
                    tile_images[tile_images_index[match]] = t2
                    tiles[match] = [
                        tiles[match][7],
                        tiles[match][6],
                        tiles[match][5],
                        tiles[match][4],
                        tiles[match][3],
                        tiles[match][3],
                        tiles[match][1],
                        tiles[match][0],
                    ]

                elif idx == 7:  # right, upside down, rotate 180
                    t = tile_images[tile_images_index[match]][:]
                    t2 = []
                    for _ in range(tile_size):
                        t2.append([])
                    for i in range(tile_size):
                        for j in range(tile_size):
                            t2[i].append(t[tile_size - i - 1][tile_size - j - 1])
                    tile_images[tile_images_index[match]] = t2
                    tiles[match] = [
                        tiles[match][5],
                        tiles[match][4],
                        tiles[match][7],
                        tiles[match][6],
                        tiles[match][1],
                        tiles[match][0],
                        tiles[match][3],
                        tiles[match][2],
                    ]

                elif idx == 9999:  # no change XXXXX
                    t = tile_images[tile_images_index[match]][:]
                    print(f"Before:")
                    for l in t:
                        print("".join(l))
                    t2 = []
                    for _ in range(tile_size):
                        t2.append([])
                    for i in range(tile_size):
                        for j in range(tile_size):
                            t2[i].append(t[i][j])
                    print(f"After:")
                    for l in t2:
                        print("".join(l))
                    tiles[match] = [
                        tiles[match][0],
                        tiles[match][1],
                        tiles[match][2],
                        tiles[match][3],
                        tiles[match][4],
                        tiles[match][5],
                        tiles[match][6],
                        tiles[match][7],
                    ]

                    tile_images[tile_images_index[match]] = t2

                else:
                    raise NotImplementedError(f"{idx}")

                image[r].append(match)
            else:
                tb_match = tiles[image[r - 1][c]][1]
                matches = edges[tb_match]
                matches.remove(image[r - 1][c])
                assert len(matches) == 1
                match = matches[0]
                used_tiles.append(match)
                idx = tiles[match].index(tb_match)
                if idx == 0:  # our top matches bottom of above: no change
                    pass

                elif idx == 1:  # bottom, flip horizontal axis
                    t = tile_images[tile_images_index[match]][:]
                    t2 = []
                    for _ in range(tile_size):
                        t2.append([])
                    for i in range(tile_size):
                        for j in range(tile_size):
                            t2[i].append(t[tile_size - i - 1][j])
                    tile_images[tile_images_index[match]] = t2
                    tiles[match] = [
                        tiles[match][1],
                        tiles[match][0],
                        tiles[match][6],
                        tiles[match][7],
                        tiles[match][5],
                        tiles[match][4],
                        tiles[match][2],
                        tiles[match][3],
                    ]

                elif idx == 3:  # rotate 90 anticlockwise
                    t = tile_images[tile_images_index[match]][:]
                    t2 = []
                    for _ in range(tile_size):
                        t2.append([])
                    for i in range(tile_size):
                        for j in range(tile_size):
                            t2[i].append(t[j][tile_size - 1 - i])
                    tiles[match] = [
                        tiles[match][3],
                        tiles[match][2],
                        tiles[match][4],
                        tiles[match][5],
                        tiles[match][7],
                        tiles[match][6],
                        tiles[match][0],
                        tiles[match][1],
                    ]

                    tile_images[tile_images_index[match]] = t2

                elif idx == 4:  # no change
                    t = tile_images[tile_images_index[match]][:]
                    t2 = []
                    for _ in range(tile_size):
                        t2.append([])
                    for i in range(tile_size):
                        for j in range(tile_size):
                            t2[i].append(t[i][tile_size - 1 - j])
                    tiles[match] = [
                        tiles[match][4],
                        tiles[match][5],
                        tiles[match][3],
                        tiles[match][2],
                        tiles[match][0],
                        tiles[match][1],
                        tiles[match][7],
                        tiles[match][6],
                    ]

                    tile_images[tile_images_index[match]] = t2

                elif idx == 5:  # rotate 180
                    t = tile_images[tile_images_index[match]][:]
                    t2 = []
                    for _ in range(tile_size):
                        t2.append([])
                    for i in range(tile_size):
                        for j in range(tile_size):
                            t2[i].append(t[tile_size - 1 - i][tile_size - 1 - j])
                    tiles[match] = [
                        tiles[match][5],
                        tiles[match][4],
                        tiles[match][7],
                        tiles[match][6],
                        tiles[match][1],
                        tiles[match][0],
                        tiles[match][3],
                        tiles[match][2],
                    ]

                    tile_images[tile_images_index[match]] = t2

                elif idx == 6:  # left, upside down, rotate 90 clockwise
                    t = tile_images[tile_images_index[match]][:]
                    t2 = []
                    for _ in range(tile_size):
                        t2.append([])
                    for i in range(tile_size):
                        for j in range(tile_size):
                            t2[i].append(t[tile_size - j - 1][i])
                    tile_images[tile_images_index[match]] = t2
                    tiles[match] = [
                        tiles[match][6],
                        tiles[match][7],
                        tiles[match][1],
                        tiles[match][0],
                        tiles[match][2],
                        tiles[match][3],
                        tiles[match][5],
                        tiles[match][4],
                    ]

                elif idx == 7:  # flip about axis top right bottom left  XXXXX
                    t = tile_images[tile_images_index[match]][:]
                    t2 = []
                    for _ in range(tile_size):
                        t2.append([])
                    for i in range(tile_size):
                        for j in range(tile_size):
                            t2[i].append(t[tile_size - 1 - j][tile_size - 1 - i])
                    tiles[match] = [
                        tiles[match][7],
                        tiles[match][6],
                        tiles[match][5],
                        tiles[match][4],
                        tiles[match][3],
                        tiles[match][2],
                        tiles[match][1],
                        tiles[match][0],
                    ]

                    tile_images[tile_images_index[match]] = t2

                elif idx == 9999:
                    t = tile_images[tile_images_index[match]]
                    for i in range(tile_size):
                        for j in range(tile_size):
                            t[i][j], t[j][i] = t[j][i], t[i][j]
                    tile_images[tile_images_index[match]] = t

                else:
                    print(idx)
                    raise NotImplementedError(f"{idx}")
                image[r].append(match)

    assert len(used_tiles) == len(tiles)
    borderlessimage = [""] * size * (tile_size - 2)
    for r2 in range(size):
        for tile_row in range(1, tile_size - 1):
            for tile_num in image[r2]:
                idx = tile_images_index[tile_num]
                # print( "".join(tile_images[idx][tile_row][1:tile_size-1]),end = " ")
                image_row = r2 * (tile_size - 2) + tile_row - 1
                borderlessimage[image_row] += "".join(
                    tile_images[idx][tile_row][1 : tile_size - 1]
                )
            # print(image_row)
        # print()
    return borderlessimage


if __name__ == "__main__":
    exit(main())
