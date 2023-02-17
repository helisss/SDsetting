#!/bin/bash
source venv.sh

apt update
apt install vim -Y

pip install wget
pip install gitpython

cp SDsetting/ui-config.json ui-config.json
cp SDsetting/config.json config.json
cp -r SDsetting/wildcards/* extensions/stable-diffusion-webui-wildcards/wildcards
cp SDsetting/styles.csv styles.csv

python SDsetting/modeldownloader.py --set

