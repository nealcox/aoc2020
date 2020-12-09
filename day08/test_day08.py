import part1
import part2
import pytest

prog = """\
nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6"""


@pytest.mark.parametrize(
    ("s", "expected"),
    (
        # Test cases here
        (prog, 5),
    ),
)
def testp1(s, expected):
    assert part1.calculate(s) == expected


@pytest.mark.parametrize(
    ("s", "expected"),
    (
        # Test cases here
        (prog, 8),
    ),
)
def testp2(s, expected):
    assert part2.calculate(s) == expected
