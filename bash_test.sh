#!/bin/bash
# set environmet variables
export GLOBANT_API_URL_FORMAT="http://127.0.0.1:8000/weather?city={}&country={}"
# turn python environment ON
source ambiente/bin/activate
# play test
python test.py
# turn python environment OFF
deactivate