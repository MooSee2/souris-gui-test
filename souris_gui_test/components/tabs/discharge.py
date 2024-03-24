import dash_bootstrap_components as dbc
from dash import dash_table, html
import data.constants as const
import data.test_data as td

discharge = dbc.Tab(
    label="Discharge data",
    children=dbc.Card(
        className="mt-3",
        children=dbc.CardBody(
            [
                dash_table.DataTable(
                    td.discharge_data.to_dict("records"),
                    const.discharge_station_names,
                    style_table={"minWidth": "100%"},
                    style_cell={"textAlign": "center", "whiteSpace": "normal", "overflow": "hidden", "textOverflow": "ellipsis"},
                    style_data={
                        "whiteSpace": "normal",
                        "height": "auto",
                    },
                    merge_duplicate_headers=True,
                    editable=True,
                    fixed_rows={"headers": True},
                ),
                html.Div(
                    id="output-data-upload",
                    children=[],
                ),
                html.Div(
                    id="output-inputs",
                    children=["100"],
                ),
            ]
        ),
    ),
)
