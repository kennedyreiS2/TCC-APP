#!/bin/bash

d=$(pwd)

cd ./data

python dataset.py

cd "$d"

cd ./src

rm -r ./runs

python train.py
