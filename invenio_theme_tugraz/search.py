# -*- coding: utf-8 -*-
#
# Copyright (C) 2020 TU Graz.
# Copyright (C) 2020 mojib wali.
#
# invenio-theme-tugraz is free software; you can redistribute it and/or
# modify it under the terms of the MIT License; see LICENSE file for more
# details.

"""Frontpage records."""

from __future__ import absolute_import, print_function

from elasticsearch_dsl.query import Q
from invenio_search.api import RecordsSearch


class FrontpageRecordsSearch(RecordsSearch):
    """Search class for records that goes on the frontpage."""

    class Meta:
        """Default index and filter for frontpage search."""

        index = "rdmrecords-records"
        default_filter = Q("query_string", query=("access.access_right:open"))
