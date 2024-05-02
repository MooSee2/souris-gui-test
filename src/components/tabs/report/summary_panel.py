import dash_bootstrap_components as dbc
from dash import html


def make_summary_panel():
    return html.Div(
        className="report-panel",
        id="summary-panel",
        children=[
            html.Div(className="report-table-header"),
            html.Div(className="report-table-body"),
        ],
    )
