#!/bin/bash
# move to project root dir
HERE=$(cd $(dirname $BASH_SOURCE) && pwd)
cd $HERE/../
# set environmet variables
export GLOBANT_API_URL_FORMAT="http://127.0.0.1:8000/weather?city={}&country={}"
# turn python environment ON
source ambiente/bin/activate
# play test
python test.py
# turn python environment OFF
deactivate