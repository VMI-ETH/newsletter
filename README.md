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
./mknewsletter.sh --date=Dec-2023
```

Date must be a directory within `./contents`.

For more information, inspect the script or run:

```sh
pipenv run python ./mkmail.py --help
```

## Sending the Newsletter

With most mail clients, you can simply open the resulting `.html` file (by default `newsletter.html`), select everything (press Cmd/Ctrl+A), copy (Cmd/Ctrl+C), and paste it (Cmd/Ctrl+V) in a new mail of your mail client of choice.
