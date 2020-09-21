/*
 * Copyright (C) 2020 CERN.
 * Copyright (C) 2020 Northwestern University.
 * Copyright (C) 2020 Graz University of Technology
 *
 * invenio-theme-tugraz is free software; you can redistribute it
 * and/or modify it under the terms of the MIT License; see LICENSE
 * file for more details.
 *
 * origin: invenio_app_rdm/search/components.js
 */

import React from "react";
import { Card, Item, Input, Label, Button } from "semantic-ui-react";
import _ from "lodash";
import _truncate from "lodash/truncate";

export const RDMRecordResultsListItem = ({ result, index }) => {
  const description = _.get(
    result,
    "metadata.descriptions[0].description",
    "No description"
  );
  const version = _.get(
    result,
    "metadata.version",
    ""
  );
  const publicationDate = _.get(
    result,
    "metadata.publication_date",
    "No metadata"
  );
  const resourceType = _.get(
    result,
    "metadata.resource_type.type",
    "No resource type"
  );
  const access = _.get(
    result,
    "metadata.access_right",
    "No access rights"
  );
  const creatorName = _.get(
    result,
    "metadata.creators[0].name",
    "No creator"
  );
  const updatedDate = _.get(result, "updated");
  const title = _.get(
    result,
    "metadata.titles[0].title",
    "No title"
  );

  return (
    <Item key={index} href={`/records/${result.pid}`}>
      <Item.Content>
        <div className="badges">
          <Label size="tiny" color="blue">{publicationDate}</Label>
          <Label size="tiny" color="blue">{version}</Label>
          <Label size="tiny" color="grey">{resourceType}</Label>
          <Label size="tiny" color="green">{access}</Label>
        </div>
        <Item.Header>{title}</Item.Header>
        <Item.Meta>{creatorName}</Item.Meta>
        <Item.Description>
          {_truncate(description, { length: 350 })}
        </Item.Description>
        <Item.Extra>
          {updatedDate && <div>Updated on <span>{updatedDate}</span></div>}
        </Item.Extra>
      </Item.Content>
    </Item>
  );
};
