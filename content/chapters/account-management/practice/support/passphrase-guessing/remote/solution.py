#!/usr/bin/python3

from pwn import *
import sys

HOST = '141.85.224.104'
PORT = 20001
ARTICLES_FILE='articles.txt'
ADJECTIVES_FILE='adjectives.txt'
NOUNS_FILE='nouns.txt'

def getlines(filename):
    lines = []
    with open(filename) as f:
        lines = [x.strip() for x in f.readlines()]

    return lines

def is_right_guess(io, guess):
    io.sendline(guess)

    return io.recvline() != b'Try Again!\n'

def get_secret(io):
    return io.recv()

def break_passphrase(isLocal = 1):
    io = None

    if isLocal:
        io = remote('127.0.0.1', PORT)
    else:
        io = remote(HOST, PORT)

    io.recvuntil(b'Start playing!\n')

    articles = getlines('./articles.txt')
    adjectives = getlines('./adjectives.txt')
    nouns = getlines('./nouns.txt')

    isGuessed = False
    #TODO: stop when isGuessed is True
    #TODO: iterate over all possible combinations of article + ' ' + adjective + ' ' noun
    #TODO: use the is_right_guess() function to check each combination

    #TODO: once is_right_guess() returns true, use get_secret(io) to get the secret
    print(get_secret(io))

def main():
    isLocal = True
    if len(sys.argv) == 2:
        isLocal = bool(int(sys.argv[1]))

    break_passphrase(isLocal)

if __name__ == '__main__':
    main()
