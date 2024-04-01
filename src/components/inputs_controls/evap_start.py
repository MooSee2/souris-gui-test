from datetime import date

import dash_bootstrap_components as dbc
from dash import dcc, html

import app_data.stations as const


def evap_start():
    return html.Div(
        className="input-container",
        children=[
            html.Div(
                className="header-info-container",
                children=[
                    html.Div(
                        className="HH6",
                        children="Evaporation Start",
                    ),
                    html.Div(
                        id="evap-start-tip",
                        className="info-container",
                        children=html.Div(className="fa-solid fa-info"),
                    ),
                ],
            ),
            dbc.Tooltip(
                "The start date for evaporation. Used to determine when to start evaporative loss calculations.  By default, April-15th.",
                target="evap-start-tip",
            ),
            # style={"width": "100%"},
            dcc.DatePickerSingle(
                id="evap-start-picker",
                className="evap-date-picker",
                date=date(const.current_year, 4, 15),
            ),
        ],
    )
