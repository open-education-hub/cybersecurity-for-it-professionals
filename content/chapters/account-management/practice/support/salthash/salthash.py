#!/usr/bin/python3

import binascii
import random
from hashlib import sha256

def hash_with_salt(password, salt, salt_prefix = True):
    if salt_prefix:
        return (salt, bytes(sha256(salt + password).hexdigest(), 'utf-8'))

    return (bytes(sha256(password + salt).hexdigest(), 'utf-8'), salt)

def generate_salt(salt_size = 5):
    return binascii.hexlify(random.randbytes(salt_size))

def salt_hash_password():
    password = bytes(input('Give me a password: '), 'utf-8')
    salt = generate_salt()

    print("Password given as input: {}".format(password))
    print("Generated salt: {}".format(salt))
    print()

    print("Salt prefix case")
    (s, h) = hash_with_salt(password, salt, True)
    print("salt + hash(salt + password) = {} + {} = {}".format(s, h, s + h))
    print()

    print("Salt suffix case")
    (h, s) = hash_with_salt(password, salt, False)
    print("hash(password + salt) + salt = {} + {} = {}".format(h, s, h + s))
    print()

def main():
    salt_hash_password()

if __name__ == '__main__':
    main()
