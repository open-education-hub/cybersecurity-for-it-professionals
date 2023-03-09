#!/bin/bash

num=20

pushd ../../support/correct-signature/ > /dev/null
for i in $(seq -f "%02g" 0 $(($num-1))); do
    gpg --armor --verify file-"$i".sig file-"$i".txt || echo file-"$i".txt
done
popd > /dev/null
