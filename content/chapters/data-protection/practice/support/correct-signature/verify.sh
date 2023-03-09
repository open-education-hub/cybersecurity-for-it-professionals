#!/bin/bash

num=20

for f in $(seq -f "file-%02g.sig" 0 $(($num-1))); do
    gpg --armor --verify "$f" $(basename "$f" .sig).txt
done
