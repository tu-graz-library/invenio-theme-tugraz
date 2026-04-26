# -*- coding: utf-8 -*-
#
# Copyright (C) 2020 TUGRAZ.
# Copyright (C) 2026 Graz University of Technology.
#
# invenio-theme-tugraz  is free software.

"""JS/CSS Webpack bundles for theme."""

from invenio_assets.webpack import WebpackThemeBundle

theme = WebpackThemeBundle(
    __name__,
    "assets",
    default="semantic-ui",
    themes={
        "semantic-ui": dict(
            entry={
                "invenio-theme-tugraz-js": "./js/invenio_theme_tugraz/theme.js",
                "invenio-theme-tugraz-unlock": "./js/invenio_theme_tugraz/unlock.js",
            },
            dependencies={
                "jquery": "^3.2.1",  # zammad-form, semantic-ui's modals
            },
        )
    },
)
