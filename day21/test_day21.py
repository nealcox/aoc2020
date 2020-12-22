import part1
import part2
import pytest

s1 = """\
mxmxvkd kfcds sqjhc nhms (contains dairy, fish)
trh fvjkl sbzzf mxmxvkd (contains dairy)
sqjhc fvjkl (contains soy)
sqjhc mxmxvkd sbzzf (contains fish)"""


@pytest.mark.parametrize(
    ("s", "expected"),
    (
        # Test cases here
        # ('FBFBBFFRLR', 357),
        (s1, 5),
    ),
)
def test_part1(s, expected):
    assert part1.calculate(s) == expected


@pytest.mark.parametrize(
    ("s", "expected"),
    (
        # Test cases here
        # ('FBFBBFFRLR', 357),
        (s1, "mxmxvkd,sqjhc,fvjkl"),
    ),
)
def test_part2(s, expected):
    assert part2.calculate(s) == expected
