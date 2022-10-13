# -*- coding: utf-8 -*-
#
# Copyright (C) 2020-2021 Graz University of Technology.
#
# invenio-theme-tugraz is free software; you can redistribute it and/or
# modify it under the terms of the MIT License; see LICENSE file for more
# details.

"""Frontpage records."""

from invenio_search.api import RecordsSearch
from invenio_search.engine import dsl


class FrontpageRecordsSearch(RecordsSearch):
    """Search class for records that goes on the frontpage."""

    class Meta:
        """Default index and filter for frontpage search."""

        index = "rdmrecords-records"
        default_filter = dsl.Q(
            "query_string",
            query=("access.record:public " "AND versions.is_latest:true"),
        )
