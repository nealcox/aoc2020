import part1
import part2
import pytest

m1 = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X"
i1 = """\
mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X
mem[8] = 11
mem[7] = 101
mem[8] = 0"""
i2 = """\
mask = 000000000000000000000000000000X1001X
mem[42] = 100
mask = 00000000000000000000000000000000X0XX
mem[26] = 1"""


@pytest.mark.parametrize(
    ("m", "v", "expected"),
    (
        # Test cases here
        # ('FBFBBFFRLR', 357),
        (m1, 11, 73),
        (m1, 101, 101),
        (m1, 0, 64),
    ),
)
def test_maskate(m, v, expected):
    assert part1.maskate(m, v) == expected


@pytest.mark.parametrize(
    ("s", "expected"),
    (
        # Test cases here
        # ('FBFBBFFRLR', 357),
        (i1, 165),
    ),
)
def test_part1(s, expected):
    assert part1.calculate(s) == expected


@pytest.mark.parametrize(
    ("s", "expected"),
    (
        # Test cases here
        # ('FBFBBFFRLR', 357),
        (i2, 208),
    ),
)
def test_part2(s, expected):
    assert part2.calculate(s) == expected
