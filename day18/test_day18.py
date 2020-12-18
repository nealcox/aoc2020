import part1
import part2
import pytest


s1 = "1 + 2 * 3 + 4 * 5 + 6"
s2 = "1 + (2 * 3) + (4 * (5 + 6))"
s3 = "2 * 3 + (4 * 5)"
s4 = "5 + (8 * 3 + 9 + 3 * 4 * 3)"
s5 = "5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))"
s6 = "((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2"


@pytest.mark.parametrize(
    ("s", "expected"),
    (
        (s1, 71),
        (s2, 51),
        (s3, 26),
        (s4, 437),
        (s5, 12240),
        (s6, 13632),
    ),
)
def test_part1(s, expected):
    assert part1.calculate(s) == expected


@pytest.mark.parametrize(
    ("s", "expected"),
    (
        (s1, 231),
        (s2, 51),
        (s3, 46),
        (s4, 1445),
        (s5, 669060),
        (s6, 23340),
    ),
)
def test_part2(s, expected):
    assert part2.calculate(s) == expected
