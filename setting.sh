#!/bin/bash
source ../venv/bin/activate

apt update
apt install vim
apt install vim -y

pip install wget
pip install gitpython

cp SDsetting/ui-config.json ui-config.json

python SDsetting/modeldownloader.py --set

