# -*- coding: utf-8 -*-
#
# Copyright (C) 2022 TUGRAZ.
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
                "invenio-theme-tugraz-theme": "./less/invenio_theme_tugraz/theme.less",
                "invenio-theme-tugraz-js": "./js/invenio_theme_tugraz/theme.js",
                "invenio-theme-tugraz-rdm-deposit": "./js/invenio_theme_tugraz/deposit/index.js",
            },
            dependencies={
                # add any additional npm dependencies here...
            },
        )
    },
)
