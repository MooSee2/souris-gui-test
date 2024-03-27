from datetime import date

import dash_bootstrap_components as dbc
import app_data.stations as const
from dash import dcc, html

evap_start = html.Div(
    className="input-container",
    children=[
        html.Div(
            className="header-info-container",
            children=[
                html.Div(
                    className="HH6",
                    children="Evaporation Start",
                ),
                html.Div(id="evap-start-tip", className="info-container", children=html.Div(className="fa-solid fa-info")),
            ],
        ),
        dbc.Tooltip(
            "This is a bunch, " "of test text to explain what this field is for.",
            target="evap-start-tip",
        ),
        # style={"width": "100%"},
        dcc.DatePickerSingle(id="evap-start-picker", className="evap-date-picker", date=date(const.current_year, 4, 15)),
    ],
)
