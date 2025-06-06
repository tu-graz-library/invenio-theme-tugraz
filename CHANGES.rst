..
    Copyright (C) 2020-2021 Graz University of Technology.

    invenio-theme-tugraz is free software; you can redistribute it and/or
    modify it under the terms of the MIT License; see LICENSE file for more
    details.

Changes
=======

Version v4.13.3 (release 2025-05-27)

- fix: add logger output


Version v4.13.2 (release 2025-05-14)

- templates: guard against possibly nonexistent vars
- templates: reformat indentation of login_user.html
- ui: add edugain login-button to login-buttons


Version v4.13.1 (release 2025-05-01)

- setup: setuptools changed to underscore
- ui: add menu to user.email
- refactor: create blueprint to newer style
- setup: remove upper pins


Version v4.13.0 (release 2025-01-24)

- setup: necessary because devs not released
- view: add route for rdm-search
- setup: relax upper pins
- add default-page for unhandled errors
- guard views/dashboard by `tugraz_authenticated`
- fix deprecated `before_app_first_request`


Version v4.12.9 (release 2024-05-07)

- overview: view publications only if permission


Version v4.12.8 (release 2024-03-11)

- ui: add banner to header


Version v4.12.7 (release 2024-02-12)

- translation: fix typo


Version v4.12.6 (release 2024-02-02)

- fix: error_handler gets 1 parameter


Version v4.12.5 (release 2024-02-02)




Version v4.12.4 (release 2024-02-02)

- ui: add 423 error page
- fix: types could be empty list
- setup: sort tests imports
- workflows: change to reusable workflows
- wording: update one string frontpage
- wording: update frontpage


Version v4.12.3 (release 2024-01-28)

- wording: update text in benefits
- translation: fix research result typo
- ui: remove commented code
- ui: remove comingsoon rule


Version v4.12.2 (release 2024-01-07)

- ui: use only first type
- ui: change overview logos
- wording: improve
- wording: improve wording
- fix: multiple subjects not displayed in one row


Version v4.12.1 (release 2023-11-23)

- translation: change text on frontpage overview
- ui: comment browse functionality
- ui: remove scss, not used


Version v4.12.0 (release 2023-11-10)

- setup: move python supported window
- overview: rephrase text
- menu: temporarily remove overwrite
- ui: change paths to data-models
- global: change to invenio-records-global-search
- refactor: apply semantic-ui, indentation, copyright
- layout: improve
- theme: add separate search entry for rdm
- global: make it compatible with v12


Version v4.11.3 (release 2023-06-07)

- fix: frontpage upload buttons small monitor


Version v4.11.2 (release 2023-06-01)

- frontpage: layout changes
- translation: add oer frontpage translation
- WIP: oer upload button on frontpage


Version v4.11.1 (release 2023-04-20)

- fix: increase invenio-config-tugraz


Version v4.11.0 (release 2023-04-20)

- global: make dependencies compatible with v11


Version v4.10.1 (release 2022-11-10)

- dep: bump in invenio-assets


Version v4.10.0 (release 2022-10-13)

- global: migrate to v10 (#282)

Version v4.0.2 (release 2022-09-09)

- release v4.0.1
- update translation
- improve wording on search options


Version v4.0.1 (release 2022-08-05)

- update translation
- improve wording on search options


Version v4.0.0 (release 2022-07-29)

- remove unnecessary html code for header-search-bar
- fix warning from semantic-ui-react Search component
- add marc21 and lom to the searchbar
- change searchbar layout and use invenio-app-rdm searchbar
- remove grey color of community block and reduce size
- migrate js to use prettier

Version 3.9.2 (released 2022-06-28)

- fix: adopt renaming of serialize function (#269)

Version 3.9.1 (released 2022-06-02)

- fix: add trigger to accordion (#265)
- dep: adapt to v9 of invenioRDM(#263)

Version 3.9.0 (released 2022-05-27)

- global: migrate setup.py to setup.cfg #260 

Version 3.8.0 (released 2022-03-03)

- global: migrate to v8 of invenioRDM #257

Version 3.7.0 (released 2021-12-07)

- dep: bump config module #252
- docs: adjust sphinx to flask2 #251
- update register and login view #247

Version 3.6.1 (released 2021-09-01)

- fix: add font locally and remove google dependency #242
- fix: css for ui divider #243

Version 3.6.0 (released 2021-05-08)

- config: removes i18n config #239
- revert: removes override for details,deposit page #238
- styling: changes deposit form segment color #234
- refactor: views & deposit override #235
- login_user: extended user login template #230

Version 3.4.1 (released 2021-06-04)

- global: route blueprint migrated to config-tugraz #228

Version 3.4.0 (released 2021-06-01)

- documents: adds reference guide version 2 #225
- ui: change title to data-tooltip #224
- global: migrate inveniordm v4 #226

Version 3.0.3 (released 2021-06-01)

- bugfix: removes overrides item #222

Version 3.0.2 (released 2021-05-17)

- feature: adds credits to footer #217
- ui: adapt color badges #220
- badges(ui): adds tug theme badge colors #221

Version 3.0.1 (released 2021-05-07)

- override depsit & edit #210
- ui: display access badge #212
- documents: adds missing documents #216

Version 3.0.0 (released 2021-04-30)

- Migrated to invenioRDM v3 #209

Version 2.0.9 (released 2021-04-15)

- bugfix: created field using old metadata #196
- fix: blur link on click, clickable login with TUG button #194

Version 2.0.6 (released 2021-04-8)

- bugfixes: modified config vars #191

Version 1.9.0 (released 2021-03-11)

- DOI minting #161
- Zammad contact Form #156

Version 1.0.3 (released 2020-07-10)

- firefox compatibility: centering the menu underline #40
- adds font-family #50

Version 1.0.1 (released 2020-07-08)

- Login page modified #48

Version 0.1.0 (released TBD)

- Initial public release.
