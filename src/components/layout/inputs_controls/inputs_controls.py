import dash_bootstrap_components as dbc
from dash import dcc, html

from components.layout.inputs_controls import (
    appor_end,
    appor_start,
    evap_end,
    evap_start,
    wateryear,
    credentials,
)

calculation_modal = dbc.Modal(
    [
        dbc.ModalHeader(
            dbc.ModalTitle(
                children=[
                    "Missing Reported Flows Detected",
                ],
                id="calc-modal-title",
            ),
            id="calc-modal-header",
        ),
        dbc.ModalBody(
            children=[
                html.P(
                    children=[
                        "Missing data will be filled in with '0' values.",
                    ],
                ),
                html.Div(
                    id="calc-modal-body",
                    children=[
                        dbc.Button(
                            id="calc-continue-button",
                            children=[
                                "Continue with apportionment",
                            ],
                        ),
                        dbc.Button(
                            id="calc-cancel-button",
                            children=["Cancel"],
                        ),
                    ],
                ),
            ],
        ),
        dbc.ModalFooter(),
    ],
    id="calculation-modal",
    is_open=False,
)


def aside():
    return html.Div(
        className="asideaside",
        children=[
            html.Div(
                className="config-card",
                children=[
                    html.H4("Credentials"),
                    credentials.credentials(),
                ],
            ),
            html.Div(
                className="config-card",
                children=[
                    html.H4("Settings"),
                    wateryear.wateryear(),
                    appor_start.appor_start(),
                    appor_end.appor_end(),
                    evap_start.evap_start(),
                    evap_end.evap_end(),
                ],
            ),
            html.Div(
                className="config-card",
                children=[
                    dcc.Loading(
                        dbc.Button(
                            "Load Data",
                            color="secondary",
                            id="load-data-button",
                            n_clicks=0,
                            className="usa-menu-btn",
                        ),
                    )
                ],
            ),
            calculation_modal,
            html.Div(
                className="config-card",
                children=[
                    dcc.Loading(
                        dbc.Button(
                            "Begin Apportionment",
                            color="secondary",
                            id="apportion-button",
                            className="usa-menu-btn",
                        ),
                    ),
                ],
            ),
        ],
    )
