# -*- coding: utf-8 -*-
#
# Copyright (C) 2020 TUGRAZ.
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
                "invenio-theme-tugraz-search-app": "./js/invenio_theme_tugraz/search/index.js",
                # overrides RDM deposit form
                'invenio-theme-tugraz-rdm-deposit': './js/invenio_theme_tugraz/deposit/index.js',
            },
            dependencies={

                # required for RDM deposit form
                # keep in sync
                "@babel/runtime": "^7.9.0",
                'formik': '^2.1.4',
                'luxon': '^1.23.0',
                'path': '^0.12.7',
                'prop-types': '^15.7.2',
                'react-dnd': '^11.1.3',
                'react-dnd-html5-backend': '^11.1.3',
                'react-invenio-deposit': '^0.11.10',
                'react-invenio-forms': '^0.6.3',
                'react-dropzone': "^11.0.3",
                'yup': '^0.27.0',
                '@ckeditor/ckeditor5-build-classic': '^16.0.0',
                '@ckeditor/ckeditor5-react': '^2.1.0',

                # datacite - rest api plugin
                'datacite-rest': '^0.1.7',

            },
        )
    },
)
