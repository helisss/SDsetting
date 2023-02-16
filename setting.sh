#!/bin/bash

#huggingface-cli login

#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
source ../venv/bin/activate

apt update
apt install vim
pip install wget
pip install gitpython

cp SDsetting/ui-config.json ui-config.json

python SDsetting/modeldownloader.py --set

#git add . && git commit -m "Update from $USER"
#git push
