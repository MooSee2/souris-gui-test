from datetime import date
from datetime import datetime as dt

import data.test_data as td
import dash_bootstrap_components as dbc
import data.constants as const
from dash import dash_table, dcc, html

navbar = dbc.NavbarSimple(
    id="navbar",
    children=[
        dbc.NavItem(dbc.NavLink("Page 1", href="#")),
    ],
    brand="IJC",
    brand_href="#",
    color="primary",
    dark=True,
)


aside = html.Aside(
    children=[
        html.Div(
            className="config-card",
            children=[
                html.H4("Settings"),
                html.Br(),
                html.Div(
                    className="input-container",
                    children=[
                        html.H6("Water year"),
                        dbc.Input(id="water-year-input", placeholder="Example: 2024", class_name="reported-flows-input", type="number", step=1, min=2023, max=2099),
                    ],
                ),
                html.Br(),
                html.Div(
                    className="input-container",
                    children=[
                        html.H6("Met Station"),
                        dcc.Dropdown(
                            options=[
                                {"label": "Gildford", "value": "Gildford"},
                                {"label": "Eastern Crossing", "value": "MRatEC"},
                            ],
                            value="MRatEC",
                            clearable=False,
                            # optionHeight=20,
                        ),
                    ],
                ),
                html.Br(),
                html.Div(
                    className="input-container",
                    children=[
                        html.H6("Evaporation Start"),
                        dcc.DatePickerSingle(id="evap-start-picker", className="evap-datepicker", date=date(int(dt.now().year), 4, 15)),
                    ],
                ),
                html.Div(
                    className="input-container",
                    children=[
                        html.H6("Evaporation End"),
                        dcc.DatePickerSingle(id="evap-end-picker", className="evap-datepicker", date=date(int(dt.now().year), 10, 15)),
                    ],
                ),
            ],
        ),
        html.Br(),
        html.Div(
            className="reported-flows-card",
            children=[
                html.H4("Reported flows"),
                html.Br(),
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
        html.Br(),
        html.Div(
            className="calculate-card",
            children=[dbc.Button("Begin Apportionment", color="secondary", id="apportion-button")],
        ),
    ],
)


main = html.Main(
    children=[
        dbc.Tabs(
            [
                dbc.Tab(
                    id="tabtab",
                    label="Discharge data",
                    children=dbc.Card(
                        className="mt-3",
                        children=dbc.CardBody(
                            [
                                # dcc.Upload(
                                #     id="upload-data",
                                #     children=html.Div(
                                #         [
                                #             "Drag and Drop or ",
                                #             html.A("Select Files"),
                                #         ],
                                #     ),
                                # ),
                                dash_table.DataTable(
                                    td.discharge_data.to_dict("records"),
                                    const.discharge_station_names,
                                    style_table={"minWidth": "100%"},
                                    style_cell={"textAlign": "center", "whiteSpace": "normal", "overflow": "hidden", "textOverflow": "ellipsis"},
                                    style_data={
                                        "whiteSpace": "normal",
                                        "height": "auto",
                                    },
                                    merge_duplicate_headers=True,
                                    editable=True,
                                    fixed_rows={"headers": True},
                                ),
                                html.Div(
                                    id="output-data-upload",
                                    children=[],
                                ),
                                html.Div(
                                    id="output-inputs",
                                    children=["100"],
                                ),
                            ]
                        ),
                    ),
                ),
                dbc.Tab(
                    label="Reservoir Data",
                    children=dbc.Card(
                        className="mt-3",
                        children=dbc.CardBody(
                            [
                                dash_table.DataTable(
                                    td.reservoir_data.to_dict("records", index=True),
                                    const.reservoir_station_names,
                                    # style_table={"minWidth": "100%"},
                                    # style_cell={"textAlign": "center", "whiteSpace": "normal", "overflow": "hidden", "textOverflow": "ellipsis"},
                                    # style_cell={
                                    #     "whiteSpace": "normal",
                                    #     "height": "auto",
                                    # },
                                    style_data={
                                        "whiteSpace": "normal",
                                    },
                                    css=[
                                        {
                                            "selector": ".dash-spreadsheet td div",
                                            "rule": """
                                            line-height: 15px;
                                            max-height: 30px; min-height: 30px; height: 30px;
                                            display: block;
                                            overflow-y: hidden;
                                        """,
                                        }
                                    ],
                                    merge_duplicate_headers=True,
                                    editable=True,
                                    fixed_rows={"headers": True},
                                    style_table={"height": "100%", "maxHeight": "100%"},
                                ),
                            ]
                        ),
                    ),
                ),
                dbc.Tab(
                    label="Met Data",
                    children=dbc.Card(
                        className="mt-3",
                        children=dbc.CardBody(
                            [
                                dash_table.DataTable(
                                    td.met_data.to_dict("records", index=True),
                                    const.met_station_names,
                                    style_table={"minWidth": "100%"},
                                    style_header={
                                        "textAlign": "center",
                                        "whiteSpace": "normal",
                                        "overflow": "hidden",
                                        "textOverflow": "ellipsis",
                                    },
                                    # style_data={
                                    #     "whiteSpace": "normal",
                                    #     "height": "auto",
                                    # },
                                    merge_duplicate_headers=True,
                                    editable=True,
                                    fixed_rows={"headers": True},
                                ),
                            ]
                        ),
                    ),
                ),
                dbc.Tab(
                    label="Report",
                    children=dbc.Card(
                        className="mt-3",
                        children=dbc.CardBody(
                            [
                                html.P("This is tab 2!", className="card-text"),
                                html.Div(className="tab2-thing"),
                                html.Div(className="tab2-thing"),
                                html.Div(className="tab2-thing"),
                                html.Div(className="tab2-thing"),
                                html.Div(className="tab2-thing"),
                                html.Div(className="tab2-thing"),
                                html.Div(className="tab2-thing"),
                                html.Div(className="tab2-thing"),
                                html.Div(className="tab2-thing"),
                            ]
                        ),
                    ),
                ),
                dbc.Tab(
                    label="Calculated",
                    children=html.P("Meow!"),
                ),
            ],
        ),
    ],
)


def make_layout():
    return [
        navbar,
        html.Div(
            id="interior-container",
            children=[
                aside,
                main,
            ],
        ),
    ]
