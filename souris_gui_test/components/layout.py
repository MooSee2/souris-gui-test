from datetime import date
from datetime import datetime as dt

import dash_bootstrap_components as dbc
import data.constants as const
import modules.data_layer as dl
import data.test_data as td
from dash import dash_table, dcc, html
import dash_mantine_components as dmc

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

load_modal = dbc.Modal(
    [
        dbc.ModalHeader(dbc.ModalTitle("Load Application Data")),
        dbc.ModalBody(
            id="load-modal-body",
            children=[
                dbc.Button(id="query-data-button", children=["Query data from web"]),
                dbc.Button(id="load-from-csv-button", children=["From CSV"]),
                dcc.Loading(html.Div(id="loading-data-div", children=["Load data from either web or local sources."]),),
            ],
        ),
        dbc.ModalFooter(
        ),
    ],
    id="load-data-modal",
    is_open=False,
)

aside = html.Div(
    id="asideaside",
    children=[
        html.Div(
            className="config-card",
            children=[
                html.H4("Settings"),
                html.Div(
                    className="input-container",
                    children=[
                        html.Div(
                            className="header-info-container",
                            children=[
                                html.Div(
                                    className="HH6",
                                    children=["Water year"],
                                ),
                                html.Div(id="water-year-tip", className="info-container", children=html.Div(className="fa-solid fa-info")),
                            ],
                        ),
                        dbc.Tooltip(
                            "This is a bunch, " "of test text to explain what this field is for.",
                            target="water-year-tip",
                        ),
                        dcc.Dropdown(
                            id="apportionment-year",
                            options=const.available_years,
                            clearable=False,
                            value=const.current_year,
                        ),
                    ],
                ),
                html.Div(
                    className="input-container",
                    children=[
                        html.Div(
                            
                            className="header-info-container",
                            children=[
                                html.Div(
                                    className="HH6",
                                    children="Evaporation Start",
                                ),
                                html.Div(id="evap-start-tip", className="info-container", children=html.Div(className="fa-solid fa-info")),
                            ],
                        ),
                        dbc.Tooltip(
                            "This is a bunch, " "of test text to explain what this field is for.",
                            target="evap-start-tip",
                        ),
                        # style={"width": "100%"},
                        dcc.DatePickerSingle(id="evap-start-picker", className="evap-date-picker", date=date(const.current_year, 4, 15)),
                    ],
                ),
                html.Div(
                    className="input-container",
                    children=[
                        html.Div(
                            
                            className="header-info-container",
                            children=[
                                html.Div(className="HH6", children="Evaporation End"),
                                html.Div(id="evap-end-tip", className="info-container", children=html.Div(className="fa-solid fa-info")),
                            ],
                        ),
                        dbc.Tooltip(
                            "This is a bunch, " "of test text to explain what this field is for.",
                            target="evap-end-tip",
                        ),
                        dcc.DatePickerSingle(id="evap-end-picker", className="evap-date-picker", date=date(int(dt.now().year), 10, 15)),
                    ],
                ),
                html.Div(
                    className="input-container",
                    children=[
                        html.Div(
                            
                            className="header-info-container",
                            children=[
                                html.Div(className="HH6", children="Met Station"),
                                html.Div(id="met-station-tip", className="info-container", children=html.Div(className="fa-solid fa-info")),
                            ],
                        ),
                        dbc.Tooltip(
                            "This is a bunch, " "of test text to explain what this field is for.",
                            target="met-station-tip",
                        ),
                        dcc.Dropdown(
                            options=[
                                {"label": "Gildford", "value": "Gildford"},
                                {"label": "Eastern Crossing", "value": "MRatEC"},
                            ],
                            value="MRatEC",
                            clearable=False,
                        ),
                    ],
                ),
            ],
        ),
        html.Div(
            className="config-card",
            children=[dbc.Button("Load Data", color="secondary", id="load-data-button", n_clicks=0)],
        ),
        load_modal,
        html.Button(id="data-downloaded-signal", style={"display": "none"}),
        html.Div(
            className="config-card",
            children=[
                dbc.Button("Begin Apportionment", color="secondary", id="apportion-button", disabled=True),
            ],
        ),
    ],
)


main = html.Main(
    children=[
        dbc.Tabs(
            [
                dbc.Tab(
                    # id="tabtab",
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
                ),
                dbc.Tab(
                    # id="tabtab",
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
                                    td.reservoir_data.to_dict("records"),
                                    const.reservoir_station_names,
                                    style_cell={"textAlign": "center"},  # "whiteSpace": "normal", "overflow": "hidden", "textOverflow": "ellipsis"
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
                                    style_cell_conditional=[
                                        {"if": {"column_id": "datetime"}, "width": "10%"},
                                        {"if": {"column_id": "05NA006"}, "width": "10%"},
                                        {"if": {"column_id": "05NB020"}, "width": "10%"},
                                        {"if": {"column_id": "05NB016"}, "width": "10%"},
                                        {"if": {"column_id": "05NC002"}, "width": "10%"},
                                        {"if": {"column_id": "05ND012"}, "width": "10%"},
                                    ],
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
                    label="Graphs",
                    children=[
                        dbc.Card(
                            className="mt-3",
                            children=[
                                dbc.CardBody(
                                    children=[
                                        html.Div(
                                            [
                                                dmc.MultiSelect(
                                                    label="Select category",
                                                    placeholder="Select Station",
                                                    searchable=True,
                                                    data=dl.make_dropdown_options(const.stations),
                                                    id="timeseries-dropdown",
                                                ),
                                            ]
                                        ),
                                        # dbc.DropdownMenu(
                                        #     id="timeseries-dropdown",
                                        #     children=[
                                        #         dbc.DropdownMenuItem("Header", header=True),
                                        #         dbc.DropdownMenuItem("An item"),
                                        #         dbc.DropdownMenuItem(divider=True),
                                        #         dbc.DropdownMenuItem("Active and disabled", header=True),
                                        #         dbc.DropdownMenuItem("Active item", active=True),
                                        #         dbc.DropdownMenuItem("Disabled item", disabled=True),
                                        #         dbc.DropdownMenuItem(divider=True),
                                        #         html.P(
                                        #             "You can have other content here like text if you like.",
                                        #             className="text-muted px-4 mt-4",
                                        #         ),
                                        #     ],
                                        #     label="Stations",
                                        # ),
                                        dcc.Graph(id="timeseries-plot"),
                                    ]
                                ),
                            ],
                        ),
                    ],
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
