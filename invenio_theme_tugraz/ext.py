# -*- coding: utf-8 -*-
#
# Copyright (C) 2020-2024 Graz University of Technology.
#
# invenio-theme-tugraz is free software; you can redistribute it and/or
# modify it under the terms of the MIT License; see LICENSE file for more
# details.

"""invenio module for TUGRAZ theme."""

from flask_login import login_required
from invenio_i18n import lazy_gettext as _
from invenio_records_marc21.ui.theme import current_identity_can_view

from . import config
from .views import index, locked, require_tugraz_authenticated


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
        self.init_config(app)

        app.register_error_handler(423, locked)

        @app.context_processor
        def inject_visibility():
            return {"can_view_marc21": current_identity_can_view()}

        app.extensions["invenio-theme-tugraz"] = self

    def init_config(self, app):
        """Initialize configuration."""
        for k in dir(config):
            if k.startswith("INVENIO_THEME_TUGRAZ_") or k.startswith("THEME_TUGRAZ_"):
                app.config.setdefault(k, getattr(config, k))


def finalize_app(app):
    """Finalize app."""
    modify_user_dashboard(app)
    guard_view_functions(app)


def modify_user_dashboard(app):
    """Modify user dashboard."""
    root_menu = app.extensions["menu"].root_node

    user_dashboard_menu = root_menu.submenu("dashboard")
    user_dashboard_menu.submenu("overview").register(
        "invenio_theme_tugraz.overview",
        text=_("Overview"),
        order=0,
    )

    root_menu.submenu("actions.deposit").register(
        "invenio_theme_tugraz.overview",
        _("My dashboard"),
        order=1,
    )


def guard_view_functions(app):
    """Guard view-functions against unauthenticated access."""
    endpoints_to_guard = [
        "invenio_app_rdm_users.communities",
        "invenio_app_rdm_users.requests",
        "invenio_app_rdm_users.uploads",
    ]

    for endpoint in endpoints_to_guard:
        view_func = app.view_functions.get(endpoint)
        if not view_func:
            continue

        # decorate view-func
        # same as if view-func were defined with:
        #   @login_required
        #   @require_tugraz_authenticated_user
        view_func = login_required(
            require_tugraz_authenticated(
                view_func,
            ),
        )

        app.view_functions[endpoint] = view_func
