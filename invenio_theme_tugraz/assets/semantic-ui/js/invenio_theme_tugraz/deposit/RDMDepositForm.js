// This file is part of InvenioRDM
// Copyright (C) 2020 CERN.
// Copyright (C) 2020 Northwestern University.
// Copyright (C) 2021 Graz University of Technology.
//
// Invenio App RDM is free software; you can redistribute it and/or modify it
// under the terms of the MIT License; see LICENSE file for more details.

import _get from "lodash/get";
import React, { Component, createRef } from "react";
import {
  Button,
  Card,
  Container,
  Grid,
  Icon,
  Ref,
  Sticky,
} from "semantic-ui-react";
import {
  AccessRightField,
  ComingSoonField,
  CreatibutorsField,
  DatesField,
  DepositFormApp,
  FormFeedback,
  DeleteButton,
  DepositFormTitle,
  DescriptionsField,
  FileUploader,
  FundingField,
  IdentifiersField,
  LanguagesField,
  PublishButton,
  PublicationDateField,
  ResourceTypeField,
  SaveButton,
  SubjectsField,
  TitlesField,
  RelatedWorksField,
  VersionField,
  LicenseField,
} from "react-invenio-deposit";
import { AccordionField } from "react-invenio-forms";
import { DoiMint } from "./DoiMint";
import { PublisherField } from "./PublisherField";

export class RDMDepositForm extends Component {
  constructor(props) {
    super(props);
    this.config = props.config || {};
    // TODO: retrieve from backend
    this.config["canHaveMetadataOnlyRecords"] = true;

    // TODO: Make ALL vocabulary be generated by backend.
    // Currently, some vocabulary is generated by backend and some is
    // generated by frontend here. Iteration is faster and abstractions can be
    // discovered by generating vocabulary here. Once happy with vocabularies,
    // then we can generate it in the backend.
    this.vocabularies = {
      metadata: {
        ...this.config.vocabularies,

        titles: {
          ...this.config.vocabularies.titles,
        },

        descriptions: {
          type: [
            { text: "Abstract", value: "abstract" },
            { text: "Methods", value: "methods" },
            { text: "Series Information", value: "seriesinformation" },
            { text: "Table of Contents", value: "tableofcontents" },
            { text: "Technical Info", value: "technicalinfo" },
            { text: "Other", value: "other" },
          ],
        },

        creators: {
          type: [
            { text: "Person", value: "personal" },
            { text: "Organization", value: "organizational" },
          ],
          role: [
            { text: "Editor", value: "editor" },
            { text: "Data Curator", value: "datacurator" },
            { text: "Data Manager", value: "datamanager" },
            { text: "Project Manager", value: "projectmanager" },
          ],
        },

        contributors: {
          type: [
            { text: "Person", value: "personal" },
            { text: "Organization", value: "organizational" },
          ],
          role: [
            { text: "Editor", value: "editor" },
            { text: "Data Curator", value: "datacurator" },
            { text: "Data Manager", value: "datamanager" },
            { text: "Project Manager", value: "projectmanager" },
          ],
        },

        dates: {
          type: [
            { text: "Accepted", value: "accepted" },
            { text: "Available", value: "available" },
            { text: "Copyrighted", value: "copyrighted" },
            { text: "Collected", value: "collected" },
            { text: "Created", value: "created" },
            { text: "Issued", value: "issued" },
            { text: "Submitted", value: "submitted" },
            { text: "Updated", value: "updated" },
            { text: "Valid", value: "valid" },
            { text: "Withdrawn", value: "withdrawn" },
            { text: "Other", value: "other" },
          ],
        },

        // TODO: Replace with an API backend
        funding: {
          funder: [
            {
              name: "National Institutes of Health (US)",
              identifier: "funder1",
              scheme: "funderScheme1",
            },
            {
              name: "European Commission (EU)",
              identifier: "funder2",
              scheme: "funderScheme2",
            },
          ],
          award: [
            {
              title: "CANCER &AIDS DRUGS--PRECLIN PHARMACOL/TOXICOLOGY",
              number: "N01CM037835-016",
              identifier: "awardA",
              scheme: "awardSchemeA",
              parentScheme: "funderScheme1",
              parentIdentifier: "funder1",
            },
            {
              title:
                "Beyond the Standard Model at the LHC and with Atom Interferometers.",
              number: "228169",
              identifier: "awardB1",
              scheme: "awardSchemeB",
              parentScheme: "funderScheme2",
              parentIdentifier: "funder2",
            },
            {
              title: "ENvironmental COnditions in GLAucoma Patients",
              number: "747441",
              identifier: "awardB2",
              scheme: "awardSchemeB",
              parentScheme: "funderScheme2",
              parentIdentifier: "funder2",
            },
          ],
        },

        related_identifiers: {
          resource_type: this.config.vocabularies.resource_type,
          scheme: [
            { text: "ARK", value: "ark" },
            { text: "ARXIV", value: "arxiv" },
            { text: "BIBCODE", value: "bibcode" },
            { text: "DOI", value: "doi" },
            { text: "EAN13", value: "ean13" },
            { text: "EISSN", value: "eissn" },
            { text: "HANDLE", value: "handle" },
            { text: "IGSN", value: "igsn" },
            { text: "ISBN", value: "isbn" },
            { text: "ISSN", value: "issn" },
            { text: "ISTC", value: "istc" },
            { text: "LISSN", value: "lissn" },
            { text: "LSID", value: "lsid" },
            { text: "PMID", value: "pmid" },
            { text: "PURL", value: "purl" },
            { text: "UPC", value: "upc" },
            { text: "URL", value: "url" },
            { text: "URN", value: "urn" },
            { text: "W3ID", value: "w3id" },
          ],
          relations: [
            { text: "Is cited by", value: "iscitedby" },
            { text: "Cites", value: "cites" },
            { text: "Is supplement to", value: "issupplementto" },
            { text: "Is supplemented by", value: "issupplementedby" },
            { text: "Is continued by", value: "iscontinuedby" },
            { text: "Continues", value: "continues" },
            { text: "Is described by", value: "isdescribedby" },
            { text: "Describes", value: "describes" },
            { text: "Has metadata", value: "hasmetadata" },
            { text: "Is metadata for", value: "ismetadatafor" },
            { text: "Has version", value: "hasversion" },
            { text: "Is version of", value: "isversionof" },
            { text: "Is new version of", value: "isnewversionof" },
            { text: "Is previous version of", value: "ispreviousversionof" },
            { text: "Is part of", value: "ispartof" },
            { text: "Has part", value: "haspart" },
            { text: "Is referenced by", value: "isreferencedby" },
            { text: "References", value: "references" },
            { text: "Is documented by", value: "isdocumentedby" },
            { text: "Documents", value: "documents" },
            { text: "Is compiled by", value: "iscompiledby" },
            { text: "Compiles", value: "compiles" },
            { text: "Is variant form of", value: "isvariantformof" },
            { text: "Is original form of", value: "isoriginalformof" },
            { text: "Is identical to", value: "isidenticalto" },
            { text: "Is reviewed by", value: "isreviewedby" },
            { text: "Reviews", value: "reviews" },
            { text: "Is derived from", value: "isderivedfrom" },
            { text: "Is source of", value: "issourceof" },
            { text: "Is required by", value: "isrequiredby" },
            { text: "Requires", value: "requires" },
            { text: "Is obsoleted by", value: "isobsoletedby" },
            { text: "Obsoletes", value: "obsoletes" },
          ],
        },
        subjects: {
          options: [
            {
              text: "Deep Learning",
              value: {
                subject: "Deep Learning",
                scheme: "user",
                identifier: "U1",
              },
            },
            {
              text: "MeSH: Cognitive Neuroscience",
              value: {
                subject: "Cognitive Neuroscience",
                scheme: "mesh",
                identifier: "D000066494",
              },
            },
            {
              text: "FAST: Glucagonoma",
              value: {
                subject: "Glucagonoma",
                scheme: "fast",
                identifier: "943672",
              },
            },
          ],
          limitToOptions: [
            { text: "All", value: "all" },
            { text: "MeSH", value: "mesh" },
            { text: "FAST", value: "fast" },
          ],
        },
      },
    };

    // check if files are present
    this.noFiles = false;
    if (
      !Array.isArray(this.props.files.entries) ||
      (!this.props.files.entries.length && this.props.record.is_published)
    ) {
      this.noFiles = true;
    }
  }

  formFeedbackRef = createRef();
  sidebarRef = createRef();

  accordionStyle = {
    header: { className: "inverted brand", style: { cursor: "pointer" } },
  };

  render() {
    return (
      <DepositFormApp
        config={this.config}
        record={this.props.record}
        files={this.props.files}
        permissions={this.props.permissions}
      >
        <FormFeedback fieldPath="message" />
        <Container style={{ marginTop: "10px" }}>
          <DepositFormTitle />
          <Grid>
            <Grid.Row>
              <Grid.Column width={11}>
                <AccordionField
                  fieldPath=""
                  active={true}
                  label={"Files"}
                  ui={this.accordionStyle}
                >
                  {this.noFiles && this.props.record.is_published && (
                    <p
                      style={{
                        textAlign: "center",
                        opacity: "0.5",
                        cursor: "default !important",
                      }}
                    >
                      <em>The record has no files.</em>
                    </p>
                  )}
                  <FileUploader
                    isDraftRecord={!this.props.record.is_published}
                    quota={{
                      maxFiles: 100,
                      maxStorage: 10 ** 10,
                    }}
                  />
                </AccordionField>
                {/**TODO: uncomment to use IdentifiersField*/}
                {/* <AccordionField
                fieldPath=""
                active={true}
                label={"Files"}
                ui={this.accordionStyle}
              >
                <IdentifiersField />
                <ComingSoonField
                  fieldPath="metadata.identifiers"
                  label="Identifier(s)"
                  labelIcon="barcode"
                />
                <br />
              </AccordionField> */}

                <AccordionField
                  fieldPath=""
                  active={true}
                  label={"Basic Information"}
                  ui={this.accordionStyle}
                >
                  <ResourceTypeField
                    options={this.vocabularies.metadata.resource_type}
                    required
                  />
                  <TitlesField
                    options={this.vocabularies.metadata.titles}
                    required
                  />
                  <PublicationDateField required />
                  <CreatibutorsField
                    label={"Creators"}
                    labelIcon={"user"}
                    fieldPath={"metadata.creators"}
                    roleOptions={this.vocabularies.metadata.creators.role}
                    schema="creators"
                    required
                  />
                  <DescriptionsField
                    options={this.vocabularies.metadata.descriptions}
                    editorConfig={{
                      removePlugins: [
                        "Image",
                        "ImageCaption",
                        "ImageStyle",
                        "ImageToolbar",
                        "ImageUpload",
                        "MediaEmbed",
                        "Table",
                        "TableToolbar",
                        "TableProperties",
                        "TableCellProperties",
                      ],
                    }}
                  />
                  <LicenseField
                    fieldPath="metadata.rights"
                    searchConfig={{
                      searchApi: {
                        axios: {
                          headers: {
                            Accept: "application/vnd.inveniordm.v1+json",
                          },
                          url: "/api/vocabularies/licenses",
                          withCredentials: false,
                        },
                      },
                      initialQueryState: {
                        filters: [["tags", "recommended"]],
                      },
                    }}
                    serializeLicenses={(result) => ({
                      title: result.title_l10n,
                      description: result.description_l10n,
                      id: result.id,
                      link: result.props.url,
                    })}
                  />
                  <br />
                </AccordionField>

                <AccordionField
                  fieldPath=""
                  active={true}
                  label={"Recommended Information"}
                  ui={this.accordionStyle}
                >
                  <CreatibutorsField
                    addButtonLabel={"Add contributor"}
                    label={"Contributors"}
                    labelIcon={"user plus"}
                    fieldPath={"metadata.contributors"}
                    roleOptions={this.vocabularies.metadata.contributors.role}
                    schema="contributors"
                    modal={{
                      addLabel: "Add contributor",
                      editLabel: "Edit contributor",
                    }}
                  />
                  {/**TODO: uncomment to use Subjects*/}
                  {/* <SubjectsField
                  initialOptions={_get(
                    this.props.record,
                    "metadata.subjects",
                    null
                  )}
                  limitToOptions={
                    this.vocabularies.metadata.subjects.limitToOptions
                  }
                />
                <ComingSoonField
                  fieldPath="metadata.subjects"
                  label="Subjects"
                  labelIcon="tag"
                /> */}
                  {/**TODO- enable once issue is solved:
                   * https://github.com/inveniosoftware/invenio-app-rdm/issues/738
                   */}
                  {/* <LanguagesField
                    initialOptions={_get(
                      this.props.record,
                      "ui.languages",
                      []
                    ).filter((lang) => lang !== null)} // needed because dumped empty record from backend gives [null]
                    serializeSuggestions={(suggestions) =>
                      suggestions.map((item) => ({
                        text: item.title_l10n,
                        value: item.id,
                        key: item.id,
                      }))
                    }
                  /> */}
                  <DatesField options={this.vocabularies.metadata.dates} />
                  <VersionField />
                  <PublisherField required />
                  <br />
                </AccordionField>
                {/**TODO: uncomment to use FundingField*/}
                {/* <AccordionField
                fieldPath=""
                active={true}
                label={"Funding"}
                ui={this.accordionStyle}
              >
                <FundingField options={this.vocabularies.metadata.funding} />
                <ComingSoonField
                  fieldPath="metadata.funding"
                  label="Awards"
                  labelIcon="money bill alternate outline"
                />

                <br />
              </AccordionField> */}

                <AccordionField
                  fieldPath=""
                  active={true}
                  label={"Related works"}
                  ui={this.accordionStyle}
                >
                  <RelatedWorksField
                    options={this.vocabularies.metadata.related_identifiers}
                  />
                  <br />
                </AccordionField>
              </Grid.Column>
              <Ref innerRef={this.sidebarRef}>
                <Grid.Column width={5} className="deposit-sidebar">
                  <Sticky context={this.sidebarRef} offset={20}>
                    <Card className="actions">
                      <Card.Content>
                        <SaveButton fluid className="save-button" />
                        <PublishButton fluid />
                      </Card.Content>
                    </Card>

                    <Card className="actions">
                      <Card.Content>
                        <DeleteButton
                          fluid
                          // TODO: make is_published part of the API response
                          //       so we don't have to do this
                          isPublished={this.props.record.is_published}
                        />
                      </Card.Content>
                    </Card>

                    <AccessRightField
                      label={"Protection"}
                      labelIcon={"shield"}
                    />
                    {this.config.data_cite && (
                      <DoiMint
                        record={this.props.record}
                        config={this.config.data_cite}
                      />
                    )}
                  </Sticky>
                </Grid.Column>
              </Ref>
            </Grid.Row>
          </Grid>
        </Container>
      </DepositFormApp>
    );
  }
}
