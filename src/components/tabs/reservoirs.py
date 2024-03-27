import dash_bootstrap_components as dbc
from dash import dash_table
import app_data.stations as const
import app_data.test_data as td
import pandas as pd

stations = [
    "datetime",
    "05NA006",
    "05NB020",
    "05NB016",
    "05NC002",
    "05ND012",
]

dummy_data = pd.DataFrame(
    {
        "datetime": "2000-01-01",
        "05NA006": [9999],
        "05NB020": [9999],
        "05NB016": [9999],
        "05NC002": [9999],
        "05ND012": [9999],
    },
)

reservoirs = dbc.Tab(
    label="Reservoir Data",
    children=dbc.Card(
        className="mt-3",
        children=dbc.CardBody(
            [
                dash_table.DataTable(
                    id="reservoir-data",
                    data=dummy_data.to_dict("records"),
                    columns=const.reservoir_station_names,
                    style_table={'overflowY': 'auto'},
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
                    # fixed_rows={"headers": True},
                    style_cell_conditional=[
                        {"if": {"column_id": station}, "width": "10%"} for station in stations
                    #     # {"if": {"column_id": "05NA006"}, "width": "10%"},
                    #     # {"if": {"column_id": "05NB020"}, "width": "10%"},
                    #     # {"if": {"column_id": "05NB016"}, "width": "10%"},
                    #     # {"if": {"column_id": "05NC002"}, "width": "10%"},
                    #     # {"if": {"column_id": "05ND012"}, "width": "10%"},
                    ],
                ),
            ]
        ),
    ),
)
