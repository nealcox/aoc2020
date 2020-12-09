import part1
import part2
import pytest


sample = """\
35
20
15
25
47
40
62
55
65
95
102
117
150
182
127
219
299
277
309
576"""


@pytest.mark.parametrize(
    ("s", "n", "expected"),
    (
        # Test cases here
        (sample, 5, 127),
    ),
)
def test1(s, n, expected):
    assert part1.calculate(s, n) == expected


@pytest.mark.parametrize(
    ("s", "n", "expected"),
    (
        # Test cases here
        (sample, 5, 62),
    ),
)
def test2(s, n, expected):
    assert part2.calculate(s, n) == expected
