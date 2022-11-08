#!/usr/bin/python3

from pwn import *
import sys
import itertools
import random
import string

HOST = '141.85.224.104'
PORT = 20002

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
    #TODO: stop when isGuessed is True
    #TODO: iterate over all possibilities for the first letter
    #TODO: use the is_right_guess() function to measure which letter takes the most amount of time
    #TODO: save that letter and proceed with the next

    #TODO: the result is the secret


def main():
    isLocal = True
    if len(sys.argv) == 2:
        isLocal = bool(int(sys.argv[1]))

    break_password(isLocal)

if __name__ == '__main__':
    main()
