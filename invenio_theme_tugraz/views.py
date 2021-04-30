# -*- coding: utf-8 -*-
#
# Copyright (C) 2020-2021 Graz University of Technology.
#
# invenio-theme-tugraz is free software; you can redistribute it and/or
# modify it under the terms of the MIT License; see LICENSE file for more
# details.

"""invenio module for TUGRAZ theme."""

import binascii
from os import environ
from typing import Dict

import requests
from elasticsearch_dsl.utils import AttrDict
from flask import Blueprint, current_app, g, redirect, render_template, request, url_for
from flask_babelex import get_locale
from flask_login import login_required
from flask_menu import current_menu
from invenio_app_rdm.records_ui.views.decorators import (
    pass_is_preview,
    pass_record_files,
    pass_record_or_draft,
)
from invenio_rdm_records.resources.serializers import UIJSONSerializer

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
    blueprint.add_url_rule(routes["guide"], view_func=guide)
    blueprint.add_url_rule(routes["terms"], view_func=terms)
    blueprint.add_url_rule(routes["gdpr"], view_func=gdpr)
    blueprint.add_url_rule(routes["record_detail"], view_func=record_detail)

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
    """Comingsoon."""
    return render_template("invenio_theme_tugraz/comingsoon.html")


def guide():
    """TUGraz_Repository_Guide."""
    locale = get_locale()
    return redirect(url_for('static',
                            filename=f'documents/TUGraz_Repository_Guide_01_{locale}.pdf',
                            _external=True))


def terms():
    """Terms_And_Conditions."""
    locale = get_locale()
    return redirect(url_for('static',
                            filename=f'documents/TUGraz_Repository_Terms_And_Conditions_{locale}.pdf',
                            _external=True))


def gdpr():
    """General_Data_Protection_Rights."""
    locale = get_locale()
    return redirect(url_for('static',
                            filename=f'documents/TUGraz_Repository_General_Data_Protection_Rights_{locale}.pdf',
                            _external=True))


@pass_is_preview
@pass_record_or_draft
@pass_record_files
def record_detail(record=None, files=None, pid_value=None, is_preview=False):
    """Record detail page (aka landing page)."""
    files_dict = None if files is None else files.to_dict()

    return render_template(
        "invenio_theme_tugraz/landingpage/detail.html",
        record=UIJSONSerializer().serialize_object_to_dict(record.to_dict()),
        pid=pid_value,
        files=files_dict,
        permissions=record.has_permissions_to(['edit', 'new_version', 'manage',
                                               'update_draft', 'read_files']),
        is_preview=is_preview,
    )
