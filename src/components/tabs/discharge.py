import dash_bootstrap_components as dbc
from dash import dash_table
import pandas as pd
from datetime import datetime as dt

import src.app_data.stations as const

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


def make_discharge_conditionals(stations):
    return [
        {
            "if": {
                "filter_query": '{station_approval} eq "approved"',
                "column_id": "Humidity",
            },
            "backgroundColor": "#008000",
            "color": "white",
        }
    ]


# discharge_conditionals = [
#     {
#         "if": {
#             "filter_query": '{Humidity_approval} eq "approved"',
#             "column_id": "Humidity",
#         },
#         "backgroundColor": "#008000",
#         "color": "white",
#     },
#     {
#         "if": {
#             "filter_query": '{Humidity_approval} eq "unapproved"',
#             "column_id": "Humidity",
#         },
#         "backgroundColor": "#FF1515",
#         "color": "white",
#     },
# ]


def discharge():
    return dbc.Tab(
        label="Discharge data",
        children=dbc.Card(
            className="mt-3",
            children=dbc.CardBody(
                children=[
                    dash_table.DataTable(
                        data=dummy_data.to_dict("records"),
                        columns=const.discharge_station_names,
                        id="discharge-data",
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
                        style_table={"overflowY": "auto"},
                        # style_data_conditional=[
                        #     [
                        #         {
                        #             "if": {
                        #                 "filter_query": '{Humidity_approval} eq "approved"',
                        #                 "column_id": "Humidity",
                        #             },
                        #             "backgroundColor": "#008000",
                        #             "color": "white",
                        #         },
                        #         {
                        #             "if": {
                        #                 "filter_query": '{Humidity_approval} eq "unapproved"',
                        #                 "column_id": "Humidity",
                        #             },
                        #             "backgroundColor": "#FF1515",
                        #             "color": "white",
                        #         },
                        #     ]
                        # ],
                        merge_duplicate_headers=True,
                        editable=True,
                        # fixed_rows={"headers": True},
                        style_cell_conditional=[{"if": {"column_id": station}, "width": "5%"} for station in stations],
                    ),
                ]
            ),
        ),
    )
