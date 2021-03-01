# -*- coding: utf-8 -*-
#
# Copyright (C) 2020 mojib wali.
#
# invenio-theme-tugraz is free software; you can redistribute it and/or
# modify it under the terms of the MIT License; see LICENSE file for more
# details.

"""invenio module for TUGRAZ theme."""

from typing import Dict

from elasticsearch_dsl.utils import AttrDict
from flask import Blueprint, render_template
from flask_menu import current_menu

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
        records=FrontpageRecordsSearch()[:5].sort("-created").execute())


def comingsoon():
    """Frontpage."""
    return render_template("invenio_theme_tugraz/comingsoon.html")
