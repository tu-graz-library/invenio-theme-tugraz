# -*- coding: utf-8 -*-
#
# Copyright (C) 2020 TUGRAZ.
#
# invenio-theme-tugraz  is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

"""JS/CSS Webpack bundles for theme."""

from flask_webpackext import WebpackBundle


def theme():
    """Returns module's webpack bundle.

    This is a callable function in order to lazy load `current_app`
    and avoid working outside application context.
    """
    return WebpackBundle(
        __name__,
        'assets',
        entry={
            # TODO:
            #'invenio-theme-tugraz-js': './js/invenio_tugraz_theme/tugraz.js',
        },
        dependencies={
            'jquery': '3.1.0'
        }
    )
