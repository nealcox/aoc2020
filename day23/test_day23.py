import part1
import part2
import pytest


@pytest.mark.parametrize(
    ("s", "expected"),
    (
        # Test cases here
        # ('FBFBBFFRLR', 357),
        ("389125467", "67384529"),
    ),
)
def test_part1(s, expected):
    assert part1.calculate(s) == expected


@pytest.mark.parametrize(
    ("s", "expected"),
    (
        # Test cases here
        # ('FBFBBFFRLR', 357),
        ("389125467", 149245887792),
    ),
)
def test_part2(s, expected):
    assert part2.calculate(s) == expected
