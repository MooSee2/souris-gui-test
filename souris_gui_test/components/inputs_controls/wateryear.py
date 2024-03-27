from dash import html, dcc
import dash_bootstrap_components as dbc
from data import stations as const

wateryear = html.Div(
    className="input-container",
    children=[
        html.Div(
            className="header-info-container",
            children=[
                html.Div(
                    className="HH6",
                    children=["Water year"],
                ),
                html.Div(id="water-year-tip", className="info-container", children=html.Div(className="fa-solid fa-info")),
            ],
        ),
        dbc.Tooltip(
            "This is a bunch, " "of test text to explain what this field is for.",
            target="water-year-tip",
        ),
        dcc.Dropdown(
            id="apportionment-year",
            options=const.available_years,
            clearable=False,
            value=const.current_year,
        ),
    ],
)
