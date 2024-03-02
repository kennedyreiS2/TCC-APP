#!/bin/bash

ENV_NAME="env"

conda create -y -n $ENV_NAME python=3.10

source activate $ENV_NAME

pip install -r requirements.txt
