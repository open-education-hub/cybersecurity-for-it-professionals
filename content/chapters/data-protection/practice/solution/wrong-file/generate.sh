#!/bin/bash

num_files=20

for f in $(seq -f "file-%02g.dat" 0 $(($num_files-1))); do
    dd if=/dev/urandom of=../../support/wrong-file/"$f" bs=1K count=8
done
