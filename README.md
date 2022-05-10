# Weather API

Create a weather API in Python.

External API: openweathermap

Consume external API and create a human readable response for city/country pair using a get request.

Note: Globant test in linux environment.

# install redis

```
sudo apt install redis-server
```

Configurations used from file `data/redis.conf`, no more steps need.


# Use

## Set python environment

use the `shells/create_environ.sh` script for create the python environment.

```
bash shells/create_environ.sh
```

You can see inside the script for the step by step commands.


## Play app

Use the `shells/run_app.sh` script for setting the environment variables, start redis server and play the application. redis-server configuration file is `data/redis.conf`. the cached data will be stored at `data/cache.rdb`. Cached data will be deleted after CACHE_TIME_SECONDS (environment variable) seconds. All environment variables are exported using shell scripts, you can take a look by opening the .sh file at `shells/*.sh`

```
bash shells/run_app.sh
```

Use a normal web browser to check the application:

app url: http://127.0.0.1:8000/weather

arguments:

- city: city as an aphabetical string only
- country: Country as an alphabetical string in format iso2 only.


example:

```
http://127.0.0.1:8000/weather?city=guayaquil&country=ec
```

## Play test

For make all the tests first initiate the app in one terminal and the test in other terminal:

```
# terminal 1
bash shells/run_app.sh
```

```
# terminal 2
bash shells/test.sh
```

# Notes

## Some ranges for human readable

Some information about ranges were taken from the following links. (ranges are shown in `data/ranges.json`)

#### [Wind speed ranges](https://www.nationalgeographic.org/encyclopedia/beaufort-scale/)

#### [cloudiness ranges](https://www.researchgate.net/figure/Calculation-of-cloudiness-in-percentage-for-corresponding-okta-values_tbl1_331176763)