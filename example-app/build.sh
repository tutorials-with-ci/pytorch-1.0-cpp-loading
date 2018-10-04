#!/bin/sh
CURRENT="$( cd "$(dirname "$0")" ; pwd -P )"
cd $CURRENT

mkdir -p build
cd build
cmake -DCMAKE_PREFIX_PATH=../libtorch ..
make

./example-app ../../model.pt
