# # -*- coding: utf-8 -*-
# #
# # Copyright (C) 2020 mojib wali.
# #
# # invenio-theme-tugraz is free software; you can redistribute it and/or
# # modify it under the terms of the MIT License; see LICENSE file for more
# # details.

# """Test views."""

# from elasticsearch_dsl.utils import AttrDict

# from invenio_theme_tugraz.views import cast_to_dict, make_dict_like


# def test_make_dict_like():
#     """Test make_dict_like."""
#     access = {
#         "access_right" : "open"
#     }
#     dicts = make_dict_like("open", "access_right")
#     assert access == dicts


# def test_cast_to_dict():
#     """Test cast_to_dict."""
#     resource_type = {
#         "subtype" : "publication-datamanagementplan",
#         "type" : "publication"
#     }
#     expected = {'subtype': 'publication-datamanagementplan', 'type': 'publication'}
#     attr = cast_to_dict(AttrDict(resource_type))
#     assert expected == attr
