#!/bin/bash
# move to project root dir
HERE=$(cd $(dirname $BASH_SOURCE) && pwd)
cd $HERE/../
# create python environment
python3 -m venv ambiente
# activate environment
source ambiente/bin/activate
# install requirements from file
pip install -r requirements.txt
# deactivate environment
deactivate