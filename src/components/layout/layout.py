import dash_bootstrap_components as dbc
from dash import html, dcc

from components.layout.inputs_controls.inputs_controls import aside
from components.layout.navbar.navbar import navbar
from components.layout.tabs.tabs import tabs


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
        dcc.Store(id="raw-discharge", storage_type="memory"),
        dcc.Store(id="raw-reservoir", storage_type="memory"),
        dcc.Store(id="raw-met", storage_type="memory"),
        dbc.Button(id="start_button", style={"display": "none"}),
        dbc.Button(id="discharge-status-btn", style={"display": "none"}),
        dbc.Button(id="reservoir-status-btn", style={"display": "none"}),
        dbc.Button(id="met-status-btn", style={"display": "none"}),
        html.Button(
            id="data-downloaded-signal",
            style={"display": "none"},
        ),
    ]
