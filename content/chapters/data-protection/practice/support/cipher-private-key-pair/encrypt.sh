#!/bin/bash

num=20

for i in $(seq -f "%02g" 0 $(($num-1))); do
    openssl rsautl -encrypt -inkey pub-"$i".pem -pubin -in file-"$i".txt -out file-"$i".enc
done
