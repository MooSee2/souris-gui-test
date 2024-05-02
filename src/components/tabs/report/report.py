import dash_bootstrap_components as dbc
from dash import html
from components.tabs.report.long_creek_basin import make_long_creek_panel
from components.tabs.report.upper_souris_basin import make_upper_souris_basin_panel


def make_report_panels():
    return dbc.Tab(
        label="Report",
        tab_id="report-tab",
        children=dbc.Card(
            className="mt-3",
            children=dbc.CardBody(
                id="report-container",
                children=[
                    make_long_creek_panel(),
                    make_upper_souris_basin_panel(),
                    html.Div(
                        className="report-panel",
                        id="lower-souris-moose-basin",
                        children=[
                            html.Div(className="report-table-header"),
                            html.Div(className="report-table-body"),
                        ],
                    ),
                    html.Div(
                        className="report-panel",
                        id="summary",
                        children=[
                            html.Div(className="report-table-header"),
                            html.Div(className="report-table-body"),
                        ],
                    ),
                ],
            ),
        ),
    )
