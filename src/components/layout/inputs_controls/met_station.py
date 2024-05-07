import dash_bootstrap_components as dbc
from dash import dcc, html


def met_station():
    return html.Div(
        className="input-container",
        children=[
            html.Div(
                className="header-info-container",
                children=[
                    html.Div(
                        className="HH6",
                        children="Met Station",
                    ),
                    html.Div(
                        id="met-station-tip",
                        className="info-container",
                        children=html.Div(
                            className="fa-solid fa-info",
                        ),
                    ),
                ],
            ),
            dbc.Tooltip(
                children=[
                    "This is a bunch, " "of test text to explain what this field is for.",
                ],
                target="met-station-tip",
            ),
            dcc.Dropdown(
                options=[
                    {"label": "Gildford", "value": "Gildford"},
                    {"label": "Eastern Crossing", "value": "MRatEC"},
                ],
                value="MRatEC",
                clearable=False,
            ),
        ],
    )
