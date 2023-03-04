#!/usr/bin/env bash

. ~/.virtualenvs/python3/bin/activate
set -e
set -x

rm -f pep8.log pyflakes.log

# ./number_system_xmlrunner.py

# Install pep8 tool.
# $ sudo apt install pep8
pep8 --max-line-length=80 ./ > pep8.log || true

# Install pyflakes tool.
# $ pip install --upgrade pyflakes
pyflakes python > pyflakes.log || true
