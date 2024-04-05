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
                        editable=True,
                        merge_duplicate_headers=True,
                        page_action="none",
                        sort_action="native",
                        style_data_conditional=conditionals,
                        style_table={
                            "overflowY": "auto",
                        },
                        style_data={"whiteSpace": "normal", "height": "auto", "lineHeight": "15px", "padding": "5px"},
                        style_cell={
                            "textAlign": "center",
                            "whiteSpace": "normal",
                            "overflow": "hidden",
                            "textOverflow": "ellipsis",
                        },
                        style_cell_conditional=[{"if": {"column_id": station}, "width": "10%"} for station in stations],
                        # css=[
                        #     {
                        #         "selector": ".dash-spreadsheet td div",
                        #         "rule": """
                        #                     line-height: 15px;
                        #                     max-height: 30px; min-height: 30px; height: 30px;
                        #                     display: block;
                        #                     overflow-y: hidden;
                        #                 """,
                        #     }
                        # ],
                        # hidden_columns=hidden_columns,
                        # fixed_rows={"headers": True},
                    ),
                ]
            ),
        ),
    )
