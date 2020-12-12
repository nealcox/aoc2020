import part1
import part2
import pytest


l = """\
#.##.##.##
#######.##
#.#.#..#..
####.##.##
#.##.##.##
#.#####.##
..#.#.....
##########
#.######.#
#.#####.##"""

l1 = """\
.......#.
...#.....
.#.......
.........
..#L....#
....#....
.........
#........
...#....."""

l2 = """\
.............
.L.L.#.#.#.#.
............."""

l3 = """\
.##.##.
#.#.#.#
##...##
...L...
##...##
#.#.#.#
.##.##."""


@pytest.mark.parametrize(
    ("s", "expected"),
    (
        # Test cases here
        # ('FBFBBFFRLR', 357),
        (l, 37),
    ),
)
def test_part1(s, expected):
    assert part1.calculate(s) == expected


@pytest.mark.parametrize(
    ("r", "c", "layout", "expected"),
    (
        # Test cases here
        # ('FBFBBFFRLR', 357),
        (4, 3, part2.parse(l1)[0], 8),
        (1, 1, part2.parse(l2)[0], 0),
        (3, 3, part2.parse(l3)[0], 0),
    ),
)
def test_occupied(r, c, layout, expected):
    assert part2.occupied(r, c, layout) == expected


@pytest.mark.parametrize(
    ("s", "expected"),
    (
        # Test cases here
        # ('FBFBBFFRLR', 357),
        (l, 26),
    ),
)
def test_part2(s, expected):
    assert part2.calculate(s) == expected
