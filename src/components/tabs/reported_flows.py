import dash_bootstrap_components as dbc
from dash import html

#TODO add info icons to headings
reported_flows = dbc.Tab(
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
                                dbc.Input(id="pipeline-input", placeholder="Box 5b: DAM3", class_name="reported-flows-input", type="number"),
                            ],
                        ),
                        html.Div(
                            className="input-container",
                            children=[
                                html.H6("Long Creek Minor Project Diversion"),
                                dbc.Input(id="long-creek-minor-project-diversion-input", placeholder="Box 11: DAM3", class_name="reported-flows-input", type="number"),
                            ],
                        ),
                        html.Div(
                            className="input-container",
                            children=[
                                html.H6("US Diversion"),
                                dbc.Input(id="us-diversion-input", placeholder="Box 12: DAM3", class_name="reported-flows-input", type="number"),
                            ],
                        ),
                        html.Div(
                            className="input-container",
                            children=[
                                html.H6("City of Weyburn Pumpage"),
                                dbc.Input(id="weyburn-pumpage-input", placeholder="Box 16: DAM3", class_name="reported-flows-input", type="number"),
                            ],
                        ),
                        html.Div(
                            className="input-container",
                            children=[
                                html.H6("City of Weyburn Return Flow"),
                                dbc.Input(id="weyburn-return-flow-input", placeholder="Box 18: DAM3", class_name="reported-flows-input", type="number"),
                            ],
                        ),
                        html.Div(
                            className="input-container",
                            children=[
                                html.H6("Upper Souris Minor Project Diversion"),
                                dbc.Input(id="upper-souris-minor-diversion-input", placeholder="Box 25: DAM3", class_name="reported-flows-input", type="number"),
                            ],
                        ),
                        html.Div(
                            className="input-container",
                            children=[
                                html.H6("City of Estavan Net Pumpage"),
                                dbc.Input(id="estevan-net-pumpage-input", placeholder="Box 27: DAM3", class_name="reported-flows-input", type="number"),
                            ],
                        ),
                        html.Div(
                            className="input-container",
                            children=[
                                html.H6("Short Creek Diversions"),
                                dbc.Input(id="short-creek-diversions-input", placeholder="Box 28: DAM3", class_name="reported-flows-input", type="number"),
                            ],
                        ),
                        html.Div(
                            className="input-container",
                            children=[
                                html.H6("Lower Souris Minor Project Diversion"),
                                dbc.Input(id="lower-souris-minor-diversion-input", placeholder="Box 29: DAM3", class_name="reported-flows-input", type="number"),
                            ],
                        ),
                        html.Div(
                            className="input-container",
                            children=[
                                html.H6("Moose Mountain Minor Project Diversion"),
                                dbc.Input(id="moose-mountain-minor-diversion-input", placeholder="Box 37: DAM3", class_name="reported-flows-input", type="number"),
                            ],
                        ),
                    ],
                ),
            ],
        ),
    ),
)
