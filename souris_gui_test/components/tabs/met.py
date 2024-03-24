import dash_bootstrap_components as dbc
from dash import dash_table
import data.constants as const
import data.test_data as td

met_data = dbc.Tab(
    label="Met Data",
    children=dbc.Card(
        className="mt-3",
        children=dbc.CardBody(
            [
                dash_table.DataTable(
                    td.met_data.to_dict("records", index=True),
                    const.met_station_names,
                    style_table={"minWidth": "100%"},
                    style_header={
                        "textAlign": "center",
                        "whiteSpace": "normal",
                        "overflow": "hidden",
                        "textOverflow": "ellipsis",
                    },
                    # style_data={
                    #     "whiteSpace": "normal",
                    #     "height": "auto",
                    # },
                    merge_duplicate_headers=True,
                    editable=True,
                    fixed_rows={"headers": True},
                ),
            ]
        ),
    ),
)
