# -*- coding: utf-8 -*-
#
# Copyright (C) 2020-2021 Graz University of Technology.
#
# invenio-theme-tugraz is free software; you can redistribute it and/or
# modify it under the terms of the MIT License; see LICENSE file for more
# details.

"""Pytest configuration.

See https://pytest-invenio.readthedocs.io/ for documentation on which test
fixtures are available.
"""

import pytest
from flask import Flask
from invenio_i18n import InvenioI18N

from invenio_theme_tugraz import InvenioThemeTugraz


@pytest.fixture()
def app(request):
    """Basic Flask application."""
    app = Flask("testapp")
    app.config.update(
        I18N_LANGUAGES=[("en", "English"), ("de", "German")],
    )
    InvenioThemeTugraz(app)
    InvenioI18N(app)

    return app
