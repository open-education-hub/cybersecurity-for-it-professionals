#!/bin/bash

num=8

pushd ../../support/map-certificate-domain/ > /dev/null
for i in $(seq -f "%01g" 0 $(($num-1))); do
    openssl x509 -in cert-"$i".pem -noout -text | grep '\(Subject\|DNS\)'
done
popd > /dev/null
