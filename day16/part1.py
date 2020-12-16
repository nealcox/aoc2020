import sys


def main():
    if len(sys.argv) > 1:
        filename = sys.argv[1]
    else:
        filename = "input.txt"
    with open(filename) as f:
        input_text = f.read().strip()
    print(f"Answer: {calculate(input_text)}")


def calculate(input_text):
    fields_in, my_ticket_in, other_tickets_in = input_text.split("\n\n")
    fields = set()

    # Get ranges for validation
    ranges = set()
    for line in fields_in.split("\n"):
        line = line.strip()
        fields = line.split(":")
        for range_or_or in fields[1].split():
            if range_or_or == "or":
                continue
            vals = range_or_or.split("-")
            lower, upper = int(vals[0]), int(vals[1])
            range_ = (lower, upper)
            ranges.add(range_)

    my_ticket = tuple(int(i) for i in my_ticket_in.split("\n")[1].split(","))

    other_tickets = set()
    for line in other_tickets_in.split("\n")[1:]:
        vals = tuple(int(i) for i in line.split(","))
        other_tickets.add(vals)

    error_rate = 0
    for other_ticket in other_tickets:
        for val in other_ticket:
            if is_invalid(val, ranges):
                error_rate += val

    return error_rate


def is_invalid(val, ranges):
    for lower, upper in ranges:
        if lower <= val <= upper:
            return False
    return True


if __name__ == "__main__":
    exit(main())
