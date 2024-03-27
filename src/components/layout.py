import dash_bootstrap_components as dbc
from components.inputs_controls.inputs_controls import aside
from components.navbar.navbar import navbar
from components.tabs import discharge, graphs, met_data, report, reported_flows, reservoirs
from dash import html


def make_main():
    return html.Main(
        children=[
            dbc.Tabs(
                [
                    reported_flows(),
                    discharge(),
                    reservoirs(),
                    met_data(),
                    report(),
                    graphs(),
                ],
            ),
        ],
    )


def make_layout():
    return [
        navbar(),
        html.Div(
            id="interior-container",
            children=[
                aside,
                make_main(),
            ],
        ),
        dbc.Button(id="start_button", style={"display": "none"}),
        html.Button(
            id="data-downloaded-signal",
            style={
                "display": "none",
            },
        ),
    ]
