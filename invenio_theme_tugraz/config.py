# -*- coding: utf-8 -*-
#
# Copyright (C) 2020 mojib wali.
#
# invenio-theme-tugraz is free software; you can redistribute it and/or
# modify it under the terms of the MIT License; see LICENSE file for more
# details.

"""invenio module for TUGRAZ theme."""

from flask_babelex import gettext as _

INVENIO_THEME_TUGRAZ_DEFAULT_VALUE = 'foobar'
"""Default value for the application."""

INVENIO_THEME_TUGRAZ_BASE_TEMPLATE = 'invenio_theme_tugraz/base.html'
"""Default base template for the demo page."""

THEME_LOGO = 'images/tug_logo.png'
"""TU Graz logo"""

THEME_HEADER_TEMPLATE = 'invenio_theme_tugraz/header.html'
"""TU Graz header template"""

THEME_FRONTPAGE_TEMPLATE = 'invenio_theme_tugraz/frontpage.html'
"""Frontpage template"""

SECURITY_LOGIN_USER_TEMPLATE = 'invenio_theme_tugraz/accounts/login.html'
"""Login template"""

THEME_HEADER_LOGIN_TEMPLATE = 'invenio_theme_tugraz/accounts/header_login.html'
"""login page header"""

THEME_FOOTER_TEMPLATE = 'invenio_theme_tugraz/footer.html'
"""footer template"""

INVENIO_THEME_TUGRAZ_ICON = 'images/icon_use.png'
"""icon used in login page"""

THEME_FRONTPAGE_TITLE = _('Frontpage Title')
"""Frontpage title."""

THEME_SITENAME = _('Application Name')
"""Site name."""

SECURITY_REGISTER_USER_TEMPLATE = \
    'invenio_theme_tugraz/accounts/register_user.html'

# Invenio-I18N
# ============
# See https://invenio-i18n.readthedocs.io/en/latest/configuration.html
BABEL_DEFAULT_LOCALE = 'en'
# Default time zone
BABEL_DEFAULT_TIMEZONE = 'Europe/Vienna'
# Other supported languages (do not include BABEL_DEFAULT_LOCALE in list).
I18N_LANGUAGES = [
     ('de', _('German'))
 ]

# Invenio-APP-RDM
# =============
SEARCH_UI_HEADER_TEMPLATE = 'invenio_theme_tugraz/header.html'
"""Search page's header template."""

DEPOSITS_HEADER_TEMPLATE = 'invenio_theme_tugraz/header.html'
"""Deposits header page's template."""
