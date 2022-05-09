# Weather API

Create a weather API in Python.

external API: openweathermap

Consume external API and create a human readable response for city/country pair using a get request.

Note: Globant test.

# Use

## Set python environment

use the `bash_create_environ.sh` script for create the python environment.

```
bash bash_create_environ.sh
```

You can see inside the script for the step by step commands.


## Set environ variable and play

use the `bash_set_env_and_play.sh` script for setting the environment variables and play the application

```
bash bash_set_env_and_play.sh
```

Use a normal web browser to check the application:

example:

```
http://127.0.0.1:8000/weather?city=bogota&country=co
```

# Description

## Some ranges for human readable

Some information about ranges were taken from the following links:

#### [Wind speed ranges](https://www.nationalgeographic.org/encyclopedia/beaufort-scale/)

#### [cloudiness ranges](https://www.researchgate.net/figure/Calculation-of-cloudiness-in-percentage-for-corresponding-okta-values_tbl1_331176763)