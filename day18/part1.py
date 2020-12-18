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
    answer = 0
    given = get_re(input_text)
    for line in given:
        if "(" in line:
            open_parens = []
            parens = []
            for i, token in enumerate(line):
                if token == "(":
                    open_parens.append(i)
                elif token == ")":
                    pair = (open_parens.pop(), i)
                    parens.append(pair)
            for s, e in parens:
                to_eval = [t for t in line[s + 1 : e] if t != "X"]
                line[s : e + 1] = "X" * (e - s + 1)
                line[s] = evaluate(to_eval)
        answer += evaluate([t for t in line if t != "X"])
    return answer


def evaluate(l):
    first = l.pop(0)
    while l:
        op = l.pop(0)
        second = l.pop(0)
        if op == "+":
            first = first + second
        elif op == "*":
            first = first * second
        else:
            raise ValueError(f"Illegal operator {op}")
    return first


def get_re(s):
    given = []
    r = re.compile(r"\d+|\+|\*|\(|\)")
    for line in s.split("\n"):
        res = []
        for i in r.findall(line):
            if i.isnumeric():
                res.append(int(i))
            else:
                res.append(i)
        given.append(res)
    return given


if __name__ == "__main__":
    exit(main())
