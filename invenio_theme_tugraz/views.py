# -*- coding: utf-8 -*-
#
# Copyright (C) 2020 mojib wali.
#
# invenio-theme-tugraz is free software; you can redistribute it and/or
# modify it under the terms of the MIT License; see LICENSE file for more
# details.

"""invenio module for TUGRAZ theme."""

import binascii
from typing import Dict

from elasticsearch_dsl.utils import AttrDict
from flask import Blueprint, current_app, render_template
from flask_login import login_required
from flask_menu import current_menu
from invenio_app_rdm.records_ui.views.deposits import (
    get_form_config,
    get_search_url,
    new_record,
)

from .crypto import Cryptor
from .search import FrontpageRecordsSearch


def ui_blueprint(app):
    """Blueprint for the routes and resources provided by Invenio-theme-tugraz."""
    routes = app.config.get("TUG_ROUTES")

    blueprint = Blueprint(
        "invenio_theme_tugraz",
        __name__,
        template_folder="templates",
        static_folder="static",
    )

    blueprint.add_url_rule(routes["index"], view_func=index)
    blueprint.add_url_rule(routes["comingsoon"], view_func=comingsoon)
    blueprint.add_url_rule(routes["deposit_create"], view_func=deposit_create)

    @blueprint.app_template_filter("make_dict_like")
    def make_dict_like(value: str, key: str) -> Dict[str, str]:
        """Convert the value to a dict like structure.

        in the form of a key -> value pair.
        """
        return {key: value}

    @blueprint.app_template_filter("cast_to_dict")
    def cast_to_dict(attr_dict):
        """Return the dict structure of AttrDict variable."""
        return AttrDict.to_dict(attr_dict)

    return blueprint


def index():
    """Frontpage."""
    return render_template(
        "invenio_theme_tugraz/index.html",
        records=FrontpageRecordsSearch()[:5].sort("-created").execute(),
    )


def comingsoon():
    """Frontpage."""
    return render_template("invenio_theme_tugraz/comingsoon.html")


def get_application_details():
    """Application credentials for DOI."""
    url = current_app.config.get("invenio_datacite_url") or ""
    username = current_app.config.get("INVENIO_DATACITE_UNAME") or ""
    password = current_app.config.get("INVENIO_DATACITE_PASS") or ""
    prefix = current_app.config.get("INVENIO_DATACITE_PREFIX") or ""

    password_iv, encrypted_password = Cryptor.encrypt(password, Cryptor.KEY)

    details = {
        "datacite_url": url,
        "datacite_uname": username,
        "datacite_pass": binascii.b2a_base64(encrypted_password).rstrip(),
        "datacite_prefix": prefix,
        "datacite_password_iv": password_iv,
    }
    return details


@login_required
def deposit_create():
    """Create a new deposit."""
    return render_template(
        "invenio_app_rdm/records/deposit.html",
        forms_config=get_form_config(createUrl=("/api/records")),
        datacite_config=get_application_details(),
        searchbar_config=dict(searchUrl=get_search_url()),
        record=new_record(),
        files=dict(default_preview=None, enabled=True, entries=[], links={}),
    )
