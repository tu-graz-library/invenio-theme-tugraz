# -*- coding: utf-8 -*-
#
# Copyright (C) 2020 mojib wali.
#
# invenio-theme-tugraz is free software; you can redistribute it and/or
# modify it under the terms of the MIT License; see LICENSE file for more
# details.

"""Pytest configuration.

See https://pytest-invenio.readthedocs.io/ for documentation on which test
fixtures are available.
"""

import shutil
import tempfile

import pytest
from flask import Flask
from flask_babelex import Babel
from invenio_i18n import InvenioI18N

from invenio_theme_tugraz import inveniothemetugraz
from invenio_theme_tugraz.views import blueprint


@pytest.fixture()
def app():
    """Flask app fixture."""
    app = Flask('myapp')
    app.config.update(
        I18N_LANGUAGES=[('en', 'English'), ('de', 'German')],
    )
    Babel(app)
    InvenioI18N(app)
    app.register_blueprint(create_blueprint_from_app(app))
    return app


@pytest.fixture(scope='module')
def celery_config():
    """Override pytest-invenio fixture.

    TODO: Remove this fixture if you add Celery support.
    """
    return {}


@pytest.fixture(scope='module')
def create_app(instance_path):
    """Application factory fixture."""
    def factory(**config):
        app = Flask('testapp', instance_path=instance_path)
        app.config.update(**config)
        Babel(app)
        inveniothemetugraz(app)
        app.register_blueprint(blueprint)
        return app
    return factory
