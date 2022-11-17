#!/usr/bin/env python3

import itertools
import hashlib
import string

f = open("../../support/3-letters-sha256/hashed_flag", "r")
hashes = [line.strip() for line in f.readlines()]

parts = [""] * len(hashes)

for pair in itertools.product(string.ascii_lowercase + ' ', repeat=3):
    v = ''
    for p in pair:
        v = v + p
    h = hashlib.sha256(v.encode('utf-8')).hexdigest()
    if h in hashes:
        idx = hashes.index(h)
        parts[idx] = v

print("Flag is '{}'".format("".join(p for p in parts)))
