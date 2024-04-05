from datetime import datetime as dt

import dash_bootstrap_components as dbc
import pandas as pd
from dash import dash_table

import app_data.stations as const
import modules.utils as utils

stations = [
    "datetime",
    "05NB001",
    "05NB036",
    "05NB011",
    "05NB018",
    "05NA003",
    "05NB040",
    "05NB041",
    "05NB038",
    "05NB014",
    "05NB035",
    "05NB033",
    "05NB039",
]

columns = const.reservoir_station_names
# hidden_columns = [f"{station}_approval" for station in stations]

datetime_conditional = [
    {
        "if": {
            "column_id": "datetime",
        },
        "backgroundColor": "#fafafa",
        "verticalAlign": "middle",
    },
]

# conditionals = utils.make_approved_conditionals(stations=stations) + utils.make_unapproved_conditionals(stations=stations) + datetime_conditional
conditionals = utils.make_conditionals(stations=stations)

def discharge():
    return dbc.Tab(
        label="Discharge data",
        children=dbc.Card(
            className="mt-3",
            children=dbc.CardBody(
                children=[
                    dash_table.DataTable(
                        id="discharge-data",
                        columns=const.discharge_station_names,
                        editable=True,
                        merge_duplicate_headers=True,
                        page_action="none",
                        # hidden_columns=hidden_columns,
                        style_table={
                            "overflowY": "auto",
                        },
                        style_data={
                            'whiteSpace': 'normal',
                            'height': 'auto',
                            'lineHeight': '15px'
                        },
                        style_data_conditional=conditionals,
                        style_cell={
                            "textAlign": "center",
                            "whiteSpace": "normal",
                            "overflow": "hidden",
                            "textOverflow": "ellipsis",
                        },
                        style_cell_conditional=[{"if": {"column_id": station}, "width": "5%"} for station in stations],
                    ),
                ]
            ),
        ),
    )
