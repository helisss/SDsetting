#!/bin/bash

#huggingface-cli login

#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
source ..venv/bin/activate

apt update
apt isntall vim
pip install wget
pip install gitpython

cp SDsetting/ui-config.json ui-config.json

python SDsetting/modeldownloader.py --set

