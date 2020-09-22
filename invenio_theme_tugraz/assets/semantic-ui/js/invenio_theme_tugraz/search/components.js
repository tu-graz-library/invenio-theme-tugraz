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
import { Card, Item, Input, Label, Button, Grid } from "semantic-ui-react";
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
  const creators = _.get(
    result,
    "metadata.creators",
    []
  );
  const uploadedDate = _.get(result, "metadata.publication_date");
  const title = _.get(
    result,
    "metadata.titles[0].title",
    "No title"
  );

  return (
    <Item key={index}>
      <Item.Content>
        <div className="badges">
          <Label className="teal">{publicationDate}</Label>
          <Label className="record-version">{version}</Label>
          <Label className="grey">{resourceType}</Label>
        </div>
        <Item.Header href={`/records/${result.pid}`}>{title}</Item.Header>
        <Creators creators={creators}/>
        <Item.Description href={`/records/${result.pid}`}>
          {_truncate(description, { length: 350 })}
        </Item.Description>
        <Grid columns={2}>
          <Grid.Row>
            <Grid.Column>
              {uploadedDate && <small>Uploaded on {uploadedDate}</small>}
            </Grid.Column>
            <Grid.Column>
              {access && <span className="access-right">{access}</span>}
            </Grid.Column>
          </Grid.Row>
        </Grid>
      </Item.Content>
    </Item>
  );
};

export const Creators = ({creators}) => {
  const creatorTags = creators.map((creator, index) => {
    return <Creator key={index} creator={creator}/>;
  });

  return (
    <div className="creators">
      {creatorTags}
    </div>
  );
};

export const Creator = ({creator}) => {
  return (
    <div className="creator">
      <a href="https://orcid.org/{creator.identifiers.Orcid}" target="_blank">
        <img className="inline-orcid" src="/static/extra/orcid.png"/>
      </a>
      <span className="text-muted">{creator.name}</span>
    </div>
  );
};
