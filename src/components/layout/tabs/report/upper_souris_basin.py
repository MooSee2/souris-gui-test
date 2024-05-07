from dash import html


def make_upper_souris_basin_panel():
    return html.Div(
        className="report-panel",
        id="upper-souris-basin-panel",
        children=[
            html.Div(
                className="report-table-header",
                children=[
                    html.H6("Upper Souris River Basin - Above Estevan"),
                ],
            ),
            html.Div(
                className="report-table-body-long",
                children=[
                    # Nickle reservoir
                    html.Div(
                        id="nickle-reservoir-header",
                        className="box-header",
                        children=[html.Div("Nickle Lake Reservoir")],
                    ),
                    html.Div(
                        className="box-number",
                        id="box-14-header",
                        children=["14"],
                    ),
                    html.Div(
                        className="box-number",
                        id="box-15-header",
                        children=["15"],
                    ),
                    html.Div(
                        className="box-number",
                        id="box-16-header",
                        children=["16"],
                    ),
                    html.Div(
                        className="box-number",
                        id="box-17-header",
                        children=["17"],
                    ),
                    html.Div(
                        className="box-content",
                        id="box-14-container",
                        children=[
                            html.Div(className="box-content-title", children=["Storage Change"]),
                            html.Div(className="box-content-value", id="box-14-value", children=["-"]),
                            html.Div(className="box-content-subscript", children=[" "]),
                        ],
                    ),
                    html.Div(
                        className="box-content",
                        id="box-15-container",
                        children=[
                            html.Div(className="box-content-title", children=["Net Evaporation and Seepage"]),
                            html.Div(className="box-content-value", id="box-15-value", children=["-"]),
                            html.Div(className="box-content-subscript", children=[" "]),
                        ],
                    ),
                    html.Div(
                        className="box-content",
                        id="box-16-container",
                        children=[
                            html.Div(className="box-content-title", children=["City of Weyburn Pumpage"]),
                            html.Div(className="box-content-value", id="box-16-value", children=["-"]),
                            html.Div(className="box-content-subscript", children=[" "]),
                        ],
                    ),
                    html.Div(
                        className="box-content",
                        id="box-17-container",
                        children=[
                            html.Div(className="box-content-title", children=["Diversion"]),
                            html.Div(className="box-content-value", id="box-17-value", children=["-"]),
                            html.Div(className="box-content-subscript", children=["14+15+16"]),
                        ],
                    ),
                    # Box 18
                    html.Div(
                        className="box-number",
                        id="box-18-header",
                        children=["18"],
                    ),
                    html.Div(
                        className="box-content",
                        id="box-18-container",
                        children=[
                            html.Div(className="box-content-title", children=["City of Weyburn Return Flow"]),
                            html.Div(className="box-content-value", id="box-18-value", children=["-"]),
                            html.Div(className="box-content-subscript", children=[" "]),
                        ],
                    ),
                    # Roughbark reservoir
                    html.Div(
                        id="roughbark-reservoir-header",
                        className="box-header",
                        children=[html.Div("Roughbark Reservoir")],
                    ),
                    html.Div(
                        className="box-number",
                        id="box-19-header",
                        children=["19"],
                    ),
                    html.Div(
                        className="box-number",
                        id="box-20-header",
                        children=["20"],
                    ),
                    html.Div(
                        className="box-number",
                        id="box-21-header",
                        children=["21"],
                    ),
                    html.Div(
                        className="box-content",
                        id="box-19-container",
                        children=[
                            html.Div(className="box-content-title", children=["Storage Change"]),
                            html.Div(className="box-content-value", id="box-19-value", children=["-"]),
                            html.Div(className="box-content-subscript", children=[" "]),
                        ],
                    ),
                    html.Div(
                        className="box-content",
                        id="box-20-container",
                        children=[
                            html.Div(className="box-content-title", children=["Net Evaporation and Seepage"]),
                            html.Div(className="box-content-value", id="box-20-value", children=["-"]),
                            html.Div(className="box-content-subscript", children=[" "]),
                        ],
                    ),
                    html.Div(
                        className="box-content",
                        id="box-21-container",
                        children=[
                            html.Div(className="box-content-title", children=["Diversion"]),
                            html.Div(className="box-content-value", id="box-21-value", children=["-"]),
                            html.Div(className="box-content-subscript", children=["19+20+21"]),
                        ],
                    ),
                    # # Rafferty reservoir
                    html.Div(
                        id="rafferty-reservoir-header",
                        className="box-header",
                        children=[html.Div("Rafferty Reservoir")],
                    ),
                    html.Div(
                        className="box-number",
                        id="box-22-header",
                        children=["22"],
                    ),
                    html.Div(
                        className="box-number",
                        id="box-23-header",
                        children=["23"],
                    ),
                    html.Div(
                        className="box-number",
                        id="box-24-header",
                        children=["24"],
                    ),
                    html.Div(
                        className="box-content",
                        id="box-22-container",
                        children=[
                            html.Div(className="box-content-title", children=["Inflow"]),
                            html.Div(className="box-content-value", id="box-22-value", children=["-"]),
                            html.Div(className="box-content-subscript", children=[" "]),
                        ],
                    ),
                    html.Div(
                        className="box-content",
                        id="box-23-container",
                        children=[
                            html.Div(className="box-content-title", children=["Outflow"]),
                            html.Div(className="box-content-value", id="box-23a-value", children=["-"]),
                            html.Div(className="box-content-subscript", children=[" "]),
                        ],
                    ),
                    html.Div(
                        className="box-content",
                        id="box-24-container",
                        children=[
                            html.Div(className="box-content-title", children=["Diversion"]),
                            html.Div(className="box-content-value", id="box-24-value", children=["-"]),
                            html.Div(className="box-content-subscript", children=["22-23"]),
                        ],
                    ),
                    # # Boxes 25 - 26
                    html.Div(
                        className="box-number",
                        id="box-25-header",
                        children=["25"],
                    ),
                    html.Div(
                        className="box-number",
                        id="box-26-header",
                        children=["26"],
                    ),
                    html.Div(
                        className="box-content",
                        id="box-25-container",
                        children=[
                            html.Div(className="box-content-title", children=["Minor Project Diversions"]),
                            html.Div(className="box-content-value", id="box-25-value", children=["-"]),
                            html.Div(className="box-content-subscript", children=[" "]),
                        ],
                    ),
                    html.Div(
                        className="box-content",
                        id="box-26-container",
                        children=[
                            html.Div(className="box-content-title", children=["Total Diversion Upper Souris River"]),
                            html.Div(className="box-content-value", id="box-26-value", children=["-"]),
                            html.Div(className="box-content-subscript", children=["17-18+21+24+25"]),
                        ],
                    ),
                ],
            ),
        ],
    )
