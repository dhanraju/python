#!/usr/bin/env bash

pip3 install virtualenv

whereis virtualenv

virtualenv testenv -p /usr/bin/python3

# . ~/.virtualenvs/python3/bin/activate
set -e
set -x

rm -f pep8.log pyflakes.log

./number_system_xmlrunner.py

# Install pep8 tool.
# $ sudo apt install pep8
pep8 --max-line-length=80 ./ > pep8.log || true

# Install pyflakes tool.
# $ sudo pip install --upgrade pyflakes
pyflakes ./ > pyflakes.log || true
