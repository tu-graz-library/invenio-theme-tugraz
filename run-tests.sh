#!/usr/bin/env sh
# -*- coding: utf-8 -*-
#
# Copyright (C) 2020 mojib wali.
#
# invenio-theme-tugraz is free software; you can redistribute it and/or
# modify it under the terms of the MIT License; see LICENSE file for more
# details.

docker-services-cli up postgresql es redis
python -m check_manifest --ignore ".travis-*" && \
python -m sphinx.cmd.build -qnNW docs docs/_build/html && \
docker-services-cli up es postgresql redis
python -m pytest
tests_exit_code=$?
docker-services-cli down
exit "$tests_exit_code"