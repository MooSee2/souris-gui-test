import dash_bootstrap_components as dbc
from dash import html


def report():
    return dbc.Tab(
        label="Report",
        tab_id="report-tab",
        children=dbc.Card(
            className="mt-3",
            children=dbc.CardBody(
                id="report-container",
                children=[
                    html.Div(
                        className="report-panel",
                        id="long-creek-basin",
                        children=[
                            html.Div(
                                className="report-table-header",
                                children=[
                                    html.H6("Long Creek Basin"),
                                ],
                            ),
                            html.Div(
                                className="report-table-body-long",
                                children=[
                                    # Larsen
                                    html.Div(
                                        id="larsen-reservoir-header",
                                        className="box-header",
                                        children=[html.H6("Larsen Reservoir")],
                                    ),
                                    html.Div(
                                        className="box-number",
                                        id="larsen-reservoir-box-1",
                                        children=["1"],
                                    ),
                                    html.Div(
                                        className="box-number",
                                        id="larsen-reservoir-box-2",
                                        children=["2"],
                                    ),
                                    html.Div(
                                        className="box-number",
                                        id="larsen-reservoir-box-3",
                                        children=["3"],
                                    ),
                                    html.Div(
                                        className="box-container",
                                        id="box-1",
                                        children=["100"],
                                    ),
                                    html.Div(
                                        className="box-container",
                                        id="box-2",
                                        children=["200"],
                                    ),
                                    html.Div(
                                        className="box-container",
                                        id="box-3",
                                        children=["300"],
                                    ),
                                    # Radville
                                    html.Div(
                                        className="box-number",
                                        id="radville-box-4",
                                        children=["4"],
                                    ),
                                    html.Div(
                                        className="box-container",
                                        id="box-4",
                                        children=["Radville"],
                                    ),
                                    # Boundary Reservoir
                                    html.Div(
                                        id="boundary-reservoir-header",
                                        className="box-header",
                                        children=[html.H6("Boundary Reservoir")],
                                    ),
                                ],
                            ),
                        ],
                    ),
                    html.Div(
                        className="report-panel",
                        id="upper-souris-basin",
                        children=[
                            html.Div(className="report-table-header"),
                            html.Div(
                                className="report-table-body-long",
                                children=[
                                    html.Div(id="larsen-reservoir", children=html.Div(children=["Nickle Lake Reservoir"])),
                                ],
                            ),
                        ],
                    ),
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
