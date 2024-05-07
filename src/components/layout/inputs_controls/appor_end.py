from datetime import datetime as dt
from datetime import date

import dash_bootstrap_components as dbc
from dash import dcc, html


def appor_end():
    return html.Div(
        className="input-container",
        children=[
            html.Div(
                className="header-info-container",
                children=[
                    html.Div(className="HH6", children="Apportionment End"),
                    html.Div(
                        id="appor-end-tip",
                        className="info-container",
                        children=html.Div(className="fa-solid fa-info"),
                    ),
                ],
            ),
            dbc.Tooltip(
                "The end date for apportionment. By default, December-31th.",
                target="appor-end-tip",
            ),
            dcc.DatePickerSingle(
                id="appor-end-picker",
                className="evap-date-picker",
                date=date(int(dt.now().year), 12, 31),
                with_portal=True,
            ),
        ],
    )
