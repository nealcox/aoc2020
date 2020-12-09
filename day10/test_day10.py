import part1
import part2
import pytest


s1 = """\
16
10
15
5
1
11
7
19
6
12
4"""

s2 = """\
28
33
18
42
31
14
46
20
48
47
24
23
49
45
19
38
39
11
1
32
25
35
8
17
7
9
4
2
34
10
3"""


@pytest.mark.parametrize(
    ("s", "expected"),
    (
        # Test cases here
        (s1, 35),
        (s2, 220),
    ),
)
def test_part1(s, expected):
    assert part1.calculate(s) == expected


@pytest.mark.parametrize(
    ("s", "expected"),
    (
        # Test cases here
        (s1, 8),
        (s2, 19208),
    ),
)
def test_part2(s, expected):
    assert part2.calculate(s) == expected
