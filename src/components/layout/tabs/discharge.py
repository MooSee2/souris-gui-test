import dash_bootstrap_components as dbc
from dash import dash_table

import app_data.stations as const
import modules.utils.make_conditionals as make_conditionals

stations = [
    # "datetime",
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

columns = const.reservoir_station_names

# conditionals = utils.make_approved_conditionals(stations=stations) + utils.make_unapproved_conditionals(stations=stations) + datetime_conditional
conditionals = make_conditionals.make_conditionals(stations=stations)  # + datetime_conditional
# station = "05113600_approval"


def make_discharge_tab():
    return dbc.Tab(
        label="Discharge data",
        children=dbc.Card(
            className="mt-3",
            children=dbc.CardBody(
                children=[
                    dash_table.DataTable(
                        id="discharge-data",
                        columns=const.discharge_station_names,
                        editable=True,
                        merge_duplicate_headers=True,
                        page_action="none",
                        style_data_conditional=conditionals,
                        # [
                        #     {
                        #         "if": {
                        #             "filter_query": f"{{{station}}} = 'Approved'",
                        #             "column_id": "05113600_approval",
                        #         },
                        #         "backgroundColor": "#D1E5F0",
                        #         "color": "black",
                        #     },
                        # ],
                        style_table={
                            "overflowY": "auto",
                        },
                        style_data={
                            "whiteSpace": "normal",
                            "height": "auto",
                            "lineHeight": "15px",
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
                        # style_cell_conditional=[{"if": {"column_id": station}, "width": "120px"} for station in stations],
                    ),
                ]
            ),
        ),
    )
