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
    public_keys = [int(i) for i in input_text.strip().split()]
    print(f"Public keys: {public_keys}")

    loop_sizes = []
    for key in public_keys:
        loop_sizes.append(loop(key))
    print(f"Loop sizes: {loop_sizes}")

    enc_key = public_keys[0]
    for i in range(loop_sizes[1] - 1):
        enc_key = (enc_key * public_keys[0]) % 20201227
    return enc_key


def loop(key, initial=7):
    subject = initial
    loops = 1
    while subject != key:
        loops += 1
        subject = (subject * initial) % 20201227
        if subject == key:
            return loops
    return loops


if __name__ == "__main__":
    exit(main())
