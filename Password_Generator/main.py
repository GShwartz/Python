from collections import Counter
import argparse
import string
import random


def generate_password(length):
    for i in range(int(length)):
        if len(password) >= int(length):
            break

        password.append(random.choice(letter_chars))
        password.append(random.choice(numbers_chars))
        password.append(random.choice(special_chars))

    counter = Counter(password)
    while True:
        for k, v in counter.items():
            if int(v) > 1:
                print(f"{k} found more than once, replacing...")
                for char in password:
                    if str(char) == str(k):
                        if str(k) not in dups:
                            dups.append(k)
                            password.remove(k)
                            print(f"removed {k} from list")

                if len(password) < int(length):
                    for i in range(int(length) - len(password)):
                        res = random.choice(mixed)
                        if str(res) not in dups and str(res) not in password:
                            password.append(res)

        return


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Random password generator")
    parser.add_argument('-n', '--length', default=12, help="Number of characters")
    args = parser.parse_args()

    letter_chars = list(string.ascii_letters)
    numbers_chars = list(string.digits)
    special_chars = list("!@#$%^&*_+")
    mixed = list(string.ascii_letters + string.digits + "!@#$%^&*_+()[]{}<>")
    dups = []
    password = []

    generate_password(args.length)
    print("".join(password))
