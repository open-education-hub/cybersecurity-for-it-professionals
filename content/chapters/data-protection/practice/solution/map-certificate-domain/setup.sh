#!/bin/bash

domains=("facebook.com" "google.com" "amazon.com" "nvidia.com" "intel.com" "microsoft.com" "apple.com" "dell.com")

for i in $(seq 0 $((${#domains[@]}-1))); do
    d=${domains[$i]}
    echo "" | timeout 5 openssl s_client -showcerts -servername "${d}" \
                -connect "${d}":443 |\
                sed -ne '/-BEGIN CERTIFICATE-/,/-END CERTIFICATE-/p' > ../../support/map-certificate-domain/"cert"-"$i".pem
done
