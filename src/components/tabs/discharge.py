import dash_bootstrap_components as dbc
from dash import dash_table, html
import app_data.stations as const
import pandas as pd
from app_data import test_data as td

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

dummy_data = pd.DataFrame(
    {
        "datetime": "2000-01-01",
        "05NB001": [9999],
        "05NB036": [9999],
        "05NB011": [9999],
        "05NB018": [9999],
        "05NA003": [9999],
        "05NB040": [9999],
        "05NB041": [9999],
        "05NB038": [9999],
        "05NB014": [9999],
        "05NB035": [9999],
        "05NB033": [9999],
        "05NB039": [9999],
    },
)

discharge = dbc.Tab(
    label="Discharge data",
    children=dbc.Card(
        className="mt-3",
        children=dbc.CardBody(
            children=[
                dash_table.DataTable(
                    # data=dummy_data.to_dict("records"),
                    columns=const.discharge_station_names,
                    id="discharge-data",
                    # style_table={"minWidth": "100%"},
                    style_cell={
                        "textAlign": "center",
                        "whiteSpace": "normal",
                        "overflow": "hidden",
                        "textOverflow": "ellipsis",
                    },
                    style_data={
                        "whiteSpace": "normal",
                        "height": "auto",
                    },
                    style_table={'overflowY': 'auto'},
                    merge_duplicate_headers=True,
                    editable=True,
                    # fixed_rows={"headers": True},
                    style_cell_conditional=[
                        {"if": {"column_id": station}, "width": "5%"}
                        for station in stations
                    ],
                ),
            ]
        ),
    ),
)
