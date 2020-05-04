# -*- coding: utf-8 -*-
#
# Copyright (C) 2020 mojib wali.
#
# invenio-theme-tugraz is free software; you can redistribute it and/or
# modify it under the terms of the MIT License; see LICENSE file for more
# details.

"""invenio module for TUGRAZ theme."""

from flask_babelex import gettext as _

# TODO: This is an example file. Remove it if your package does not use any
# extra configuration variables.

INVENIO_THEME_TUGRAZ_DEFAULT_VALUE = 'foobar'
"""Default value for the application."""

INVENIO_THEME_TUGRAZ_BASE_TEMPLATE = 'invenio_theme_tugraz/base.html'
"""Default base template for the demo page."""


# Theme Logo
THEME_LOGO = 'images/tug_logo.png'

# Instance's theme entrypoint file. Path relative to the ``assets/`` folder.
INSTANCE_THEME_FILE = './scss/invenio_tugraz_theme/theme.scss'

# Instance's search theme entrypoint file. Path under `assets` folder.
INSTANCE_SEARCH_THEME_FILE = './scss/invenio_tugraz_theme/search/theme.scss'

# Custom header.html
THEME_HEADER_TEMPLATE = 'invenio_theme_tugraz/header.html'

# override frontpage.html
THEME_FRONTPAGE_TEMPLATE = 'invenio_theme_tugraz/frontpage.html'

# Login page
SECURITY_LOGIN_USER_TEMPLATE = 'invenio_theme_tugraz/accounts/login.html'

# footer template
THEME_FOOTER_TEMPLATE = 'invenio_theme_tugraz/footer.html'

# uncomment this to use the login with Tugraz @ login.html
SHIBBOLETH_ISACTIVE = 'False'

# icon used in login page
TUG_ICON = 'images/icon_use.png'

# Frontpage title
THEME_FRONTPAGE_TITLE = "RDM for TUGRAZ"

# Mail server
MAIL_SERVER = '129.27.11.182'
SECURITY_EMAIL_SENDER = 'info@invenio-rdm.tugraz.at'
SECURITY_EMAIL_SUBJECT_REGISTER = 'Welcome to RDM!'
MAIL_SUPPRESS_SEND = False

# Invenio-I18N
# ============
# See https://invenio-i18n.readthedocs.io/en/latest/configuration.html
# Other supported languages (do not include BABEL_DEFAULT_LOCALE in list).
I18N_LANGUAGES = [
     ('de', _('German'))
 ]

