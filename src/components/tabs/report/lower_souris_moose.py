import dash_bootstrap_components as dbc
from dash import html


def make_lower_souris_moose_panel():
    return html.Div(
        className="report-panel",
        id="lower-souris-moose-panel",
        children=[
            html.Div(className="report-table-header"),
            html.Div(className="report-table-body"),
        ],
    )
