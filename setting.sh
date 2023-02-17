#!/bin/bash
source venv.sh

apt update
apt -y install vim

pip install wget
pip install gitpython

python SDsetting/modeldownloader.py --set

cp SDsetting/ui-config.json ui-config.json
cp SDsetting/config.json config.json
#cp SDsetting/styles.csv styles.csv

cp -r SDsetting/wildcards/* extensions/stable-diffusion-webui-wildcards/wildcards

