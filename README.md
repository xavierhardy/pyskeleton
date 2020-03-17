PySkeleton
==========

PySkeleton is a skeleton Python-3 application, it follows some good practices such as:

- unit testing
- separation of concerns
- various forms of linting
- automatic formatting

Prerequisites
-------------

- Linux or macOS
- [Python 3.6 or newer](https://www.python.org/downloads)
- [Shellcheck](https://github.com/koalaman/shellcheck#installing)

Installation
------------

```sh
./install.sh
```

Usage
-----

```sh
./run.sh
```

```
usage: pyskeleton [-h] [-v | -l LOG_LEVEL]

Example application

optional arguments:
  -h, --help            show this help message and exit
  -v, --verbose         Enable debug logging
  -l LOG_LEVEL, --log_level LOG_LEVEL
                        Enable a specific level of logging (1: DEBUG, 5:
                        CRITICAL, default: INFO)
```

Tests and linting
-----------------

```sh
./check.sh
```
