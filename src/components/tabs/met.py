import dash_bootstrap_components as dbc
from dash import dash_table, dcc

import app_data.stations as const
import modules.utils.make_conditionals as make_conditionals

stations = [
    "datetime",
    "1234_wind_speed",
    "1234_air_temp",
    "1234_sol_rad",
    "1234_rel_humidity",
    "1234_precip",
    "4321_wind_speed",
    "4321_air_temp",
    "4321_sol_rad",
    "4321_rel_humidity",
    "4321_precip",
]


columns = const.reservoir_station_names
# hidden_columns = [f"{station}_approval" for station in stations]

datetime_conditional = [
    {
        "if": {
            "column_id": "date",
        },
        "backgroundColor": "#fafafa",
        "verticalAlign": "middle",
    },
]

# conditionals = utils.make_approved_conditionals(stations=stations) + utils.make_unapproved_conditionals(stations=stations) + datetime_conditional
conditionals = make_conditionals.make_conditionals(stations=stations) + datetime_conditional


def met_data():
    return dbc.Tab(
        label="Met Data",
        children=dbc.Card(
            className="mt-3",
            children=dbc.CardBody(
                [
                    dcc.Loading(
                        dbc.Button(id="load-2023-met-btn", children=["Load 2023 Data"]),
                    ),
                    dash_table.DataTable(
                        id="met-data",
                        columns=const.met_station_names,
                        editable=True,
                        merge_duplicate_headers=True,
                        page_action="none",
                        style_data_conditional=conditionals,
                        style_table={
                            "overflowY": "auto",
                        },
                        style_data={
                            "whiteSpace": "normal",
                            "height": "auto",
                            "lineHeight": "10px",
                        },
                        style_cell={
                            "textAlign": "center",
                            "whiteSpace": "normal",
                            "overflow": "hidden",
                            "textOverflow": "ellipsis",
                        },
                        style_cell_conditional=[
                            {"if": {"column_id": "date"}, "width": "200px"},
                        ],
                    ),
                ],
            ),
        ),
    )
