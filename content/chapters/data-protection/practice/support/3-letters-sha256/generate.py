#!/usr/bin/env python3

import hashlib
import itertools
import string

for pair in itertools.product(string.ascii_lowercase + ' ', repeat=3):
    v = ''
    for p in pair:
        v = v + p
    print("{}: {}".format(v, hashlib.sha256(v.encode('utf-8')).hexdigest()))
