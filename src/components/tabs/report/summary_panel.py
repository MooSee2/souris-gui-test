import dash_bootstrap_components as dbc
from dash import html


def make_summary_panel():
    return html.Div(
        className="report-panel",
        id="summary-panel",
        children=[
            html.Div(
                className="report-table-header",
                children=[
                    html.H6("Summary"),
                ],
            ),
            html.Div(
                className="report-table-body-long",
                children=[
                    # Non-contributory basins
                    html.Div(
                        id="non-contributory-header",
                        className="box-header",
                        children=[html.Div("Non-Contributory Basins")],
                    ),
                    html.Div(
                        className="box-number",
                        id="box-39-header",
                        children=["39"],
                    ),
                    html.Div(
                        className="box-number",
                        id="box-40-header",
                        children=["40"],
                    ),
                    html.Div(
                        className="box-number",
                        id="box-41-header",
                        children=["41"],
                    ),
                    html.Div(
                        className="box-content",
                        id="box-39-container",
                        children=[
                            html.Div(className="box-content-title", children=["Yellow Grass Ditch"]),
                            html.Div(className="box-content-value", id="box-39-value", children=["-"]),
                            html.Div(className="box-content-subscript", children=[" "]),
                        ],
                    ),
                    html.Div(
                        className="box-content",
                        id="box-40-container",
                        children=[
                            html.Div(className="box-content-title", children=["Tatagwa Lake Drain"]),
                            html.Div(className="box-content-value", id="box-40-value", children=["-"]),
                            html.Div(className="box-content-subscript", children=[" "]),
                        ],
                    ),
                    html.Div(
                        className="box-content",
                        id="box-41-container",
                        children=[
                            html.Div(className="box-content-title", children=["Total Additions"]),
                            html.Div(className="box-content-value", id="box-41-value", children=["-"]),
                            html.Div(className="box-content-subscript", children=["39+40"]),
                        ],
                    ),
                    # Summary of Natural Flow
                    html.Div(
                        id="summary-header",
                        className="box-header",
                        children=[html.Div("Summary of Natural Flow")],
                    ),
                    html.Div(
                        className="box-number",
                        id="box-42-header",
                        children=["42"],
                    ),
                    html.Div(
                        className="box-number",
                        id="box-43-header",
                        children=["43"],
                    ),
                    html.Div(
                        className="box-number",
                        id="box-44-header",
                        children=["44"],
                    ),
                    html.Div(
                        className="box-number",
                        id="box-45-header",
                        children=["45"],
                    ),
                    html.Div(
                        className="box-number",
                        id="box-46-header",
                        children=["46"],
                    ),
                    html.Div(
                        className="box-number",
                        id="box-47-header",
                        children=["47"],
                    ),
                    html.Div(
                        className="box-content",
                        id="box-42-container",
                        children=[
                            html.Div(className="box-content-title", children=["Total Diversion Souris River Basin"]),
                            html.Div(className="box-content-value", id="box-42-value", children=["-"]),
                            html.Div(className="box-content-subscript", children=["13+26+30+38"]),
                        ],
                    ),
                    html.Div(
                        className="box-content",
                        id="box-43-container",
                        children=[
                            html.Div(className="box-content-title", children=["Recorded Flow at Sherwood"]),
                            html.Div(className="box-content-value", id="box-43-value", children=["-"]),
                            html.Div(className="box-content-subscript", children=[" "]),
                        ],
                    ),
                    html.Div(
                        className="box-content",
                        id="box-44-container",
                        children=[
                            html.Div(className="box-content-title", children=["Natural Flow at Sherwood"]),
                            html.Div(className="box-content-value", id="box-44-value", children=["-"]),
                            html.Div(className="box-content-subscript", children=["32+43-41"]),
                        ],
                    ),
                    html.Div(
                        className="box-content",
                        id="box-45-container",
                        children=[
                            html.Div(className="box-content-title", children=["USA Share"]),
                            html.Div(className="box-content-value", id="box-45a-value", children=["-"]),
                            html.Div(className="box-content-subscript", children=[" "]),
                        ],
                    ),
                    html.Div(
                        className="box-content",
                        id="box-46-container",
                        children=[
                            html.Div(className="box-content-title", children=["Flow Received by USA"]),
                            html.Div(className="box-content-value", id="box-46-value", children=["-"]),
                            html.Div(className="box-content-subscript", children=["12+28+43"]),
                        ],
                    ),
                    html.Div(
                        className="box-content",
                        id="box-47-container",
                        children=[
                            html.Div(className="box-content-title", children=["Surplus or Deficit to USA"]),
                            html.Div(className="box-content-value", id="box-47a-value", children=["-"]),
                            html.Div(className="box-content-subscript", children=[" "]),
                        ],
                    ),
                    # Boxes 48 - 50
                    html.Div(
                        id="annual-flow-header",
                        className="box-header",
                        children=[html.Div("Annual Flow of Long Creek")],
                    ),
                    html.Div(
                        className="box-number",
                        id="box-48-header",
                        children=["48"],
                    ),
                    html.Div(
                        className="box-number",
                        id="box-49-header",
                        children=["49"],
                    ),
                    html.Div(
                        className="box-number",
                        id="box-50-header",
                        children=["50"],
                    ),
                    html.Div(
                        className="box-content",
                        id="box-48-container",
                        children=[
                            html.Div(className="box-content-title", children=["Recorded Flow at Western Crossing"]),
                            html.Div(className="box-content-value", id="box-48-value", children=["-"]),
                            html.Div(className="box-content-subscript", children=[" "]),
                        ],
                    ),
                    html.Div(
                        className="box-content",
                        id="box-49-container",
                        children=[
                            html.Div(className="box-content-title", children=["Recorded Flow at Eastern Crossing"]),
                            html.Div(className="box-content-value", id="box-49-value", children=["-"]),
                            html.Div(className="box-content-subscript", children=[" "]),
                        ],
                    ),
                    html.Div(
                        className="box-content",
                        id="box-50-container",
                        children=[
                            html.Div(className="box-content-title", children=["Surplus or Deficit From USA"]),
                            html.Div(className="box-content-value", id="box-50-value", children=["-"]),
                            html.Div(className="box-content-subscript", children=["49-48"]),
                        ],
                    ),
                ],
            ),
        ],
    )
