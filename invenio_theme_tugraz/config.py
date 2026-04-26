# -*- coding: utf-8 -*-
#
# Copyright (C) 2020-2026 Graz University of Technology.
#
# invenio-theme-tugraz is free software; you can redistribute it and/or
# modify it under the terms of the MIT License; see LICENSE file for more
# details.

"""invenio module for TUGRAZ theme."""

from invenio_i18n import gettext as _

DEPOSITS_HEADER_TEMPLATE = "invenio_override/header.html"

OVERRIDE_ACCOUNT_BASE = "invenio_override/accounts/accounts_base.html"
OVERRIDE_CONTACT_FORM = False
OVERRIDE_FAVICON = "tug.ico"
OVERRIDE_FRONTPAGE_RIGHT = False
OVERRIDE_FRONTPAGE_SHOW_RECENT_UPLOADS = True
OVERRIDE_HEADER_CLAIM_WORDS = ["SCIENCE", "PASSION", "TECHNOLOGY"]
OVERRIDE_HEADER_LOGO_LEFT = "images/library_logo.png"
OVERRIDE_HEADER_LOGO_LINK = "https://www.tugraz.at"
OVERRIDE_HEADER_LOGO_SVG = "images/tu_graz_logo.svg"
OVERRIDE_HEADER_TEXT_LINE1 = "TU GRAZ"
OVERRIDE_HEADER_TEXT_LINE2 = "REPOSITORY"
OVERRIDE_HEADER_TEXT_LINE3 = "LIBRARY & ARCHIVES"
OVERRIDE_ICON = "images/icon_use.png"
OVERRIDE_FRONTPAGE_FEATURES = [
    {"icon": "check circle", "text": "FAIR Data"},
    {"icon": "quote left", "text": "Citable with DOI"},
    {"icon": "lock open", "text": "Open Access"},
    {"icon": "shield alternate", "text": "Long-term Preservation"},
]
OVERRIDE_FRONTPAGE_SUBTITLE = _(
    "Publish and share your research data — citable, visible, and FAIR."
)
OVERRIDE_FOOTER_BACKGROUND = "#4a4a4a"
OVERRIDE_FOOTER_DIVIDER_COLOR = "rgba(255,255,255,0.1)"
OVERRIDE_FOOTER_FG_COLOR = "#ffffff"


OVERRIDE_FOOTER_LINKS = {
    "Repository": [
        {
            "label": "Documentation",
            "url": "https://tu-graz-library.github.io/docs-repository",
            "external": True,
        },
        {"label": "Reference Guide", "url": "/guide", "external": True},
        {"label": "Search Guide", "url": "/help/search"},
        {"label": "Data Protection", "url": "/gdpr", "external": True},
        {"label": "Terms and Conditions", "url": "/terms", "external": True},
        {"label": "Accessibility Statement", "url": "/accessibility", "external": True},
        {
            "label": "List of preferred file formats",
            "url": "/file-formats",
            "external": True,
        },
        {"label": "Curation Workflow", "url": "/curations", "external": True},
    ],
    "Features": [
        {"label": "Scalability"},
        {"label": "Institutional integration"},
        {"label": "Next Generation Repository"},
        {"label": "Repository Profiles"},
        {"label": "Resilient"},
    ],
    "Connected Services": [
        {"label": "PURE", "url": "https://pure.tugraz.at", "external": True},
        {
            "label": "CampusOnline",
            "url": "http://campusonline.tugraz.at",
            "external": True,
        },
        {
            "label": "Research Data Management",
            "url": "https://rdm.tugraz.at",
            "external": True,
        },
    ],
    "Accessibility": [
        {"label": "Tip:"},
        {"label": "Use Ctrl + and Ctrl - to change the font size."},
    ],
}
OVERRIDE_FOOTER_LOGO_FILTER = "brightness(0) invert(1)"
OVERRIDE_LOGO = "images/TUG.png"
OVERRIDE_PRODUCTION = True
OVERRIDE_REASONS_BG = None  # use CSS radial-gradient from frontpage.less
OVERRIDE_REASONS_PARTNER = "TU Graz & CERN"
OVERRIDE_RESOURCE_OVERVIEW = False
OVERRIDE_SHIBBOLETH = False

OVERRIDE_SHOW_CONTACT = True
OVERRIDE_SHOW_EDUCATIONAL_RESOURCES = True
OVERRIDE_SHOW_EDUCATIONAL_RESOURCES_CARD = True
OVERRIDE_SHOW_PUBLICATIONS_CARD = True
OVERRIDE_SHOW_PUBLICATIONS_SEARCH = True
OVERRIDE_SHOW_RIGHT_CONTACT_EMAIL = True
OVERRIDE_SHOW_RDM_SEARCH = True

SEARCH_UI_HEADER_TEMPLATE = "invenio_override/header.html"

SECURITY_LOGIN_USER_TEMPLATE = "invenio_override/accounts/login_user.html"
SECURITY_REGISTER_USER_TEMPLATE = "invenio_override/accounts/register_user.html"

THEME_500_TEMPLATE = "invenio_theme_tugraz/default_error.html"
THEME_FOOTER_TEMPLATE = "invenio_override/footer.html"
THEME_FRONTPAGE = False
THEME_FRONTPAGE_TITLE = _("TU Graz Repository")
THEME_HEADER_LOGIN_TEMPLATE = "invenio_override/accounts/header_login.html"
THEME_HEADER_TEMPLATE = "invenio_override/header.html"
THEME_LOGO = "images/tug_logo.png"
THEME_SEARCHBAR = False
THEME_SITENAME = _("Repository")
THEME_SHOW_FRONTPAGE_INTRO_SECTION = True
