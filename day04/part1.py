import sys


def main():
    if len(sys.argv) > 1:
        input_file = sys.argv[1]
    else:
        input_file = "input.txt"
    given = setup(input_file)

    print(f"Answer: {run(given)}")


def run(given):
    answer = 0
    for batch in given:
        if len(batch) == 8:
            answer += 1
        elif "hgt" not in batch:
            pass
        elif len(batch) == 7 and "cid" not in batch:
            answer += 1
    return answer


def setup(filename):
    given = []
    with open(filename) as f:
        passports = f.read().strip().split("\n\n")
        for passport in passports:
            batch = {}
            details = passport.split()
            for detail in details:
                k, v = detail.split(":")
                batch[k] = v
            given.append(batch)
    return given


if __name__ == "__main__":
    exit(main())
