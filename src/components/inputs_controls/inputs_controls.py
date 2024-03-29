import dash_bootstrap_components as dbc
from dash import dcc, html
from components.inputs_controls import evap_start, evap_end, met_station, wateryear, appor_start, appor_end

load_modal = dbc.Modal(
    [
        dbc.ModalHeader(dbc.ModalTitle("Load Application Data")),
        dbc.ModalBody(
            id="load-modal-body",
            children=[
                dbc.Button(
                    id="query-data-button",
                    children=["Query data from web"],
                ),
                html.Div(
                    id="loading-wrapper",
                    style={"flex-grow": "1"},
                    children=[
                        dcc.Loading(
                            children=html.Div(
                                id="loading-data-div",
                                children=["Load data from the web."],
                            ),
                        ),
                    ],
                ),
            ],
        ),
        dbc.ModalFooter(),
    ],
    id="load-data-modal",
    is_open=False,
)


def aside():
    return html.Div(
        className="asideaside",
        children=[
            load_modal,
            # dbc.Modal(
            #     [
            #         dbc.ModalHeader(
            #             dbc.ModalTitle("Load Application Data"),
            #         ),
            #         dbc.ModalBody(
            #             id="load-modal-body",
            #             children=[
            #                 dbc.Button(
            #                     id="query-data-button",
            #                     children=["Query data from web"],
            #                 ),
            #                 html.Div(
            #                     id="loading-wrapper",
            #                     style={"flex-grow": "1"},
            #                     children=[
            #                         dcc.Loading(
            #                             children=html.Div(
            #                                 id="loading-data-div",
            #                                 children=["Load data from the web."],
            #                             ),
            #                         ),
            #                     ],
            #                 ),
            #             ],
            #         ),
            #         dbc.ModalFooter(),
            #     ],
            #     id="load-data-modal",
            #     is_open=False,
            # ),
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
                    dbc.Button(
                        "Load Data",
                        color="secondary",
                        id="load-data-button",
                        n_clicks=0,
                    ),
                ],
            ),
            html.Div(
                className="config-card",
                children=[
                    dbc.Button(
                        "Begin Apportionment",
                        color="secondary",
                        id="apportion-button",
                        disabled=True,
                    ),
                ],
            ),
        ],
    )
