#!/usr/bin/env bash

. ~/.virtualenvs/python3/bin/activate
set -e
set -x

rm -f pep8.log pyflakes.log

./test.py

pep8 --max-line-length=120 python > pep8.log || true

pyflakes python > pyflakes.log || true
