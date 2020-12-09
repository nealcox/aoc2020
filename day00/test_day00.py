import part1
import pytest


@pytest.mark.parametrize(
    ("s", "expected"),
    (
        # Test cases here
        # ('FBFBBFFRLR', 357),
    ),
)
def test(s, expected):
    assert part1.calculate(s) == expected
