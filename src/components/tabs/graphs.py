import dash_bootstrap_components as dbc
import dash_mantine_components as dmc
import app_data.stations as const
import app_data.test_data as td
import modules.data_layer as dl
from dash import dash_table, dcc, html

graphs = dbc.Tab(
    label="Graphs",
    children=[
        dbc.Card(
            className="mt-3",
            children=[
                dbc.CardBody(
                    children=[
                        html.Div(
                            [
                                dmc.MultiSelect(
                                    label="Select category",
                                    placeholder="Select Station",
                                    searchable=True,
                                    id="timeseries-dropdown",
                                ),
                            ]
                        ),
                        # dbc.DropdownMenu(
                        #     id="timeseries-dropdown",
                        #     children=[
                        #         dbc.DropdownMenuItem("Header", header=True),
                        #         dbc.DropdownMenuItem("An item"),
                        #         dbc.DropdownMenuItem(divider=True),
                        #         dbc.DropdownMenuItem("Active and disabled", header=True),
                        #         dbc.DropdownMenuItem("Active item", active=True),
                        #         dbc.DropdownMenuItem("Disabled item", disabled=True),
                        #         dbc.DropdownMenuItem(divider=True),
                        #         html.P(
                        #             "You can have other content here like text if you like.",
                        #             className="text-muted px-4 mt-4",
                        #         ),
                        #     ],
                        #     label="Stations",
                        # ),
                        dcc.Loading(
                            children=[
                                dcc.Graph(id="timeseries-plot"),
                            ],
                        ),
                    ]
                ),
            ],
        ),
    ],
)
