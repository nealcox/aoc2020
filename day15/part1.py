import re
import sys


TURNS = 2020


def main():
    if len(sys.argv) > 1:
        filename = sys.argv[1]
    else:
        filename = "input.txt"
    with open(filename) as f:
        input_text = f.read().strip()
    print(f"Answer: {calculate(input_text)}")


def calculate(input_text):
    nums = get_nums(input_text)
    last = {}
    prev = {}
    for i in range(TURNS):
        if nums:
            num = nums.pop(0)
            spoken = num
        else:
            if spoken in prev:
                spoken = last[spoken] - prev[spoken]
            else:
                spoken = 0
        if spoken in last:
            prev[spoken] = last[spoken]
        last[spoken] = i
    return spoken


def get_nums(s):
    r = re.compile(r"\d+")
    return [int(i) for i in r.findall(s)]


if __name__ == "__main__":
    exit(main())
