import part1

# import part2
import pytest


@pytest.mark.parametrize(
    ("s", "expected"),
    (
        # Test cases here
        # ('FBFBBFFRLR', 357),
    ),
)
def test_part1(s, expected):
    assert part1.calculate(s) == expected
