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

now = dt.now().year
datetime = pd.date_range(f"{now}-01-01", f"{now}-12-31", freq="d").strftime("%Y-%m-%d")
dummy_data = pd.DataFrame({"datetime": datetime})

columns = const.reservoir_station_names
hidden_columns = [f"{station}_approval" for station in stations]
datetime_conditional = [
    {
        "if": {
            "column_id": "datetime",
        },
        "backgroundColor": "#fafafa",
        "verticalAlign": "middle",
    },
]
conditionals = utils.make_reservoir_approved_conditionals(stations=stations) + utils.make_reservoir_unapproved_conditionals(stations=stations) + datetime_conditional


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
                        hidden_columns=hidden_columns,
                        page_size=367,
                        style_table={
                            "overflowY": "auto",
                        },
                        style_data={
                            "whiteSpace": "normal",
                            "height": "auto",
                        },
                        style_data_conditional=conditionals,
                        style_cell={
                            "textAlign": "center",
                            "whiteSpace": "normal",
                            "overflow": "hidden",
                            "textOverflow": "ellipsis",
                        },
                        style_cell_conditional=[{"if": {"column_id": station}, "width": "5%"} for station in stations],
                        merge_duplicate_headers=True,
                        editable=True,
                    ),
                ]
            ),
        ),
    )
