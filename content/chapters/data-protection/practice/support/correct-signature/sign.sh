#!/bin/bash

num=20

for f in $(seq -f "file-%02g.txt" 0 $(($num-1))); do
    gpg --armor --output $(basename "$f" .txt).sig --detach-sign "$f"
done
