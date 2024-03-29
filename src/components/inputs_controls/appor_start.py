from datetime import date
from datetime import datetime as dt

import dash_bootstrap_components as dbc
from dash import dcc, html

import app_data.stations as const


def appor_start():
    return html.Div(
        className="input-container",
        children=[
            html.Div(
                className="header-info-container",
                children=[
                    html.Div(
                        className="HH6",
                        children="Apportionment Start",
                    ),
                    html.Div(id="appor-start-tip", className="info-container", children=html.Div(className="fa-solid fa-info")),
                ],
            ),
            dbc.Tooltip(
                "The start date for apportionment. By default, January-1st.",
                target="appor-start-tip",
            ),
            # style={"width": "100%"},
            dcc.DatePickerSingle(id="appor-start-picker", className="evap-date-picker", date=date(const.current_year, 1, 1)),
        ],
    )
