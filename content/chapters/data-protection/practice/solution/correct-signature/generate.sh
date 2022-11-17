#!/bin/bash

num=20

for f in $(seq -f "file-%02g.txt" 0 $(($num-1))); do
    tr -dc a-z1-4 </dev/urandom | tr 1-2 ' \n' | awk 'length==0 || length>10' | tr 3-4 ' ' | sed 's/^ *//' | cat -s | sed 's/ / /g' | fmt | head -20 > ../../support/correct-signature/"$f"
done
