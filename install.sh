#!/bin/bash
python3 -m venv env
source ./env/bin/activate
pip3 install -r requirements.txt
echo $'\n'
echo $'\n'

python learn_tables.py