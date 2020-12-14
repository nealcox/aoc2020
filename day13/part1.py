import re
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

    start_time, bus_ids = get_re(input_text)
    earliest_time = float("inf")
    earliest_bus_id = None
    for bus in bus_ids:
        time_since_last = start_time % bus
        if time_since_last:
            earliest_time_for_bus = bus - time_since_last
        else:
            earliest_time_for_bus = 0
        if earliest_time_for_bus < earliest_time:
            earliest_time = earliest_time_for_bus
            earliest_bus_id = bus
            print(f"bus id {bus} departs at {earliest_time_for_bus}")
    return earliest_bus_id * earliest_time


def get_re(s):
    given = []
    r = re.compile(r"(\d+)")
    for line in s.split("\n"):
        res = []
        for i in r.findall(line):
            res.append(int(i))
        given.append(res)
    return given[0][0], given[1]


if __name__ == "__main__":
    exit(main())
