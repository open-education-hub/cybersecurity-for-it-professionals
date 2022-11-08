#!/usr/bin/python3

import string
import itertools
import random
import sys
import time

SECRET_FILE='/home/ctf/password-guessing/secret'
PASSWORD_LEN = 3

def generate_secret_password():
    all_passwords = ["".join(x) for x in itertools.product(string.ascii_lowercase, repeat=PASSWORD_LEN)]

    return random.choice(all_passwords)

def guess_password():
    secret_password = generate_secret_password()

    print('Start playing!')

    isGuessed = False
    while not isGuessed:
        current_guess = input()

        if current_guess == secret_password:
            isGuessed = True
        else:
            print("Try Again!")

    print("Congratz! Password is: {}.".format(secret_password))

    f = open(SECRET_FILE)
    secret = f.read()
    f.close()
    print("The secret is: {}.".format(secret.strip()))

def main():
    guess_password()

if __name__ == "__main__":
    main()
