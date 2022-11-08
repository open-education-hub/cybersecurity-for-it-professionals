#!/usr/bin/python3

import time

SECRET_FILE='/home/ctf/sidechannel/secret'

def generate_secret_password():
    password = ''
    with open(SECRET_FILE) as f:
        password = f.read().strip()

    return password

def is_right_guess(secret_password, current_guess):
    length = min(len(secret_password), len(current_guess))

    for i in range(length):
        if secret_password[i] != current_guess[i]:
            return False
        else:
            time.sleep(0.2)

    if len(secret_password) != len(current_guess):
        return False

    return True

def guess_password():
    secret_password = generate_secret_password()

    print('Start playing!')

    isGuessed = False
    while not isGuessed:
        current_guess = input()

        start_time = time.time()
        if is_right_guess(secret_password, current_guess):
            isGuessed = True
        else:
            print("Try Again! Seconds taken by the verification process: {}".format(time.time() - start_time))

    print("Congratz! Password is: {}.".format(secret_password))

def main():
    guess_password()

if __name__ == '__main__':
    main()
