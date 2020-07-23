# -*- coding: utf-8 -*-
#
# Copyright (C) 2020 mojib wali.
#
# invenio-theme-tugraz is free software; you can redistribute it and/or
# modify it under the terms of the MIT License; see LICENSE file for more
# details.

"""Module tests."""

from flask import Flask

from invenio_theme_tugraz import inveniothemetugraz


def test_version():
    """Test version import."""
    from invenio_theme_tugraz import __version__
    assert __version__


def test_init():
    """Test extension initialization."""
    app = Flask('testapp')
    ext = inveniothemetugraz(app)
    assert 'invenio-theme-tugraz' in app.extensions

    app = Flask('testapp')
    ext = inveniothemetugraz()
    assert 'invenio-theme-tugraz' not in app.extensions
    ext.init_app(app)
    assert 'invenio-theme-tugraz' in app.extensions
