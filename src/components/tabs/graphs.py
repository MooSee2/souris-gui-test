import dash_bootstrap_components as dbc
import dash_mantine_components as dmc
from dash import dcc, html

timeseries_dropdown_stations = {
    ("Long Creek near Estevan", "05NB001", "Rivers"),
    ("Souris River below Rafterty", "05NB036", "Rivers"),
    ("Yellowgrass Ditch", "05NB011", "Rivers"),
    ("Tatagra Lake Drain", "05NB018", "Rivers"),
    ("Long Creek at Western Crossing", "05NA003", "Rivers"),
    ("Souris River near Ralph", "05NB040", "Rivers"),
    ("Roughbark Creek above Rafferty Res.", "05NB041", "Rivers"),
    ("Boundary Res. Diversion Canal", "05NB038", "Rivers"),
    ("Jewel Creek near Goodwater", "05NB014", "Rivers"),
    ("Cooke Creek near Goodwater", "05NB035", "Rivers"),
    ("Moseley Creek near Halbrite", "05NB033", "Rivers"),
    ("Tributary near Outram", "05NB039", "Rivers"),
    ("Larson", "05NA006", "Reservoirs"),
    ("Nickle Lake", "05NB020", "Reservoirs"),
    ("Roughbark", "05NB016", "Reservoirs"),
    ("Moose Mountain Lake", "05NC002", "Reservoirs"),
    ("Grant Devine", "05ND012", "Reservoirs"),
    ("Roughbark Wind Speed, Units: m/s", "1234_wind_speed", "Met Stations"),
    ("Roughbark Air Temperature, Units: C", "1234_air_temp", "Met Stations"),
    ("Roughbark Solar Radiation, Units: w/m", "1234_sol_rad", "Met Stations"),
    ("Roughbark Relative Humidity, Units: %", "1234_rel_humidity", "Met Stations"),
    ("Roughbark Precipitation, Units: mm", "1234_precip", "Met Stations"),
    ("Handsworth Wind Speed, Units: m/s", "4321_wind_speed", "Met Stations"),
    ("Handsworth Air Temperature, Units: C", "4321_air_temp", "Met Stations"),
    ("Handsworth Solar Radiation, Units: w/m\u00b2", "4321_sol_rad", "Met Stations"),
    ("Handsworth Relative Humidity, Units: %", "4321_rel_humidity", "Met Stations"),
    ("Handsworth Precipitation, Units: mm", "4321_precip", "Met Stations"),
}


def make_dropdown_options(data: set[tuple]) -> list[dict]:
    dropdowns = [{"label": staid, "value": name, "group": group} for staid, name, group in data]
    return sorted(dropdowns, key=lambda x: (x["group"], x["label"]))


def graphs():
    return dbc.Tab(
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
                                        data=make_dropdown_options(timeseries_dropdown_stations),
                                        label="Select Station",
                                        placeholder="Stations",
                                        searchable=True,
                                        id="timeseries-dropdown",
                                        maxDropdownHeight="350px",
                                        disabled=True,
                                    ),
                                ]
                            ),
                            html.Div(
                                className="loading-graph-wrapper",
                                children=[
                                    dcc.Graph(
                                        id="timeseries-plot",
                                        figure={
                                            "layout": {
                                                "xaxis": {"visible": False},
                                                "yaxis": {"visible": False},
                                                "annotations": [
                                                    {
                                                        "text": "No Data Selected.",
                                                        "xref": "paper",
                                                        "yref": "paper",
                                                        "showarrow": False,
                                                        "font": {"size": 28},
                                                    }
                                                ],
                                            }
                                        },
                                    ),
                                    dcc.Loading(id="time-series-loader"),
                                ],
                            ),
                        ],
                    ),
                ],
            ),
        ],
    )
