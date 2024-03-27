import dash_bootstrap_components as dbc
from dash import dash_table
import app_data.stations as const
import app_data.test_data as td
import pandas as pd

stations = ["datetime" "1234_wind_speed" "1234_air_temp" "1234_sol_rad" "1234_rel_humidity" "1234_precip" "4321_wind_speed" "4321_air_temp" "4321_sol_rad" "4321_rel_humidity" "4321_precip"]

dummy_data = pd.DataFrame(
    {
        "datetime": "2000-01-01",
        "1234_wind_speed": [9999],
        "1234_air_temp": [9999],
        "1234_sol_rad": [9999],
        "1234_rel_humidity": [9999],
        "1234_precip": [9999],
        "4321_wind_speed": [9999],
        "4321_air_temp": [9999],
        "4321_sol_rad": [9999],
        "4321_rel_humidity": [9999],
        "4321_precip": [9999],
    },
)

met_data = dbc.Tab(
    label="Met Data",
    children=dbc.Card(
        className="mt-3",
        children=dbc.CardBody(
            [
                dash_table.DataTable(
                    data=dummy_data.to_dict("records"),
                    id="met-data",
                    columns=const.met_station_names,
                    style_table={"minWidth": "100%", 'overflowY': 'auto'},
                    style_header={
                        "textAlign": "center",
                        "whiteSpace": "normal",
                        "overflow": "hidden",
                        "textOverflow": "ellipsis",
                    },
                    style_data={
                        #     "whiteSpace": "normal",
                        "height": "auto",
                    },
                    merge_duplicate_headers=True,
                    editable=True,
                    # fixed_rows={"headers": True},
                    # style_cell_conditional=[
                    #     {"if": {"column_id": "datetime"}, "width": "10%"},
                    # ],
                    style_cell_conditional=[
                        {"if": {"column_id": station}, "width": "5%"}
                        for station in stations
                    ],
                ),
            ]
        ),
    ),
)
