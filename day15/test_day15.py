import part1
import part2slow
import pytest

s1 = "0,3,6"
s2 = "1,3,2"
s3 = "2,1,3"
s4 = "1,2,3"
s5 = "2,3,1"
s6 = "3,2,1"
s7 = "3,1,2"


@pytest.mark.parametrize(
    ("s", "expected"),
    (
        # Test cases here
        # ('FBFBBFFRLR', 357),
        (s1, 436),
        (s2, 1),
        (s3, 10),
        (s4, 27),
        (s5, 78),
        (s6, 438),
        (s7, 1836),
    ),
)
def test_part1(s, expected):
    assert part1.calculate(s) == expected


@pytest.mark.parametrize(
    ("s", "expected"),
    (
        # Test cases here
        # ('FBFBBFFRLR', 357),
        (s1, 175594),
        (s2, 2578),
        (s3, 3544142),
        (s4, 261214),
        (s5, 6895259),
        (s6, 18),
        (s7, 362),
    ),
)
def test_part2(s, expected):
    assert part2slow.calculate(s) == expected
