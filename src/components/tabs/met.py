import dash_bootstrap_components as dbc
from dash import dash_table
import src.app_data.stations as const

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


def met_data():
    return dbc.Tab(
        label="Met Data",
        children=dbc.Card(
            className="mt-3",
            children=dbc.CardBody(
                [
                    dash_table.DataTable(
                        id="met-data",
                        columns=const.met_station_names,
                        style_table={"minWidth": "100%", "overflowY": "auto"},
                        style_header={
                            "textAlign": "center",
                            "whiteSpace": "normal",
                            "overflow": "hidden",
                            "textOverflow": "ellipsis",
                        },
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
                        merge_duplicate_headers=True,
                        editable=True,
                        style_cell_conditional=[{"if": {"column_id": station}, "width": "5%"} for station in stations],
                    ),
                ]
            ),
        ),
    )
