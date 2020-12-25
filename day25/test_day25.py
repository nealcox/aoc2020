import part1
import pytest


s1 = """\
5764801
17807724"""


@pytest.mark.parametrize(
    ("s", "expected"),
    (
        # Test cases here
        # ('FBFBBFFRLR', 357),
        (s1, 14897079),
    ),
)
def test_part1(s, expected):
    assert part1.calculate(s) == expected
