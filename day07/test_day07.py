import part1
import part2
import pytest


s1 = """\
light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags."""

s2 = """\
shiny gold bags contain 2 dark red bags.
dark red bags contain 2 dark orange bags.
dark orange bags contain 2 dark yellow bags.
dark yellow bags contain 2 dark green bags.
dark green bags contain 2 dark blue bags.
dark blue bags contain 2 dark violet bags.
dark violet bags contain no other bags."""


@pytest.mark.parametrize(
    ("s", "expected"),
    (
        # Test cases here
        (
            s1,
            4,
        ),
    ),
)
def test(s, expected):
    assert part1.calculate(s) == expected


@pytest.mark.parametrize(
    ("s", "expected"),
    (
        # Test cases here
        (s1, 32),
        (s2, 126),
    ),
)
def test_part2(s, expected):
    assert part2.calculate(s) == expected
