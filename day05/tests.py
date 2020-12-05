import pytest

import part1
import part2

@pytest.mark.parametrize(
        ('s', 'expected'),
        (
            ('FBFBBFFRLR', 357),
            ('BFFFBBFRRR', 567),
            ('FFFBBBFRRR', 119),
            ('BBFFBBFRLL', 820),
        ),
)
def test(s, expected):
    assert part1.calculate(s) == expected
