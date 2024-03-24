import dash_bootstrap_components as dbc
from dash import dash_table
import data.constants as const
import data.test_data as td

reservoirs = dbc.Tab(
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
)
