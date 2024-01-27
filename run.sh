#!/bin/bash

d=$(pwd)

cd ./data

python dataset.py

cd "$d"

cd ./src

python train.py
