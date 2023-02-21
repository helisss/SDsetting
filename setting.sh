#!/bin/bash
#source venv.sh


pip install wget
pip install gitpython

python SDsetting/modeldownloader.py --set

cp -r SDsetting/wildcards/* extensions/sd-dynamic-prompts/wildcards

cp SDsetting/relauncher.py relauncher.py

