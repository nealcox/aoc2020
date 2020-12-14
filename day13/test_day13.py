import part1
import part2
import pytest


s1 = """\
939
7,13,x,x,59,x,31,19"""

s2 = """\
3417
17,x,13,19"""

s3 = """\
754018
67,7,59,61"""

s4 = """\
779210
67,x,7,59,61"""

s5 = """\
1261476
67,7,x,59,61"""

s6 = """\
1202161486
1789,37,47,1889"""


@pytest.mark.parametrize(
    ("s", "expected"),
    (
        # Test cases here
        # ('FBFBBFFRLR', 357),
        (s1, 295),
    ),
)
def test_part1(s, expected):
    assert part1.calculate(s) == expected


@pytest.mark.parametrize(
    ("s", "expected"),
    (
        # Test cases here
        # ('FBFBBFFRLR', 357),
        (s1, 1068781),
        (s2, 3417),
        (s3, 754018),
        (s4, 779210),
        (s5, 1261476),
        (s6, 1202161486),
    ),
)
def test_part2(s, expected):
    assert part2.calculate(s) == expected
