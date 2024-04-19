import dash_bootstrap_components as dbc
from dash import html, dcc

from components.inputs_controls.inputs_controls import aside
from components.navbar.navbar import navbar
from components.tabs.tabs import tabs


def make_main():
    return html.Main(
        children=html.Div(
            id="tab-container",
            children=[
                tabs(),
            ],
        )
    )


def make_layout():
    return [
        navbar(),
        html.Div(
            id="interior-container",
            children=[
                aside(),
                make_main(),
            ],
        ),
        dcc.Download(id="report-download"),
        dbc.Button(id="start_button", style={"display": "none"}),
        dbc.Button(id="discharge-status-btn", style={"display": "none"}),
        dbc.Button(id="reservoir-status-btn", style={"display": "none"}),
        dbc.Button(id="met-status-btn", style={"display": "none"}),
        html.Button(
            id="data-downloaded-signal",
            style={"display": "none"},
        ),
    ]
