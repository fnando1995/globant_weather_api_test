#!/bin/bash
# create python environmente
python3 -m venv ambiente
# activate environment
source ambiente/bin/activate
# install requirements from file
pip install -r requirements.txt
# deactivate environment
deactivate