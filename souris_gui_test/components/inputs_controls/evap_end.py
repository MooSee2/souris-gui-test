from datetime import datetime as dt
from datetime import date

import dash_bootstrap_components as dbc
from dash import dcc, html

evap_end = html.Div(
        className="input-container",
        children=[
            html.Div(
                className="header-info-container",
                children=[
                    html.Div(className="HH6", children="Evaporation End"),
                    html.Div(id="evap-end-tip", className="info-container", children=html.Div(className="fa-solid fa-info")),
                ],
            ),
            dbc.Tooltip(
                "This is a bunch, " "of test text to explain what this field is for.",
                target="evap-end-tip",
            ),
            dcc.DatePickerSingle(id="evap-end-picker", className="evap-date-picker", date=date(int(dt.now().year), 10, 15)),
        ],
    )
