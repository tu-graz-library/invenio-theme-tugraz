#!/usr/bin/env bash
# -*- coding: utf-8 -*-
#
# Copyright (C) 2019-2020 CERN.
# Copyright (C) 2019-2020 Northwestern University.
# Copyright (C) 2020-2021 Graz University of Technology.
#
# invenio-theme-tugraz is free software; you can redistribute it and/or
# modify it under the terms of the MIT License; see LICENSE file for more
# details.


# Quit on errors
set -o errexit

# Quit on unbound symbols
set -o nounset

python -m check_manifest --ignore ".*-requirements.txt"
python -m sphinx.cmd.build -qnN docs docs/_build/html
python -m pytest
tests_exit_code=$?
python -m sphinx.cmd.build -qnN -b doctest docs docs/_build/doctest
exit "$tests_exit_code"
