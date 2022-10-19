# VMI Newsletter

This repository contains a python script that can generate a newsletter-like .html document.

## Prerequisites

You need to [install python](https://www.python.org/downloads/) and [install Pipenv](https://github.com/pypa/pipenv#installation).
Pipenv is a tool that manages python dependencies in a virtualized environment.

After you have installed Pipenv, navigate into this folder and run:

```sh
pipenv install
```

## Compiling a Newsletter

To compile a newsletter, run:

```sh
pipenv run python ./mkmail.py --date DATE
```

Date must be a directory within `./contents`.

For more information, run:

```sh
pipenv run python ./mkmail.py --help
```
