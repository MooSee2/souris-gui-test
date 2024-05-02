import dash_bootstrap_components as dbc
from dash import html


def make_long_creek_panel():
    return html.Div(
        className="report-panel",
        id="long-creek-basin-panel",
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
                        children=[html.Div("Larsen Reservoir")],
                    ),
                    html.Div(
                        className="box-number",
                        id="box-1-header",
                        children=["1"],
                    ),
                    html.Div(
                        className="box-number",
                        id="box-2-header",
                        children=["2"],
                    ),
                    html.Div(
                        className="box-number",
                        id="box-3-header",
                        children=["3"],
                    ),
                    html.Div(
                        className="box-content",
                        id="box-1-container",
                        children=[
                            html.Div(className="box-content-title", children=["Storage Change"]),
                            html.Div(className="box-content-value", id="box-1-value", children=["-"]),
                            html.Div(className="box-content-subscript", children=[" "]),
                        ],
                    ),
                    html.Div(
                        className="box-content",
                        id="box-2-container",
                        children=[
                            html.Div(className="box-content-title", children=["Net Evaporation and Seepage"]),
                            html.Div(className="box-content-value", id="box-2-value", children=["-"]),
                            html.Div(className="box-content-subscript", children=[" "]),
                        ],
                    ),
                    html.Div(
                        className="box-content",
                        id="box-3-container",
                        children=[
                            html.Div(className="box-content-title", children=["Diversion"]),
                            html.Div(className="box-content-value", id="box-3-value", children=["-"]),
                            html.Div(className="box-content-subscript", children=["1+2"]),
                        ],
                    ),
                    # Radville
                    html.Div(
                        className="box-number",
                        id="box-4-header",
                        children=["4"],
                    ),
                    html.Div(
                        className="box-content",
                        id="box-4-container",
                        children=[
                            html.Div(className="box-content-title", children=["Town of Radville Pumpage"]),
                            html.Div(className="box-content-value", id="box-4-value", children=["-"]),
                            html.Div(className="box-content-subscript", children=[" "]),
                        ],
                    ),
                    # Boundary Reservoir
                    html.Div(
                        id="boundary-reservoir-header",
                        className="box-header",
                        children=[html.Div("Boundary Reservoir")],
                    ),
                    html.Div(
                        id="inflow-header",
                        className="box-header",
                        children=[html.Div("Inflow")],
                    ),
                    html.Div(
                        id="outflow-header",
                        className="box-header",
                        children=[html.Div("Outflow")],
                    ),
                    # Long Creek at Eastern Crossing
                    html.Div(
                        className="box-number",
                        id="box-5-header",
                        children=["5"],
                    ),
                    html.Div(
                        className="box-content",
                        id="box-5-container",
                        children=[
                            html.Div(className="box-content-title", children=["Long Creek at Eastern Crossing"]),
                            html.Div(className="box-content-value", id="box-5-value", children=["-"]),
                            html.Div(className="box-content-subscript", children=[" "]),
                        ],
                    ),
                    # Boxes 6-9
                    html.Div(
                        className="box-number",
                        id="box-6-header",
                        children=["6"],
                    ),
                    html.Div(
                        className="box-number",
                        id="box-7-header",
                        children=["7"],
                    ),
                    html.Div(
                        className="box-number",
                        id="box-8-header",
                        children=["8"],
                    ),
                    html.Div(
                        className="box-number",
                        id="box-9-header",
                        children=["9"],
                    ),
                    html.Div(
                        className="box-content",
                        id="box-6-container",
                        children=[
                            html.Div(className="box-content-title", children=["Long Creek near Estevan"]),
                            html.Div(className="box-content-value", id="box-6-value", children=["-"]),
                            html.Div(className="box-content-subscript", children=[" "]),
                        ],
                    ),
                    html.Div(
                        className="box-content",
                        id="box-7-container",
                        children=[
                            html.Div(className="box-content-title", children=["Estevan Pipeline"]),
                            html.Div(className="box-content-value", id="box-7-value", children=["-"]),
                            html.Div(className="box-content-subscript", children=[" "]),
                        ],
                    ),
                    html.Div(
                        className="box-content",
                        id="box-8-container",
                        children=[
                            html.Div(className="box-content-title", children=["Diversion Canal"]),
                            html.Div(className="box-content-value", id="box-8-value", children=["-"]),
                            html.Div(className="box-content-subscript", children=[" "]),
                        ],
                    ),
                    html.Div(
                        className="box-content",
                        id="box-9-container",
                        children=[
                            html.Div(className="box-content-title", children=["Total Outflow"]),
                            html.Div(className="box-content-value", id="box-9-value", children=["-"]),
                            html.Div(className="box-content-subscript", children=["6+7+8"]),
                        ],
                    ),
                    # Box 10
                    html.Div(
                        className="box-number",
                        id="box-10-header",
                        children=["10"],
                    ),
                    html.Div(
                        className="box-content",
                        id="box-10-container",
                        children=[
                            html.Div(className="box-content-title", children=["Diversion"]),
                            html.Div(className="box-content-value", id="box-10-value", children=["-"]),
                            html.Div(className="box-content-subscript", children=["5-9"]),
                        ],
                    ),
                    # Boxes 11 - 13
                    html.Div(
                        className="box-number",
                        id="box-11-header",
                        children=["11"],
                    ),
                    html.Div(
                        className="box-number",
                        id="box-12-header",
                        children=["12"],
                    ),
                    html.Div(
                        className="box-number",
                        id="box-13-header",
                        children=["13"],
                    ),
                    html.Div(
                        className="box-content",
                        id="box-11-container",
                        children=[
                            html.Div(className="box-content-title", children=["Minor project diversions"]),
                            html.Div(className="box-content-value", id="box-11-value", children=["-"]),
                            html.Div(className="box-content-subscript", children=[""]),
                        ],
                    ),
                    html.Div(
                        className="box-content",
                        id="box-12-container",
                        children=[
                            html.Div(className="box-content-title", children=["USA diversion between Western and Eastern Crossing"]),
                            html.Div(className="box-content-value", id="box-12-value", children=["-"]),
                            html.Div(className="box-content-subscript", children=[""]),
                        ],
                    ),
                    html.Div(
                        className="box-content",
                        id="box-13-container",
                        children=[
                            html.Div(className="box-content-title", children=["Total Diversion Long Creek"]),
                            html.Div(className="box-content-value", id="box-13-value", children=["-"]),
                            html.Div(className="box-content-subscript", children=["3+4+10+11+12"]),
                        ],
                    ),
                ],
            ),
        ],
    )
