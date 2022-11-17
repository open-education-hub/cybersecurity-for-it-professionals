#!/bin/bash

num=20

for i in $(seq -f "%02g" 0 $(($num-1))); do
    openssl enc -aes-256-cbc -K $(cat key-"$i".txt) -iv $(cat iv-"$i".txt) -in file-"$i".txt -out file-"$i".enc
done

