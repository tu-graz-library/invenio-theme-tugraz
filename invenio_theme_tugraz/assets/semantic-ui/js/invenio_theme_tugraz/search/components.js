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

import React, { useState } from "react";
import { Card, Item, Input, Label, Button, Grid, Checkbox, List, } from "semantic-ui-react";
import { BucketAggregation, Toggle } from "react-searchkit";
import _ from "lodash";
import _truncate from "lodash/truncate";
import Overridable from "react-overridable";
import { SearchBar } from "@js/invenio_search_ui/components";

export const RDMRecordResultsListItem = ({ result, index }) => {
  const description = _.get(result, "metadata.description", "No description");
  const version = _.get(result, "metadata.version", "");
  const creators = _.get(result, "metadata.creators", []);
  const title = _.get(result, "metadata.title", "No title");
  const subjects = _.get(result, "metadata.subjects", null);
  const rights = _.get(result, "metadata.rights", null)

  const publicationDate = _.get(result, "ui.publication_date_l10n_long", "No publication date found");
  const createdDate = _.get(result, "ui.created_date_l10n_long", "No creation date found.");
  const resourceType = _.get(result, "ui.resource_type", "No resource type");
  const access = _.get(result, "ui.access_right.title", "No access rights");
  const accessRightCategory = _.get(result, "ui.access_right.category", "closed");
  const accessRightIcon = _.get(result, "ui.access_right.icon", "closed");
  const accessRight = {type: access, category: accessRightCategory, icon: accessRightIcon, rights};

  const href = `/records/${result.id}`;

  return (
    <Item key={index}>
      <Item.Content>
        <div className="badges">
          <Label className="record-version">
            {publicationDate} {version ? `(${version})` : null}
          </Label>
          <Label className="teal">
            {resourceType}
          </Label>
        </div>
        <Item.Header href={href}>{title}</Item.Header>
        <Creators creators={creators}/>
        <Item.Description href={href}>
          {_truncate(description.replace(/(<([^>]+)>)/ig, ''), { length: 350 })}
        </Item.Description>
        <Footer subjects={subjects} createdDate={createdDate} accessRight={accessRight}/>
      </Item.Content>
    </Item>
  );
};

const Creators = ({creators}) => {
  const creatorTags = creators.map((creator, index) => {
    return <Creator key={index} creator={creator}/>;
  });

  return (
    <div className="creators">
      {creatorTags}
    </div>
  );
};

const Identifiers = ({creator}) => {
  return (
    <div className="identifiers">
      {_.isObject(creator.identifiers) && creator.identifiers.hasOwnProperty("orcid") &&
       <Orcid creator={creator}/>
      }
    </div>
  );
};

const Orcid = ({creator}) => {
  const href = `https://orcid.org/${creator.identifiers.orcid}`

  return (
    <a href={href} target="_blank">
      <img className="inline-orcid" src="/static/extra/orcid.png"/>
    </a>
  );
};

const Creator = ({creator}) => {
  return (
    <div className="creator">
      <Identifiers creator={creator}/>
      <span className="text-muted">{creator.person_or_org.name}</span>
    </div>
  );
};

const Footer = ({subjects, createdDate, accessRight}) => {
  return (
    <Item.Extra>
      <div className="left floated column">
        {subjects && subjects.map((subject, index) => (
          <Label key={index} size="tiny">
            {subject.subject}
          </Label>
        ))}
        {createdDate && (
          <div>
            <small>
              Uploaded on <span>{createdDate}</span>
            </small>
          </div>
        )}
      </div>
      <div className="right floated column">
        <span className={`ui access-right ${accessRight.category}`}>
          <i className={`icon ${accessRight.icon}`}></i>
          {accessRight.type} {accessRight.rights && accessRight.rights.map((right, index) => (
            <a key={index} href={right.uri}>({right.identifier})</a>
          ))}
        </span>
      </div>
    </Item.Extra>
  );
};

/**
 * ATTENTION:
 * The following classes are only here because it is not easily possible to
 * import it from the original module.
 * If there is in the future a possibility to import following classes from
 * invenio_app_rdm then this should be done!
 */
export const RDMRecordResultsGridItem = ({ result, index }) => {
  const description = _.get(result, "metadata.description", "No description");
  return (
    <Card fluid key={index} href={`/records/${result.pid}`}>
      <Card.Content>
        <Card.Header>{result.metadata.title}</Card.Header>
        <Card.Description>
          {_truncate(description, { length: 200 })}
        </Card.Description>
      </Card.Content>
    </Card>
  );
};

export const RDMRecordSearchBarContainer = () => {
  return (
    <Overridable id={"SearchApp.searchbar"}>
      <SearchBar />
    </Overridable>
  );
};

export const RDMRecordSearchBarElement = ({
  placeholder: passedPlaceholder,
  queryString,
  onInputChange,
  executeSearch,
}) => {
  const placeholder = passedPlaceholder || "Search";
  const onBtnSearchClick = () => {
    executeSearch();
  };
  const onKeyPress = (event) => {
    if (event.key === "Enter") {
      executeSearch();
    }
  };
  return (
    <Input
      action={{
        icon: "search",
        onClick: onBtnSearchClick,
        className: "search",
      }}
      placeholder={placeholder}
      onChange={(event, { value }) => {
        onInputChange(value);
      }}
      value={queryString}
      onKeyPress={onKeyPress}
    />
  );
};

export const RDMRecordFacetsValues = ({
  bucket,
  isSelected,
  onFilterClicked,
  getChildAggCmps,
}) => {
  const childAggCmps = getChildAggCmps(bucket);
  const [isActive, setisActive] = useState(false);
  const hasChildren = childAggCmps && childAggCmps.props.buckets.length > 0;
  return (
    <List.Item key={bucket.key}>
      <div
        className={`title ${hasChildren ? "" : "facet-subtitle"} ${
          isActive ? "active" : ""
        }`}
      >
        <List.Content floated="right">
          <Label circular>{bucket.doc_count}</Label>
        </List.Content>
        {hasChildren ? (
          <i
            className={`angle ${isActive ? "down" : "right"} icon`}
            onClick={() => setisActive(!isActive)}
          ></i>
        ) : null}
        <Checkbox
          label={bucket.label}
          value={bucket.key}
          onClick={() => onFilterClicked(bucket.key)}
          checked={isSelected}
        />
      </div>
      <div className={`content facet-content ${isActive ? "active" : ""}`}>
        {childAggCmps}
      </div>
    </List.Item>
  );
};

const SearchHelpLinks = () => {
  return (
    <Overridable id={"RdmSearch.SearchHelpLinks"}>
      <Grid className="padded-small">
        <Grid.Row className="no-padded">
          <Grid.Column>
            <Card className="borderless-facet">
              <Card.Content>
                <a>Advanced search</a>
              </Card.Content>
            </Card>
          </Grid.Column>
        </Grid.Row>
        <Grid.Row className="no-padded">
          <Grid.Column>
            <Card className="borderless-facet">
              <Card.Content>
                <a>Search guide</a>
              </Card.Content>
            </Card>
          </Grid.Column>
        </Grid.Row>
      </Grid>
    </Overridable>
  );
};

export const RDMRecordFacets = ({ aggs, currentResultsState }) => {
  return (
    <>
      <Toggle
        title="Versions"
        label="View all versions"
        filterValue={["all_versions", "true"]}
      />
      {aggs.map((agg) => {
        return (
          <div key={agg.title} className="ui accordion">
            <BucketAggregation title={agg.title} agg={agg} />
          </div>
        );
      })}
      <SearchHelpLinks />
    </>
  );
};

export const RDMBucketAggregationElement = ({ title, containerCmp }) => {
  return (
    <Card className="borderless-facet">
      <Card.Content>
        <Card.Header>{title}</Card.Header>
      </Card.Content>
      <Card.Content>{containerCmp}</Card.Content>
    </Card>
  );
};

export const RDMToggleComponent = ({
  updateQueryFilters,
  userSelectionFilters,
  filterValue,
  label,
  title,
  isChecked,
}) => {
  const _isChecked = (userSelectionFilters) => {
    const isFilterActive =
      userSelectionFilters.filter((filter) => filter[0] === filterValue[0])
        .length > 0;
    return isFilterActive;
  };

  const onToggleClicked = () => {
    updateQueryFilters(filterValue);
  };

  var isChecked = _isChecked(userSelectionFilters);
  return (
    <Card className="borderless-facet">
      <Card.Content>
        <Card.Header>{title}</Card.Header>
      </Card.Content>
      <Card.Content>
        <Checkbox
          toggle
          label={label}
          onClick={onToggleClicked}
          checked={isChecked}
        />
      </Card.Content>
    </Card>
  );
};
