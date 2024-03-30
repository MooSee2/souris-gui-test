import dash_bootstrap_components as dbc
from dash import dash_table
import app_data.stations as const
import app_data.test_data as td
import pandas as pd


stations = {
    "05NA006",
    "05NB020",
    "05NB016",
    "05NC002",
    "05ND012",
}

hidden_columns = [f"{station}_approval" for station in stations]


def make_reservoir_approved_conditionals(stations=None):
    if stations is None:
        stations = {
            "05NA006",
            "05NB020",
            "05NB016",
            "05NC002",
            "05ND012",
        }
    return [
        {
            "if": {
                "filter_query": f'{{{station}_approved}} eq "approved"',
                "column_id": f"{station}",
            },
            "backgroundColor": "#008000",
            "color": "white",
        }
        for station in stations
    ]


def make_reservoir_unapproved_conditionals(stations=None):
    if stations is None:
        stations = {
            "05NA006",
            "05NB020",
            "05NB016",
            "05NC002",
            "05ND012",
        }
    return [
        {
            "if": {
                "filter_query": f'{{{station}_approved}} eq "unapproved"',
                "column_id": f"{station}",
            },
            "backgroundColor": "#008000",
            "color": "white",
        }
        for station in stations
    ]


def _combine_approval_conditionals(stations) -> list:
    approved_conds = make_reservoir_approved_conditionals(stations=stations)
    unapproved_conds = make_reservoir_unapproved_conditionals(stations=stations)
    approved_conds.append(unapproved_conds)
    return None


def reservoirs():
    return dbc.Tab(
        label="Reservoir Data",
        children=dbc.Card(
            className="mt-3",
            children=dbc.CardBody(
                [
                    dash_table.DataTable(
                        id="reservoir-data",
                        columns=const.reservoir_station_names,
                        # fill_width = False,
                        style_table={"overflowY": "auto"},
                        style_cell={"textAlign": "center"},
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
                        style_data_conditional=_combine_approval_conditionals(stations=stations),
                        hidden_columns=hidden_columns,
                        # fixed_rows={"headers": True},
                        # style_cell_conditional=[{"if": {"column_id": station}, "width": "10%"} for station in stations],
                    ),
                ]
            ),
        ),
    )
