import dash_bootstrap_components as dbc
from dash import dash_table

import app_data.stations as const
import modules.utils as utils

stations = {
    "05NA006",
    "05NB020",
    "05NB016",
    "05NC002",
    "05ND012",
}

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


def reservoirs():
    return dbc.Tab(
        label="Reservoir Data",
        children=dbc.Card(
            className="mt-3",
            children=dbc.CardBody(
                [
                    dash_table.DataTable(
                        id="reservoir-data",
                        columns=columns,
                        style_table={"overflowY": "auto"},
                        style_cell={"textAlign": "center", "verticalAlign": "middle"},
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
                        style_data_conditional=conditionals,
                        hidden_columns=hidden_columns,
                        # fixed_rows={"headers": True},
                        # style_cell_conditional=[{"if": {"column_id": station}, "width": "10%"} for station in stations],
                    ),
                ]
            ),
        ),
    )
