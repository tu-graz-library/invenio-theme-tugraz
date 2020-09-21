/*
 * Copyright (C) 2020 Graz University of Technology
 *
 * invenio-theme-tugraz is free software; you can redistribute it and/or modify
 * it under the terms of the MIT License; see LICENSE file for more details.
 */


import { defaultComponents, createSearchAppInit } from "@js/invenio_search_ui";

import {
  RDMRecordResultsListItem,
  RDMRecordResultsGridItem,
  RDMRecordSearchBarElement,
} from "./components";

const initSearchApp = createSearchAppInit({
  "ResultsList.item": RDMRecordResultsListItem,
  "ResultsGrid.item": RDMRecordResultsGridItem,
  "SearchBar.element": RDMRecordSearchBarElement,
});
