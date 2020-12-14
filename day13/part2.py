import re
import sys
from collections import defaultdict
from itertools import permutations


def main():
    if len(sys.argv) > 1:
        filename = sys.argv[1]
    else:
        filename = "input.txt"
    with open(filename) as f:
        input_text = f.read().strip()
    print(f"Answer: {calculate(input_text)}")


def departs(start, n):
    time = start
    while True:
        yield time
        time += n


def calculate(input_text):
    start_time, bus_info = get_re(input_text)
    earliest_bus_id = None
    bus_first = {}
    bus_ids = []
    time = -1
    for bus in bus_info:
        time += 1
        if bus.isnumeric():
            bus = int(bus)
            if time == 0:
                base = bus
            else:
                bus_ids.append(bus)
            bus_first[bus] = time

    #  All buses leave at time 0 then every i minutes where i is its id
    #  all bus ids are coprime, so they will cycle leaving times with a
    #  period equal to product of their periods.
    #  So take first two buses, find out when they are in sync, then the
    #  subsequent bus must fit with the first
    #
    #  Call the buses dealt with the Base bus
    #  The next bus syncs at time T (sync meaning is t-bus after) where
    #  T = t-base + A * period-base = t-bus + B * period-bus
    #  Take mod of period-bus
    #               A * period-base = (t-bus - t-base) mod period-bus
    #
    #  Multiply by inverse of period-base mod period-bus (ie divide to find A)
    #  Now have A so the Base bus and additional bus sync at
    #  t-base + A * period-base
    #  We now have new Base
    time = 0
    while bus_ids:
        bus = bus_ids.pop()
        inv_of_a = pow(base, -1, bus)
        a = ((-time - bus_first[bus] % bus) * inv_of_a) % bus
        period = base * bus
        time = time + a * base
        base = period
    return time


def get_re(s):
    lines = s.splitlines()
    start_time = int(lines[0])
    buses = lines[1].split(",")
    return start_time, buses


if __name__ == "__main__":
    exit(main())
