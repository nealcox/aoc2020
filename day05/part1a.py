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
    answer = 0
    for bpass in given:
        seat_id = 0
        for bit in bpass:
            seat_id = seat_id * 2 + int(bit in "BR")
        if seat_id > answer:
            answer = seat_id
    return answer


def parse(input_text):
    given = []
    for line in input_text.split("\n"):
        line = line.strip()
        given.append(line)
    return given


if __name__ == "__main__":
    exit(main())
