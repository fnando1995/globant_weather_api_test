# Weather API

Create a weather API in Python.

external API: openweathermap

Consume external API and create a human readable response for city/country pair using a get request.

Note: Globant test.

# install redis

For installing redis follow this simpe [tutorial](https://www.digitalocean.com/community/tutorials/como-instalar-y-proteger-redis-en-ubuntu-18-04-es)

# Use

## Set python environment

use the `bash_create_environ.sh` script for create the python environment.

```
bash bash_create_environ.sh
```

You can see inside the script for the step by step commands.


## Play app

Use the `bash_set_env_and_play.sh` script for setting the environment variables, start redis server and play the application. redis-server configuration files is at `data/`, the cached data will be stored at `data/cache.rdb`. 

```
bash bash_set_env_and_play.sh
```

Use a normal web browser to check the application:

example:

```
http://127.0.0.1:8000/weather?city=bogota&country=co
```

Note: cached data will be deleted after CACHE_TIME_SECONDS seconds.

## Play test

For make all the tests first initiate the app in one terminal and the test in other terminal:

```
# terminal 1
bash bash_set_env_and_play.sh
```

```
# terminal 1
bash bash_test.sh
```

# Description

## Some ranges for human readable

Some information about ranges were taken from the following links:

#### [Wind speed ranges](https://www.nationalgeographic.org/encyclopedia/beaufort-scale/)

#### [cloudiness ranges](https://www.researchgate.net/figure/Calculation-of-cloudiness-in-percentage-for-corresponding-okta-values_tbl1_331176763)