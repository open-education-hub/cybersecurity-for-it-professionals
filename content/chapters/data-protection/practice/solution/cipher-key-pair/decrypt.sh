#!/bin/bash

num=20

pushd ../../support/cipher-key-pair/ > /dev/null
for i in $(seq -f "%02g" 0 $(($num-1))); do
    openssl enc -d -aes-256-cbc -K $(cat key-"$i".txt) -iv $(cat iv-"$i".txt) -in file-"$i".enc -out file-"$i".dec
    cmp file-"$i".dec file-"$i".txt || echo "file-$i.txt"
done
popd > /dev/null
