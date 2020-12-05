import sys


def main():
    if len(sys.argv) > 1:
        input_file = sys.argv[1]
    else:
        input_file = "input.txt"
    with open(input_file) as f:
        input_text = f.read().strip()

    print(f"Answer: {calculate(input_text)}")


def calculate(input_text):
    given = parse(input_text)
    seat_ids = []
    for bpass in given:
        row = binary(bpass[:7], 0, 127)
        seat = binary(bpass[-3:], 0, 7)
        seat_ids.append(row * 8 + seat)
    for seat in range(1025):
        if (seat not in seat_ids) and (seat + 1 in seat_ids) and (seat - 1 in seat_ids):
            answer = seat
    return answer


def binary(s, lower, upper):
    for i in range(len(s)):
        if s[i] in "FL":
            upper = upper - (upper - lower) // 2 - 1
        elif s[i] in "BR":
            lower = lower + (upper - lower) // 2 + 1
    if upper != lower:
        raise ValueError
    return lower


def parse(input_text):
    given = []
    for line in input_text.split("\n"):
        line = line.strip()
        given.append(line)
    return given


if __name__ == "__main__":
    exit(main())
