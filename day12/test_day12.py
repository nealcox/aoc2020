import part1
import part2
import pytest


s1 = """\
F10
N3
F7
R90
F11"""


@pytest.mark.parametrize(
    ("s", "expected"),
    (
        # Test cases here
        (s1, 25),
        # ('FBFBBFFRLR', 357),
    ),
)
def test_part1(s, expected):
    assert part1.calculate(s) == expected


@pytest.mark.parametrize(
    ("s", "expected"),
    (
        # Test cases here
        (s1, 286),
        # ('FBFBBFFRLR', 357),
    ),
)
def test_part2(s, expected):
    assert part2.calculate(s) == expected
