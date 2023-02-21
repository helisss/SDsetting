#!/bin/bash
#source venv.sh

apt update
apt -y install vim zip

pip install wget
pip install gitpython

cp SDsetting/ui-config.json ui-config.json
cp SDsetting/config.json config.json

python SDsetting/modeldownloader.py --set

#cp SDsetting/styles.csv styles.csv

cp -r SDsetting/wildcards/* extensions/sd-dynamic-prompts/wildcards

cp SDsetting/relauncher.py relauncher.py

