import pytest

import part1
import part2


s1 = """\
abcx
abcy
abcz"""

s2 = """\
abc

a
b
c

ab
ac

a
a
a
a

b"""

@pytest.mark.parametrize(
    ("s", "expected"),
    (
        # Test cases here
        (s1,6), 
        (s2,11), 
    ),
)
def test(s, expected):
    assert part1.calculate(s) == expected


@pytest.mark.parametrize(
    ("s", "expected"),
    (
        # Test cases here
        (s2,6), 
    ),
)
def test2(s, expected):
    assert part2.calculate(s) == expected
