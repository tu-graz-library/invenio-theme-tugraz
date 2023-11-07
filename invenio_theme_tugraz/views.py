# -*- coding: utf-8 -*-
#
# Copyright (C) 2020-2021 Graz University of Technology.
#
# invenio-theme-tugraz is free software; you can redistribute it and/or
# modify it under the terms of the MIT License; see LICENSE file for more
# details.

"""invenio module for TUGRAZ theme."""

from typing import Dict

from flask import Blueprint, g, render_template
from flask_login import current_user, login_required
from flask_menu import current_menu
from invenio_i18n import lazy_gettext as _

# from invenio_rdm_records.resources.serializers import UIJSONSerializer
from invenio_records_global_search.resources.serializers import (
    GlobalSearchJSONSerializer,
)
from invenio_users_resources.proxies import current_user_resources
from opensearch_dsl.utils import AttrDict

from .search import FrontpageRecordsSearch

blueprint = Blueprint(
    "invenio_theme_tugraz",
    __name__,
    template_folder="templates",
    static_folder="static",
)


@blueprint.route("/me/overview")
@login_required
def overview():
    """Overview."""
    url = current_user_resources.users_service.links_item_tpl.expand(
        g.identity, current_user
    )["avatar"]
    return render_template(
        "invenio_theme_tugraz/overview.html",
        user_avatar=url,
    )


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


@blueprint.before_app_first_request
def modify_user_dashboard():
    """Modify user dashboard."""
    user_dashboard_menu = current_menu.submenu("dashboard")

    # order matters, this has to be here, otherwise it want override the orginal
    # entry

    # this is to buggy, it depends on the load order of the packages which is indeterminate
    # user_dashboard_menu.submenu("uploads").register(
    #     "invenio_app_rdm_users.uploads",
    #     text=_("Research Results"),
    #     order=1,
    # )

    user_dashboard_menu.submenu("overview").register(
        "invenio_theme_tugraz.overview",
        text=_("Overview"),
        order=0,
    )

    current_menu.submenu("actions.deposit").register(
        "invenio_theme_tugraz.overview",
        _("My dashboard"),
        order=1,
    )


def ui_blueprint(app):
    """Blueprint for the routes and resources provided by Invenio-theme-tugraz."""
    routes = app.config.get("TUG_ROUTES")

    blueprint.add_url_rule(routes["index"], view_func=index)
    blueprint.add_url_rule(routes["comingsoon"], view_func=comingsoon)

    return blueprint


def records_serializer(records=None):
    """Serialize list of records."""
    serializer = GlobalSearchJSONSerializer()
    return [serializer.dump_obj(r.to_dict()) for r in records]


def index():
    """Frontpage."""
    records = FrontpageRecordsSearch()[:5].sort("-created").execute()

    return render_template(
        "invenio_theme_tugraz/index.html", records=records_serializer(records)
    )


def comingsoon():
    """Comingsoon."""
    return render_template("invenio_theme_tugraz/comingsoon.html")
