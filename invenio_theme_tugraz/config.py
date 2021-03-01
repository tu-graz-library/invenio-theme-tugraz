# -*- coding: utf-8 -*-
#
# Copyright (C) 2020 mojib wali.
#
# invenio-theme-tugraz is free software; you can redistribute it and/or
# modify it under the terms of the MIT License; see LICENSE file for more
# details.

"""invenio module for TUGRAZ theme."""

from flask_babelex import gettext as _
from invenio_app_rdm.config import RECORDS_UI_ENDPOINTS

INVENIO_THEME_TUGRAZ_DEFAULT_VALUE = _("TU Graz Repository")
"""Default value for the application."""

INVENIO_THEME_TUGRAZ_BASE_TEMPLATE = "invenio_theme_tugraz/base.html"
"""TU Graz Default base template"""

INVENIO_THEME_TUGRAZ_ACCOUNT_BASE = "invenio_theme_tugraz/accounts/accounts_base.html"
"""TU Graz Default account base template"""

INVENIO_THEME_TUGRAZ_ICON = "images/icon_use.png"
"""icon used in login page"""

INVENIO_THEME_TUGRAZ_LOGIN_IMG = "images/login_logo.png"
"""TU Logo for forms"""

# Invenio-theme
# ============
# See https://invenio-theme.readthedocs.io/en/latest/configuration.html
#
THEME_LOGO = "images/tug_logo.png"
"""TU Graz logo"""

THEME_SEARCHBAR = False
"""Enable or disable the header search bar."""

THEME_HEADER_TEMPLATE = "invenio_theme_tugraz/header.html"
"""TU Graz header template"""

THEME_FRONTPAGE = False
"""Use default frontpage."""

THEME_HEADER_LOGIN_TEMPLATE = "invenio_theme_tugraz/accounts/header_login.html"
"""login page header"""

THEME_FOOTER_TEMPLATE = "invenio_theme_tugraz/footer.html"
"""footer template"""

THEME_FRONTPAGE_TITLE = _("TU Graz Repository")
"""Frontpage title."""

THEME_SITENAME = _("Repository")
"""Site name."""

# Invenio-accounts
# ============
# See https://invenio-accounts.readthedocs.io/en/latest/configuration.html

# COVER_TEMPLATE = 'invenio_theme_tugraz/accounts/accounts_base.html'
"""Cover page template for login and sign up pages."""

SECURITY_LOGIN_USER_TEMPLATE = "invenio_theme_tugraz/accounts/login_user.html"
"""Login template"""

SECURITY_REGISTER_USER_TEMPLATE = "invenio_theme_tugraz/accounts/register_user.html"
"""Sigup template"""

# Invenio-I18N
# ============
# See https://invenio-i18n.readthedocs.io/en/latest/configuration.html
BABEL_DEFAULT_LOCALE = "en"
# Default time zone
BABEL_DEFAULT_TIMEZONE = "Europe/Vienna"
# Other supported languages (do not include BABEL_DEFAULT_LOCALE in list).
I18N_LANGUAGES = [("de", _("German"))]

# Invenio-app-rdm
# =============
# See https://invenio-app-rdm.readthedocs.io/en/latest/configuration.html
SEARCH_UI_HEADER_TEMPLATE = "invenio_theme_tugraz/header.html"
"""Search page's header template."""

DEPOSITS_HEADER_TEMPLATE = "invenio_theme_tugraz/header.html"
"""Deposits header page's template."""


# Invenio-rdm-records
# =============
# See https://invenio-rdm-records.readthedocs.io/en/latest/configuration.html
# Uncomment below to override records landingpage.
# from invenio_rdm_records.config import RECORDS_UI_ENDPOINTS
# RECORDS_UI_ENDPOINTS["recid"].update(
#     template="invenio_theme_tugraz/record_landing_page.html"
# )
"""override the default record landing page"""

# Invenio-search-ui
# =============
# See https://invenio-search-ui.readthedocs.io/en/latest/configuration.html
# SEARCH_UI_SEARCH_TEMPLATE = "invenio_theme_tugraz/search.html"
# """override the default search page"""

TUG_ROUTES = {
    "index": "/",
    "comingsoon": "/comingsoon",
}

# Invenio-app-rdm
# =============
# See https://invenio-app-rdm.readthedocs.io/en/latest/configuration.html
# """override the default search page"""
# Keep this in sync
APP_RDM_ROUTES = {
    "index": "/notvalid/notvalid/notvalid",
    "help_search": "/help/search",
    "record_search": "/search2",
    "record_detail": "/records/<pid_value>",
    "record_export": "/records/<pid_value>/export/<export_format>",
    "record_file_preview": "/records/<pid_value>/preview/<path:filename>",
    "record_file_download": "/records/<pid_value>/files/<path:filename>",
    "deposit_search": "/uploads",
    "deposit_create": "/uploads/new",
    "deposit_edit": "/uploads/<pid_value>",
}
