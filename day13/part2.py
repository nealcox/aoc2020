import re
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
    #
    #  Consider 17,x,13,19
    #  Firstly 17 & 13
    #  We need bus 13 to leave 2 minutes after bus 17. If bus 17 leaves at
    #  time T,
    #          A * 17 + 2 = B * 13     for some A & B
    #              A * 17 = -2 + B * 13
    #  mod 13:
    #     A * 17 (mod 13) = -2 (mod 13)
    #
    #  Rather than divide by 17 to find A, need to multiple by the inverse,
    #  which, mod 13, is 10 as 10 * 17 = 170 = 1 (mod 13)
    #  so
    #                 A   = 11 * 10 = 6 (mod 13)
    #
    #  so at time 102, bus 17 goes, then at 104, bus 13 goes
    #
    #
    #  Now add bus 19, which must leave 3 minutes after bus 13.
    #  Bus 17 leaves with bus 13 two minutes after it at
    #  102 minutes then every subsequent 221 minutes, similar to above
    #
    #        102 + A * 221 + 3 = B * 19   for some A & B
    #                  A * 221 = (-102 -3) + B * 19
    #         A * 221 (mod 19) = (-102 -3)   (mod 19)
    #
    #  Inverse of  221 (mod 19) is 8
    #  so
    #                       A  = 9 * 8 (mod 19)
    #                          = 15
    #
    #  So time T for bus 17 is 102 + 15 * 221 = 3417

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
