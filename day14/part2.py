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
    given = get_re(input_text)
    memory = defaultdict(int)
    for mask in given:
        for mem, val in given[mask]:
            floating_address = maskate(mask, mem)
            for m in get_addresses(floating_address):
                memory[int(m, base=2)] = val
    return sum(memory.values())


def get_addresses(floatimg):
    addresses = []
    to_do = []
    to_do.append(floatimg)
    while to_do:
        m = to_do.pop()
        if "X" in m:
            to_do.append(m.replace("X", "0", 1))
            to_do.append(m.replace("X", "1", 1))
        else:
            addresses.append(m)
    return addresses


def maskate(mask, add):
    add = f"{add:036b}"
    ret = []
    for i, m in enumerate(mask):
        if m == "0":
            ret.append(add[i])
        else:
            ret.append(m)
    return "".join(ret)


def get_re(s):
    given = defaultdict(list)
    r_mem = re.compile(r"(\d+)")
    for line in s.split("\n"):
        if line.startswith("mask"):
            curr_mask = line[7:]
        else:
            vals = r_mem.findall(line)
            given[curr_mask].append((int(vals[0]), int(vals[1])))
    return given


if __name__ == "__main__":
    exit(main())
