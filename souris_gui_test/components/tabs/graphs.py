import dash_bootstrap_components as dbc
import dash_mantine_components as dmc
import data.constants as const
import data.test_data as td
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
                                    data=dl.make_dropdown_options(const.stations),
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
                        dcc.Graph(id="timeseries-plot"),
                    ]
                ),
            ],
        ),
    ],
)
