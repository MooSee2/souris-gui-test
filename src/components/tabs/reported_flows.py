import dash_bootstrap_components as dbc
from dash import html

# Add new reported flows here.
reported_flows = [
    (
        "Boundary Reservoir Pipeline",
        "pipeline-input",
        "Box 5b:  DAM3,   Provider:  USGS, ND WSC.",
        "box5b-tip",
        "This value is obtained from the USGS, Dakota Water Science Center, Bismarck Program Office",
    ),
    (
        "Long Creek Minor Project Diversion",
        "long-creek-minor-project-diversion-input",
        "Box 11:  DAM3,   Provider:  WSA",
        "box11-tip",
        "This value is obtained from the WSA.",
    ),
    (
        "US Diversion",
        "us-diversion-input",
        "Box 12: DAM3,   Provider:  USGS",
        "box12-tip",
        "This value is obtained from the USGS.",
    ),
    (
        "City of Weyburn Pumpage",
        "weyburn-pumpage-input",
        "Box 16: DAM3,   Provider:  Weyburn WTP",
        "box16-tip",
        "This value is obtained from staff of the Weyburn Water Treatment Plant.",
    ),
    (
        "City of Weyburn Return Flow",
        "weyburn-return-flow-input",
        "Box 18: DAM3,   Provider:  Weyburn Engineering Dept.",
        "box18-tip",
        "This value is obtained from staff of the City of Weyburn Engineering Department.",
    ),
    (
        "Upper Souris Minor Project Diversion",
        "upper-souris-minor-diversion-input",
        "Box 25: DAM3,   Provider:  WSA",
        "box25-tip",
        "This value is obtained from the WSA.",
    ),
    (
        "City of Estavan Net Pumpage",
        "estevan-net-pumpage-input",
        "Box 27: DAM3,   Provider:  Estevan WTP",
        "box27-tip",
        "This value is obtained from staff of the City of Estevan Water Treatment Plant.",
    ),
    (
        "Short Creek Diversions",
        "short-creek-diversions-input",
        "Box 28: DAM3,   Provider:  USGS",
        "box28-tip",
        "This value is obtained from the USGS.",
    ),
    (
        "Lower Souris Minor Project Diversion",
        "lower-souris-minor-diversion-input",
        "Box 29: DAM3,   Provider:  WSA",
        "box29-tip",
        "This value is obtained from the WSA.",
    ),
    (
        "Moose Mountain Minor Project Diversion",
        "moose-mountain-minor-diversion-input",
        "Box 37: DAM3,   Provider:  WSA",
        "box37-tip",
        "This value is obtained from the WSA.",
    ),
]

# This is a big list comprehension that builds all the reported flows inputs and containers.
# To add a new reported flow source, modify the reported_flows dictionary.
reported_flows_container = [
    html.Div(
        className="input-container",
        children=[
            html.Div(
                className="reported-flows-info-container",
                children=[
                    html.H6(box_name),
                    # html.Div(
                    #     # id=tip_name,
                    #     className="info-container",
                    #     children=html.Div(className="fa-solid fa-info"),
                    # ),
                ],
            ),
            # dbc.Tooltip(
            #     tip_text,
            #     target=tip_name,
            # ),
            dbc.Input(
                id=container_id,
                class_name="reported-flows-input",
                placeholder=box_label,
                type="number",
            ),
        ],
    )
    for box_name, container_id, box_label, *_ in reported_flows
]


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
