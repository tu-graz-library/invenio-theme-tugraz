# -*- coding: utf-8 -*-
#
# Copyright (C) 2020 mojib wali.
#
# invenio-theme-tugraz is free software; you can redistribute it and/or
# modify it under the terms of the MIT License; see LICENSE file for more
# details.

"""invenio module for TUGRAZ theme."""

import os

from setuptools import find_packages, setup

readme = open("README.rst").read()
history = open("CHANGES.rst").read()

invenio_version = '~=3.4.0'
invenio_search_version = '>=1.4.0,<1.5.0'
invenio_db_version = '>=1.0.5,<1.1.0'

tests_require = [
    "pytest-invenio~=1.4.1",
    "sqlalchemy-continuum>=1.3.11",
    "invenio_search>=1.3.1",
    "psycopg2-binary>=2.8.6",
]

extras_require = {
    # Invenio-Search
    'elasticsearch6': [
        f'invenio-search[elasticsearch6]{invenio_search_version}'
    ],
    'elasticsearch7': [
        f'invenio-search[elasticsearch7]{invenio_search_version}'
    ],
    # Invenio-DB
    'mysql': [
        f'invenio-db[mysql,versioning]{invenio_db_version}'
    ],
    'postgresql': [
        f'invenio-db[postgresql,versioning]{invenio_db_version}'
    ],
    'sqlite': [
        f'invenio-db[versioning]{invenio_db_version}'
    ],
    # Extras
    'docs': [
        'Sphinx>=3,<3.4.2',
    ],
    'tests': tests_require,
}


extras_require['all'] = []
for name, reqs in extras_require.items():
    if name[0] == ':' or name in ('elasticsearch6', 'elasticsearch7',
                                  'mysql', 'postgresql', 'sqlite'):
        continue
    extras_require['all'].extend(reqs)


setup_requires = [
    'Babel>=2.8',
]

install_requires = [
    "invenio-assets>=1.2.0",
    "invenio-i18n>=1.2.0",
    "elasticsearch_dsl>=7.2.1",
    "invenio_app_rdm>=0.18.8",

]

packages = find_packages()


# Get the version string. Cannot be done with import!
g = {}
with open(os.path.join("invenio_theme_tugraz", "version.py"), "rt") as fp:
    exec(fp.read(), g)
    version = g["__version__"]

setup(
    name="invenio-theme-tugraz",
    version=version,
    description=__doc__,
    long_description=readme + "\n\n" + history,
    keywords="invenio, theme, invenioRDM, TU-Graz, Graz University of Technology, statistics",
    license="MIT",
    author="mojib wali",
    author_email="mojib.wali@tugraz.at",
    url="https://github.com/tu-graz-library/invenio-theme-tugraz",
    packages=packages,
    zip_safe=False,
    include_package_data=True,
    platforms="any",
    entry_points={
        "invenio_base.apps": [
            "invenio_theme_tugraz = invenio_theme_tugraz:InvenioThemeTugraz",
        ],
        "invenio_base.blueprints": [
            "invenio_theme_tugraz = invenio_theme_tugraz.views:blueprint",
        ],
        "invenio_i18n.translations": [
            "messages = invenio_theme_tugraz",
        ],
        "invenio_assets.webpack": [
            "invenio_theme_tugraz_theme = invenio_theme_tugraz.webpack:theme",
        ],
        "invenio_config.module": [
            "invenio_theme_tugraz = invenio_theme_tugraz.config",
        ],
    },
    extras_require=extras_require,
    install_requires=install_requires,
    setup_requires=setup_requires,
    tests_require=tests_require,
    classifiers=[
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Development Status :: 3 - Alpha",
    ],
)
