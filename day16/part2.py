import sys
from collections import defaultdict


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

    ranges = set()
    defined = defaultdict(list)
    for line in fields_in.split("\n"):
        fields = line.split(":")
        name = fields[0]
        for range_or_or in fields[1].split():
            if range_or_or == "or":
                continue
            vals = range_or_or.split("-")
            lower, upper = int(vals[0]), int(vals[1])
            range_ = (lower, upper)
            ranges.add(range_)
            defined[name].append(range_)

    my_ticket = tuple(int(i) for i in my_ticket_in.split("\n")[1].split(","))

    other_tickets = set()
    for line in other_tickets_in.split("\n")[1:]:
        vals = tuple(int(i) for i in line.split(","))
        other_tickets.add(vals)

    invalid_tickets = set()
    for other_ticket in other_tickets:
        for val in other_ticket:
            if is_invalid(val, ranges):
                invalid_tickets.add(other_ticket)

    valid_tickets = other_tickets - invalid_tickets

    num_fields = len(my_ticket)
    # possible[i] = list of field names that could be field number i
    # initially, all possible
    possible = defaultdict(set)
    for i in range(num_fields):
        for name in defined:
            possible[i].add(name)

    # if a valid ticket has a value that doesn't work in field n for a field name
    # that number field can't be that name
    for t in valid_tickets:
        for field_num, val in enumerate(t):
            to_delete = set()
            for name in possible[field_num]:
                if is_invalid(val, defined[name]):
                    to_delete.add(name)
            possible[field_num] = possible[field_num] - to_delete

    # if a field number has only one possibility, that name belongs too that
    # field, so eliminate the name as possible for other field numbers
    changes = True
    while changes:
        changes = False
        for i in range(num_fields):
            if len(possible[i]) == 1:
                for j in range(num_fields):
                    if i != j and (possible[i] & possible[j]):
                        possible[j] = possible[j] - possible[i]
                        changes = True
    assert all(len(possible[i]) == 1 for i in range(num_fields))

    answer = 1
    for i in range(num_fields):
        for n in possible[i]:
            if n.startswith("departure"):
                answer *= my_ticket[i]
    return answer


def is_invalid(val, ranges):
    for lower, upper in ranges:
        if lower <= val <= upper:
            return False
    return True


if __name__ == "__main__":
    exit(main())
