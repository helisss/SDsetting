#!/bin/bash

#huggingface-cli login

#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
source ../venv/bin/activate

apt update
apt isntall vim
pip install wget
pip install gitpython

python SDsetting/modeldownloader.py --set

#git add . && git commit -m "Update from $USER"
#git push
