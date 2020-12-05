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
        if (len(batch) == 8) or (len(batch) == 7 and "cid" not in batch):
            if (valid_byr(batch["byr"]) and
               valid_iyr(batch["iyr"]) and
               valid_eyr(batch["eyr"]) and
               valid_hgt(batch["hgt"]) and
               valid_hcl(batch["hcl"]) and
               valid_ecl(batch["ecl"]) and
               valid_pid(batch["pid"])):
               answer += 1


    return answer

def valid_byr(s):
    if s.isnumeric():
        i = int(s)
        if 1920 <= i <= 2002:
            return True
    return  False

def valid_iyr(s):
    if s.isnumeric():
        i = int(s)
        if 2010 <= i <= 2020:
            return True
    return  False

def valid_eyr(s):
    if s.isnumeric():
        i = int(s)
        if 2020 <= i <= 2030:
            return True
    return False

def valid_hgt(s):
    if len(s) > 2:
        units = s[-2:]
        s = s[:-2]
    if len(s) >0 and s.isnumeric():
        i = int(s)
        if units == "in":
            if 59 <= i <= 76:
                return True
        elif units == "cm":
            if 150 <= i <= 193:
                return True
    return False


def valid_hcl(s):
    if len(s) >1 and s[0] == "#":
        valid = True
        for char in s[1:]:
            if char not in "0123456789abcdef":
                return False
        return True
    return False

def valid_ecl(s):
    if s in ("amb","blu","brn","gry","grn","hzl","oth"):
        return True
    return False

def valid_pid(s):
    if len(s) == 9 and s.isnumeric():
        return True
    return False


def setup(filename):
    given = []
    with open(filename) as f:
        passports = f.read().strip().split("\n\n")
        for passport in passports:
            batch = {}
            details = passport.split()
            for detail in details:
                k,v = detail.split(":")
                batch[k] = v
            given.append(batch)
                
    return given



if __name__ == "__main__":
    exit(main())
