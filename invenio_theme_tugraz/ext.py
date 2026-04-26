# -*- coding: utf-8 -*-
#
# Copyright (C) 2020-2026 Graz University of Technology.
#
# invenio-theme-tugraz is free software; you can redistribute it and/or
# modify it under the terms of the MIT License; see LICENSE file for more
# details.

"""invenio module for TUGRAZ theme."""

from invenio_i18n import lazy_gettext as _

from . import config


class InvenioThemeTugraz(object):
    """invenio-theme-tugraz extension."""

    def __init__(self, app=None):
        """Extension initialization."""
        if app:
            self.init_app(app)

    def init_app(self, app):
        """Flask application initialization."""
        self.init_config(app)
        app.extensions["invenio-theme-tugraz"] = self

    def init_config(self, app):
        """Initialize configuration."""
        for k in dir(config):
            if (
                k.startswith("DEPOSITS_")
                or k.startswith("OVERRIDE_")
                or k.startswith("SEARCH_")
                or k.startswith("SECURITY__")
                or k.startswith("THEME_")
            ):
                # this is intentionally a `=` and not a `setdefault`. with this
                # style it is ensured that this package provides the
                # configuration variables to configure the layout
                app.config[k] = getattr(config, k)
