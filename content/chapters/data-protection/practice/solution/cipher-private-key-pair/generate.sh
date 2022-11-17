#!/bin/bash

num=20

for f in $(seq -f "file-%02g.txt" 0 $(($num-1))); do
    tr -dc a-z < /dev/urandom | head -c 20 > ../../support/cipher-private-key-pair/"$f"
done

for i in $(seq -f "%02g" 0 $(($num-1))); do
    openssl genrsa -out ../../support/cipher-private-key-pair/priv-"$i".pem 1024
    openssl rsa -in ../../support/cipher-private-key-pair/priv-"$i".pem -pubout > ../../support/cipher-private-key-pair/pub-"$i".pem
done
