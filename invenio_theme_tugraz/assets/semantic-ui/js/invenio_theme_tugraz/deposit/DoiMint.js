import React, { Component } from "react";
import {
  Button,
  Card,
  Icon,
  Label,
  Loader,
  Dimmer,
  Message,
} from "semantic-ui-react";
import { FieldArray } from "formik";

import { DoiRest, MapDatacite, DecryptAES } from "datacite-rest";

export class DoiMint extends Component {
  constructor(props) {
    super(props);
    this.record = props.record || {};
    this.configs = props.config || {};
    this.metadata = this.record.metadata;
    this.is_doi = false;
    this.id_doi = "";

    // check for existing identifiers
    if (
      typeof this.metadata.identifiers != "undefined" &&
      this.metadata.identifiers != null &&
      this.metadata.identifiers.length != null &&
      this.metadata.identifiers.length > 0 &&
      this.metadata.identifiers[0] != null
    ) {
      this.is_doi = true;
      this.id_doi = this.metadata.identifiers[0].identifier;
    }

    // add metadata to the state
    this.state = {
      identifiers: [],
      showLoader: false,
      doi_id: "",
      errorMsg: "",
      isError: false,
    };
  }

  render() {
    // this should fetch a new doi
    var pushDoi = (form) => {
      // activate the loader
        this.setState({
          showLoader: true,
        });

      // Decrypt the password
      const _decrypted = DecryptAES(
        this.configs.datacite_pass,
        "01ab38d5e05c92aa098921d9d4626107133c7e2ab0e4849558921ebcc242bcb0",
        this.configs.datacite_password_iv
      );

      // TODO: Get values from backend
      // make request for a new DOI
      const url = this.configs.datacite_url;
      const auth = {
        username: this.configs.datacite_uname,
        password: _decrypted,
      };
      const prefix = this.configs.datacite_prefix;

      // get mapped DOI
      const mapped = MapDatacite(this.metadata, this.record.id, prefix);

      const _doirest = new DoiRest(url);

      // Create a new DOI
      _doirest
        .create(mapped, auth)
        .then((data) => {
          // if there is an error
          if (data.data.errors) {
            this.setState({
              showLoader: false,
              isError: true,
              errorMsg: data.data.errors[0].title,
            });
            // if credentials are wrong!
          } else if (data.code == 405) {
            this.setState({
              showLoader: false,
              isError: true,
              errorMsg: "Not configured!",
            });
          }
          // new doi is fetched
          else {
            // add new identifier
            const _identifiers = [
              {
                identifier: data.data.data.id,
                scheme: "doi",
              },
            ];
            // submit the value to the form
            this.setState({ identifiers: _identifiers });
            form.setFieldValue("metadata.identifiers", this.state.identifiers);

            this.is_doi = true;
            // deactivate the loader
            this.setState({
              showLoader: false,
              doi_id: this.state.identifiers[0].identifier,
            });
          }
        })
        .catch((error) => {
          console.log("error", error);
        });
    };

    // get a link of dio
    var doiLink = (doiId) => {
      window.open(`https://doi.org/${doiId}`, "_blank");
    };

    return (
      <Card className="actions">
        <Card.Content>
          <Card.Header>
            <Icon name="certificate" />
            Datacite DOI
          </Card.Header>
          <Card.Description>
            <span style={{ color: "#B6B6B6" }}>
              Record must be a <b>published</b> record to mint a DOI.
            </span>
          </Card.Description>

          {this.state.isError && (
            <Message negative>
              <Message.Header>{this.state.errorMsg}</Message.Header>
              <p>Please contact Repository supporters!</p>
            </Message>
          )}

          {/* when the Component is rendered */}
          {!this.is_doi && (
            <FieldArray name="metadata.identifiers">
              {(fieldArrayProps) => {
                const { form } = fieldArrayProps;
                return (
                  <div
                    style={{
                      marginTop: "10px",
                      textAlign: "center",
                    }}
                  >
                    <Button
                      compact
                      className="save-button"
                      disabled={!this.record.is_published}
                      as={"label"}
                      color="green"
                      size="large"
                      onClick={() => pushDoi(form)}
                    >
                      <Icon name="certificate" />
                      Get DOI Now!
                    </Button>
                    {this.state.showLoader && (
                      <Dimmer active inverted>
                        <Loader inverted>Loading...</Loader>
                      </Dimmer>
                    )}
                  </div>
                );
              }}
            </FieldArray>
          )}

          {this.is_doi && (
            <div
              style={{
                textAlign: "center",
                marginTop: "10px",
              }}
            >
              <Label
                style={{
                  cursor: "pointer",
                }}
                size="large"
                as="a"
                color="blue"
                onClick={() => doiLink(this.state.doi_id || this.id_doi)}
              >
                <strong>DOI: </strong>
                <Label.Detail>{this.state.doi_id || this.id_doi}</Label.Detail>
              </Label>
            </div>
          )}
        </Card.Content>
      </Card>
    );
  }
}
