# -*- coding: utf-8 -*-
#
# Copyright (C) 2019-2021 CERN.
# Copyright (C) 2019-2021 Northwestern University.
# Copyright (C)      2021 TU Wien.
# Copyright (C)      2021 Graz University of Technology.
#
# Invenio_theme_tugraz is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.
# https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/records_ui/views/deposits.py
"""Routes for record-related pages provided by Invenio-App-RDM."""


from flask import render_template
from flask_login import login_required
from invenio_app_rdm.records_ui.utils import set_default_value
from invenio_app_rdm.records_ui.views.decorators import pass_draft, pass_draft_files
from invenio_app_rdm.records_ui.views.deposits import (
    get_form_config,
    get_search_url,
    new_record,
)
from invenio_rdm_records.resources.serializers import UIJSONSerializer


@login_required
def deposit_create():
    """Create a new deposit."""
    return render_template(
        "invenio_theme_tugraz/deposit/deposit.html",
        forms_config=get_form_config(createUrl=("/api/records")),
        searchbar_config=dict(searchUrl=get_search_url()),
        record=new_record(),
        files=dict(
            default_preview=None, entries=[], links={}
        ),
    )


@login_required
@pass_draft
@pass_draft_files
def deposit_edit(draft=None, draft_files=None, pid_value=None):
    """Edit an existing deposit."""
    serializer = UIJSONSerializer()
    record = serializer.serialize_object_to_dict(draft.to_dict())

    return render_template(
        "invenio_theme_tugraz/deposit/deposit.html",
        forms_config=get_form_config(apiUrl=f"/api/records/{pid_value}/draft"),
        record=record,
        files=draft_files.to_dict(),
        searchbar_config=dict(searchUrl=get_search_url()),
        permissions=draft.has_permissions_to(['new_version'])
    )
