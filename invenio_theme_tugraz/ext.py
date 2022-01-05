# -*- coding: utf-8 -*-
#
# Copyright (C) 2020-2022 Graz University of Technology.
#
# invenio-theme-tugraz is free software; you can redistribute it and/or
# modify it under the terms of the MIT License; see LICENSE file for more
# details.

"""invenio module for TUGRAZ theme."""

from invenio_theme_tugraz.deposits import deposit_create, deposit_edit

from . import config
from .views import index


class InvenioThemeTugraz(object):
    """invenio-theme-tugraz extension."""

    def __init__(self, app=None):
        """Extension initialization."""
        if app:
            self.init_app(app)

    def init_app(self, app):
        """Flask application initialization."""
        # add index route rule
        # https://flask.palletsprojects.com/en/1.1.x/api/#flask.Flask.add_url_rule
        app.add_url_rule("/", "index", index)
        app.add_url_rule("/uploads/new", "deposit_create", deposit_create)
        app.add_url_rule("/uploads/<pid_value>", "deposit_edit", deposit_edit)
        self.init_config(app)
        app.extensions["invenio-theme-tugraz"] = self

    def init_config(self, app):
        """Initialize configuration."""
        for k in dir(config):
            if k.startswith("INVENIO_THEME_TUGRAZ_") or k.startswith("THEME_TUGRAZ_"):
                app.config.setdefault(k, getattr(config, k))
