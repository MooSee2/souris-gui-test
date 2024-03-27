import dash_bootstrap_components as dbc
from dash import html


reported_flows = [
    (
        "Boundary Reservoir Pipeline",
        "pipeline-input",
        "Box 5b: DAM3",
    ),
    (
        "Long Creek Minor Project Diversion",
        "long-creek-minor-project-diversion-input",
        "Box 11: DAM3",
    ),
    (
        "US Diversion",
        "us-diversion-input",
        "Box 12: DAM3",
    ),
    (
        "City of Weyburn Pumpage",
        "weyburn-pumpage-input",
        "Box 16: DAM3",
    ),
    (
        "City of Weyburn Return Flow",
        "weyburn-return-flow-input",
        "Box 18: DAM3",
    ),
    (
        "Upper Souris Minor Project Diversion",
        "upper-souris-minor-diversion-input",
        "Box 25: DAM3",
    ),
    (
        "City of Estavan Net Pumpage",
        "estevan-net-pumpage-input",
        "Box 27: DAM3",
    ),
    (
        "Short Creek Diversions",
        "short-creek-diversions-input",
        "Box 28: DAM3",
    ),
    (
        "Lower Souris Minor Project Diversion",
        "lower-souris-minor-diversion-input",
        "Box 29: DAM3",
    ),
    (
        "Moose Mountain Minor Project Diversion",
        "moose-mountain-minor-diversion-input",
        "Box 37: DAM3",
    ),
]


# TODO add info icons to headings
def reported_flows():
    return dbc.Tab(
        label="Reported Flows",
        children=dbc.Card(
            className="mt-3",
            children=dbc.CardBody(
                [
                    html.Div(
                        className="config-card",
                        children=[
                            html.Div(
                                className="input-container",
                                children=[
                                    html.H6("Boundary Reservoir Pipeline"),
                                    dbc.Input(
                                        id="pipeline-input",
                                        class_name="reported-flows-input",
                                        placeholder="Box 5b: DAM3",
                                        type="number",
                                    ),
                                ],
                            ),
                            html.Div(
                                className="input-container",
                                children=[
                                    html.H6("Long Creek Minor Project Diversion"),
                                    dbc.Input(
                                        id="long-creek-minor-project-diversion-input",
                                        class_name="reported-flows-input",
                                        placeholder="Box 11: DAM3",
                                        type="number",
                                    ),
                                ],
                            ),
                            html.Div(
                                className="input-container",
                                children=[
                                    html.H6("US Diversion"),
                                    dbc.Input(
                                        id="us-diversion-input",
                                        class_name="reported-flows-input",
                                        placeholder="Box 12: DAM3",
                                        type="number",
                                    ),
                                ],
                            ),
                            html.Div(
                                className="input-container",
                                children=[
                                    html.H6("City of Weyburn Pumpage"),
                                    dbc.Input(
                                        id="weyburn-pumpage-input",
                                        class_name="reported-flows-input",
                                        placeholder="Box 16: DAM3",
                                        type="number",
                                    ),
                                ],
                            ),
                            html.Div(
                                className="input-container",
                                children=[
                                    html.H6("City of Weyburn Return Flow"),
                                    dbc.Input(
                                        id="weyburn-return-flow-input",
                                        placeholder="Box 18: DAM3",
                                        class_name="reported-flows-input",
                                        type="number",
                                    ),
                                ],
                            ),
                            html.Div(
                                className="input-container",
                                children=[
                                    html.H6("Upper Souris Minor Project Diversion"),
                                    dbc.Input(
                                        id="upper-souris-minor-diversion-input",
                                        class_name="reported-flows-input",
                                        placeholder="Box 25: DAM3",
                                        type="number",
                                    ),
                                ],
                            ),
                            html.Div(
                                className="input-container",
                                children=[
                                    html.H6("City of Estavan Net Pumpage"),
                                    dbc.Input(
                                        id="estevan-net-pumpage-input",
                                        class_name="reported-flows-input",
                                        placeholder="Box 27: DAM3",
                                        type="number",
                                    ),
                                ],
                            ),
                            html.Div(
                                className="input-container",
                                children=[
                                    html.H6("Short Creek Diversions"),
                                    dbc.Input(
                                        id="short-creek-diversions-input",
                                        class_name="reported-flows-input",
                                        placeholder="Box 28: DAM3",
                                        type="number",
                                    ),
                                ],
                            ),
                            html.Div(
                                className="input-container",
                                children=[
                                    html.H6("Lower Souris Minor Project Diversion"),
                                    dbc.Input(
                                        id="lower-souris-minor-diversion-input",
                                        class_name="reported-flows-input",
                                        placeholder="Box 29: DAM3",
                                        type="number",
                                    ),
                                ],
                            ),
                            html.Div(
                                className="input-container",
                                children=[
                                    html.H6("Moose Mountain Minor Project Diversion"),
                                    dbc.Input(
                                        id="moose-mountain-minor-diversion-input",
                                        class_name="reported-flows-input",
                                        placeholder="Box 37: DAM3",
                                        type="number",
                                    ),
                                ],
                            ),
                        ],
                    ),
                ],
            ),
        ),
    )
