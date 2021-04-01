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
from flask import Blueprint, current_app, g, render_template, request
from flask_login import login_required
from flask_menu import current_menu
from invenio_app_rdm.records_ui.views.decorators import (
    pass_draft,
    pass_record,
    pass_record_files,
    service,
)
from invenio_app_rdm.records_ui.views.deposits import (
    get_form_config,
    get_search_url,
    new_record,
)
from invenio_rdm_records.proxies import current_rdm_records
from invenio_rdm_records.resources.config import RDMDraftFilesResourceConfig
from invenio_rdm_records.resources.serializers import UIJSONSerializer
from invenio_rdm_records.services import RDMDraftFilesService

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
    blueprint.add_url_rule(routes["record_detail"], view_func=record_detail)
    blueprint.add_url_rule(routes["getdoi"], view_func=retrieve_doi, methods=["POST"])

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


def get_datacite_details():
    """Application credentials for DOI."""
    prefix = environ.get("INVENIO_DATACITE_PREFIX")
    suffix = environ.get("INVENIO_DATACITE_SUFFIX")
    host_url = environ.get("INVENIO_SITE_HOSTNAME")

    details = {
        "datacite_prefix": prefix,
        "datacite_suffix": suffix,
        "datacite_host_url": host_url,
    }
    return details


@login_required
def retrieve_doi():
    """Retrieve DOI from datacite API."""
    doi_metadata = request.get_json()

    url = environ.get("INVENIO_DATACITE_URL")
    username = environ.get("INVENIO_DATACITE_UNAME")
    password = environ.get("INVENIO_DATACITE_PASS")

    doi_response = requests.post(
        url,
        auth=(username, password.encode('utf-8')),
        json=doi_metadata,
    )

    response_data = {"code": doi_response.status_code}

    try:
        doi_response.raise_for_status()
        response_data["data"] = doi_response.json()
    except requests.exceptions.RequestException:
        response_data["errors"] = doi_response.json()["errors"]

    return response_data, response_data["code"]


#
# TODO: change this override behaviour once
# PR is merged:
# https://github.com/inveniosoftware/invenio-app-rdm/pull/638
#


@login_required
def deposit_create():
    """Create a new deposit."""
    forms_config = get_form_config(createUrl=("/api/records"))
    forms_config["data_cite"] = get_datacite_details()

    return render_template(
        "invenio_theme_tugraz/deposit/deposit.html",
        forms_config=forms_config,
        searchbar_config=dict(searchUrl=get_search_url()),
        record=new_record(),
        files=dict(default_preview=None, enabled=True, entries=[], links={}),
    )


@login_required
@pass_draft
def deposit_edit(draft=None, pid_value=None):
    """Edit an existing deposit."""
    files_list = current_rdm_records.draft_files_service.list_files(
        id_=pid_value,
        identity=g.identity,
        links_config=RDMDraftFilesResourceConfig.links_config,
    )

    serializer = UIJSONSerializer()
    record = serializer.serialize_object_to_dict(draft.to_dict())

    forms_config = get_form_config(apiUrl=f"/api/records/{pid_value}/draft")
    forms_config["data_cite"] = get_datacite_details()

    return render_template(
        "invenio_theme_tugraz/deposit/deposit.html",
        forms_config=forms_config,
        record=record,
        files=files_list.to_dict(),
        searchbar_config=dict(searchUrl=get_search_url()),
        permissions=draft.has_permissions_to(['new_version'])
    )


@pass_record
@pass_record_files
def record_detail(record=None, files=None, pid_value=None):
    """Record detail page (aka landing page)."""
    files_dict = None if files is None else files.to_dict()
    return render_template(
        "invenio_theme_tugraz/landingpage/detail.html",
        record=UIJSONSerializer().serialize_object_to_dict(record.to_dict()),
        pid=pid_value,
        files=files_dict,
        permissions=record.has_permissions_to(['edit', 'new_version']),
    )
