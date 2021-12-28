#!/usr/bin/env bash
set -e 

# . ~/.virtualenvs/python3/bin/activate

bazel test bazel/example01/main:helloworld_test
bazel test maths:number_system_conversion_test --test_verbose_timeout_warnings
