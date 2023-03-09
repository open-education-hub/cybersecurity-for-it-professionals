#!/bin/bash

echo "Inspecting checksums ..."
echo ""
pushd ../../support/wrong-file/ > /dev/null
sha256sum --check SHA256SUMS
popd > /dev/null

echo ""
echo "Correct checksums are ..."
echo ""
pushd ../../support/wrong-file/ > /dev/null
sha256sum *.dat
popd > /dev/null
