from dash import html


def make_lower_souris_moose_panel():
    return html.Div(
        className="report-panel",
        id="lower-souris-moose-panel",
        children=[
            html.Div(
                className="report-table-header",
                children=[
                    html.H6("Lower Souris River and Moose Mountain Basin"),
                ],
            ),
            html.Div(
                className="report-table-body-long",
                children=[
                    # Lower Souris River
                    html.Div(
                        id="lower-souris-river-header",
                        className="box-header",
                        children=[html.Div("Lower Souris River - Estevan to Sherwood")],
                    ),
                    html.Div(
                        className="box-number",
                        id="box-27-header",
                        children=["27"],
                    ),
                    html.Div(
                        className="box-number",
                        id="box-28-header",
                        children=["28"],
                    ),
                    html.Div(
                        className="box-number",
                        id="box-29-header",
                        children=["29"],
                    ),
                    html.Div(
                        className="box-number",
                        id="box-30-header",
                        children=["30"],
                    ),
                    html.Div(
                        className="box-content",
                        id="box-27-container",
                        children=[
                            html.Div(className="box-content-title", children=["City of Estevan Net Pumpage"]),
                            html.Div(className="box-content-value", id="box-27-value", children=["-"]),
                            html.Div(className="box-content-subscript", children=[" "]),
                        ],
                    ),
                    html.Div(
                        className="box-content",
                        id="box-28-container",
                        children=[
                            html.Div(className="box-content-title", children=["Short Creek Diversions in USA"]),
                            html.Div(className="box-content-value", id="box-28-value", children=["-"]),
                            html.Div(className="box-content-subscript", children=[" "]),
                        ],
                    ),
                    html.Div(
                        className="box-content",
                        id="box-29-container",
                        children=[
                            html.Div(className="box-content-title", children=["Minor Project Diversions"]),
                            html.Div(className="box-content-value", id="box-29-value", children=["-"]),
                            html.Div(className="box-content-subscript", children=[" "]),
                        ],
                    ),
                    html.Div(
                        className="box-content",
                        id="box-30-container",
                        children=[
                            html.Div(className="box-content-title", children=["Total Diversion Lower Souris River"]),
                            html.Div(className="box-content-value", id="box-30-value", children=["-"]),
                            html.Div(className="box-content-subscript", children=["27+28+29"]),
                        ],
                    ),
                    # Moose Mountain Lake
                    html.Div(
                        id="moose-mountain-header",
                        className="box-header",
                        children=[html.Div("Moose Mountain Lake")],
                    ),
                    html.Div(
                        className="box-number",
                        id="box-31-header",
                        children=["31"],
                    ),
                    html.Div(
                        className="box-number",
                        id="box-32-header",
                        children=["32"],
                    ),
                    html.Div(
                        className="box-number",
                        id="box-33-header",
                        children=["33"],
                    ),
                    html.Div(
                        className="box-content",
                        id="box-31-container",
                        children=[
                            html.Div(className="box-content-title", children=["Storage Change"]),
                            html.Div(className="box-content-value", id="box-31-value", children=["-"]),
                            html.Div(className="box-content-subscript", children=[" "]),
                        ],
                    ),
                    html.Div(
                        className="box-content",
                        id="box-32-container",
                        children=[
                            html.Div(className="box-content-title", children=["Net Evaporation and Seepage"]),
                            html.Div(className="box-content-value", id="box-32-value", children=["-"]),
                            html.Div(className="box-content-subscript", children=[" "]),
                        ],
                    ),
                    html.Div(
                        className="box-content",
                        id="box-33-container",
                        children=[
                            html.Div(className="box-content-title", children=["Diversion"]),
                            html.Div(className="box-content-value", id="box-33-value", children=["-"]),
                            html.Div(className="box-content-subscript", children=["31+32"]),
                        ],
                    ),
                    # # Grant divine reservoir
                    html.Div(
                        id="grant-divine-reservoir-header",
                        className="box-header",
                        children=[html.Div("Grant Divine Reservoir")],
                    ),
                    html.Div(
                        className="box-number",
                        id="box-34-header",
                        children=["34"],
                    ),
                    html.Div(
                        className="box-number",
                        id="box-35-header",
                        children=["35"],
                    ),
                    html.Div(
                        className="box-number",
                        id="box-36-header",
                        children=["36"],
                    ),
                    html.Div(
                        className="box-content",
                        id="box-34-container",
                        children=[
                            html.Div(className="box-content-title", children=["Storage Change"]),
                            html.Div(className="box-content-value", id="box-34-value", children=["-"]),
                            html.Div(className="box-content-subscript", children=[" "]),
                        ],
                    ),
                    html.Div(
                        className="box-content",
                        id="box-35-container",
                        children=[
                            html.Div(className="box-content-title", children=["Net Evaporation and Seepage"]),
                            html.Div(className="box-content-value", id="box-35-value", children=["-"]),
                            html.Div(className="box-content-subscript", children=[" "]),
                        ],
                    ),
                    html.Div(
                        className="box-content",
                        id="box-36-container",
                        children=[
                            html.Div(className="box-content-title", children=["Diversion"]),
                            html.Div(className="box-content-value", id="box-36-value", children=["-"]),
                            html.Div(className="box-content-subscript", children=["34+35"]),
                        ],
                    ),
                    # Boxes 37 - 38
                    html.Div(
                        className="box-number",
                        id="box-37-header",
                        children=["37"],
                    ),
                    html.Div(
                        className="box-number",
                        id="box-38-header",
                        children=["38"],
                    ),
                    html.Div(
                        className="box-content",
                        id="box-37-container",
                        children=[
                            html.Div(className="box-content-title", children=["Minor Project Diversions"]),
                            html.Div(className="box-content-value", id="box-37-value", children=["-"]),
                            html.Div(className="box-content-subscript", children=[" "]),
                        ],
                    ),
                    html.Div(
                        className="box-content",
                        id="box-38-container",
                        children=[
                            html.Div(className="box-content-title", children=["Total Diversion Moose Mountain Creek Basin"]),
                            html.Div(className="box-content-value", id="box-38-value", children=["-"]),
                            html.Div(className="box-content-subscript", children=["33+36+37"]),
                        ],
                    ),
                ],
            ),
        ],
    )
