#!/bin/bash
# move to project root dir
HERE=$(cd $(dirname $BASH_SOURCE) && pwd)
cd $HERE/../
# set environmet variables
export API_ID=1508a9a4840a5574c822d70ca2132032
export API_URL_FORMAT="https://api.openweathermap.org/data/2.5/weather?q={},{}&appid={}"
export FLASK_HOST=0.0.0.0
export FLASK_PORT=8000
export CACHE_TIME_SECONDS=120
redis-server ./data/redis.conf
# turn python environment ON
source ambiente/bin/activate
# play app
python app.py
# turn python environment OFF
deactivate
redis-cli shutdown