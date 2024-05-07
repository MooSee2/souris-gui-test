from datetime import date
from datetime import datetime as dt

import dash_bootstrap_components as dbc
from dash import dcc, html


def evap_end():
    return html.Div(
        className="input-container",
        children=[
            html.Div(
                className="header-info-container",
                children=[
                    html.Div(className="HH6", children="Evaporation End"),
                    html.Div(
                        id="evap-end-tip",
                        className="info-container",
                        children=html.Div(className="fa-solid fa-info"),
                    ),
                ],
            ),
            dbc.Tooltip(
                "The end date for evaporation. Used to determine when to end evaporative loss calculations.  By default, October-15th.",
                target="evap-end-tip",
            ),
            dcc.DatePickerSingle(
                id="evap-end-picker",
                className="evap-date-picker",
                date=date(int(dt.now().year), 10, 31),
                with_portal=True,
            ),
        ],
    )
