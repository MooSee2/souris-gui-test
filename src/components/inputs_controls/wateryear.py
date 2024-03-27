from dash import html, dcc
import dash_bootstrap_components as dbc
from app_data import stations as const

wateryear = html.Div(
    className="input-container",
    children=[
        html.Div(
            className="header-info-container",
            children=[
                html.Div(
                    className="HH6",
                    children=["Apportionment Year"],
                ),
                html.Div(id="apport-year-tip", className="info-container", children=html.Div(className="fa-solid fa-info")),
            ],
        ),
        dbc.Tooltip(
            "The year to apportion.  By default, the current year.",
            target="apport-year-tip",
        ),
        dcc.Dropdown(
            id="apportionment-year",
            options=const.available_years,
            clearable=False,
            value=const.current_year,
        ),
    ],
)
