#!/usr/bin/env python3

import hashlib

FLAG = "it is a worse day to die"

parts = [FLAG[i:i+3] for i in range(0, len(FLAG), 3)]

for p in parts:
    print(hashlib.sha256(p.encode('utf-8')).hexdigest())
