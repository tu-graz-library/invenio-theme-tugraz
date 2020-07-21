# -*- coding: utf-8 -*-
#
# Copyright (C) 2020 mojib wali.
#
# invenio-theme-tugraz is free software; you can redistribute it and/or
# modify it under the terms of the MIT License; see LICENSE file for more
# details.

"""invenio module for TUGRAZ theme."""

from flask import Blueprint, render_template
from flask_babelex import gettext as _

from .search import FrontpageRecordsSearch

blueprint = Blueprint(
    'invenio_theme_tugraz',
    __name__,
    template_folder='templates',
    static_folder='static',
)


@blueprint.route("/")
def index():
    """Render frontpage view."""
    return render_template(
        "invenio_theme_tugraz/index.html",
        records=FrontpageRecordsSearch()[:5].sort('-_created').execute(),)
