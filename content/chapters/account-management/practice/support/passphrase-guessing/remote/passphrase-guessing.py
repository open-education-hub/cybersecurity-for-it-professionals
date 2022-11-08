#!/usr/bin/python3

import random

ARTICLES_FILE='/home/ctf/passphrase-guessing/articles.txt'
ADJECTIVES_FILE='/home/ctf/passphrase-guessing/adjectives.txt'
NOUNS_FILE='/home/ctf/passphrase-guessing/nouns.txt'
SECRET_FILE='/home/ctf/passphrase-guessing/secret'

def getlines(filename):
    lines = []
    with open(filename) as f:
        lines = [x.strip() for x in f.readlines()]

    return lines

def generate_secret_passhprase():
    articles = getlines(ARTICLES_FILE)
    adjectives = getlines(ADJECTIVES_FILE)
    nouns = getlines(NOUNS_FILE)

    return random.choice(articles) + ' ' + random.choice(adjectives) + ' ' + random.choice(nouns)

def guess_passphrase():
    secret_passhprase = generate_secret_passhprase()

    print('Start playing!')

    isGuessed = False
    while not isGuessed:
        current_guess = input()

        if current_guess == secret_passhprase:
            isGuessed = True
        else:
            print("Try Again!")

    print("Congratz! Passphrase is: {}.".format(secret_passhprase))

    f = open(SECRET_FILE)
    secret = f.read()
    f.close()
    print("The secret is: {}.".format(secret.strip()))

def main():
    guess_passphrase()

if __name__ == '__main__':
    main()
