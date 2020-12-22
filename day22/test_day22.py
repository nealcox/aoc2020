import part1
import part2
import pytest


s1 = """\
Player 1:
9
2
6
3
1

Player 2:
5
8
4
7
10"""


@pytest.mark.parametrize(
    ("s", "expected"),
    (
        # Test cases here
        # ('FBFBBFFRLR', 357),
        (s1, 306),
    ),
)
def test_part1(s, expected):
    assert part1.calculate(s) == expected


@pytest.mark.parametrize(
    ("s", "expected"),
    (
        # Test cases here
        # ('FBFBBFFRLR', 357),
        (s1, 291),
    ),
)
def test_part2(s, expected):
    assert part2.calculate(s) == expected
