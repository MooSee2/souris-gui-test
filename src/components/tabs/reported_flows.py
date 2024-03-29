import dash_bootstrap_components as dbc
from dash import html

# Add new reported flows here.
reported_flows = [
    (
        "Boundary Reservoir Pipeline",
        "pipeline-input",
        "Box 5b: DAM3",
        "box5b-tip",
        "",
    ),
    (
        "Long Creek Minor Project Diversion",
        "long-creek-minor-project-diversion-input",
        "Box 11: DAM3",
        "box11-tip",
        "",
    ),
    (
        "US Diversion",
        "us-diversion-input",
        "Box 12: DAM3",
        "box12-tip",
        "",
    ),
    (
        "City of Weyburn Pumpage",
        "weyburn-pumpage-input",
        "Box 16: DAM3",
        "box16-tip",
        "",
    ),
    (
        "City of Weyburn Return Flow",
        "weyburn-return-flow-input",
        "Box 18: DAM3",
        "box18-tip",
        "",
    ),
    (
        "Upper Souris Minor Project Diversion",
        "upper-souris-minor-diversion-input",
        "Box 25: DAM3",
        "box25-tip",
        "",
    ),
    (
        "City of Estavan Net Pumpage",
        "estevan-net-pumpage-input",
        "Box 27: DAM3",
        "box27-tip",
        "",
    ),
    (
        "Short Creek Diversions",
        "short-creek-diversions-input",
        "Box 28: DAM3",
        "box28-tip",
        "",
    ),
    (
        "Lower Souris Minor Project Diversion",
        "lower-souris-minor-diversion-input",
        "Box 29: DAM3",
        "box29-tip",
        "",
    ),
    (
        "Moose Mountain Minor Project Diversion",
        "moose-mountain-minor-diversion-input",
        "Box 37: DAM3",
        "box37-tip",
        "",
    ),
]

# This builds all the reported flows inputs and containers.
reported_flows_container = [
    html.Div(
        className="input-container",
        children=[
            html.Div(
                className="reported-flows-info-container",
                children=[
                    html.H6(box_name),
                    html.Div(
                        id=tip_name,
                        className="info-container",
                        children=html.Div(className="fa-solid fa-info"),
                    ),
                ],
            ),
            dbc.Tooltip(
                tip_text,
                target=tip_name,
            ),
            dbc.Input(
                id=container_id,
                class_name="reported-flows-input",
                placeholder=box_label,
                type="number",
            ),
        ],
    )
    for box_name, container_id, box_label, tip_name, tip_text, in reported_flows
]

# children = []


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
                        children=reported_flows_container,
                    ),
                ],
            ),
        ),
    )
