from datetime import date
from datetime import datetime as dt
from dash import html, dcc
import dash_bootstrap_components as dbc


navbar = dbc.NavbarSimple(
    id="navbar",
    children=[
        dbc.NavItem(dbc.NavLink("Page 1", href="#")),
        # dbc.DropdownMenu(
        #     children=[
        #         dbc.DropdownMenuItem("More pages", header=True),
        #         dbc.DropdownMenuItem("Page 2", href="#"),
        #         dbc.DropdownMenuItem("Page 3", href="#"),
        #     ],
        #     nav=True,
        #     in_navbar=True,
        #     label="More",
        # ),
    ],
    brand="IJC",
    brand_href="#",
    color="primary",
    dark=True,
)


aside = html.Aside(
    children=[
        # html.Div(
        #     className="config-card",
        #     children=[
        #     ],
        # ),
        html.Div(
            className="config-card",
            children=[
                html.H4("Settings"),
                html.Br(),
                html.H6("Met Station"),
                dcc.Dropdown(
                    options=[
                        {"label": "Gildford", "value": "Gildford"},
                        {"label": "Eastern Crossing", "value": "MRatEC"},
                    ],
                    value="MRatEC",
                    clearable=False,
                    # optionHeight=20,
                ),
                html.Br(),
                html.Div(
                    className="input-container",
                    children=[
                        html.H6("Evaporation Start"),
                        dcc.DatePickerSingle(date=date(int(dt.now().year), 4, 15)),
                    ],
                ),
                html.Div(
                    className="input-container",
                    children=[
                        html.H6("Evaporation End"),
                        dcc.DatePickerSingle(date=date(int(dt.now().year), 10, 15)),
                    ],
                ),
            ],
        ),
        html.Div(
            className="reported-flows-card",
            children=[
                html.H4("Reported flows"),
                html.Div(
                    className="input-container",
                    children=[
                        html.H6("City of Weyburn"),
                        dbc.Input(id="city-of-weyburn", placeholder="Units: DAM3", class_name="reported-flows-input", type="number"),
                    ],
                ),
                html.Div(
                    className="input-container",
                    children=[
                        "The Lake",
                        dbc.Input(id="the-lake", placeholder="Units: DAM3", class_name="reported-flows-input", type="number"),
                    ],
                ),
                html.Div(
                    className="input-container",
                    children=[
                        "Pumpage",
                        dbc.Input(id="pumpage", placeholder="Units: DAM3", class_name="reported-flows-input", type="number"),
                    ],
                ),
                html.Div(
                    className="input-container",
                    children=[
                        "Pipe",
                        dbc.Input(id="pipe", placeholder="Units: DAM3", class_name="reported-flows-input", type="number"),
                    ],
                ),
            ],
        ),
        html.Div(
            className="calculate-card",
            children=[dbc.Button("Calculate", color="secondary", id="calc-button")],
        ),
    ],
)

main = html.Main(
    children=[
        dbc.Tabs(
            [
                dbc.Tab(
                    id="tabtab",
                    label="Input",
                    children=dbc.Card(
                        className="mt-3",
                        children=dbc.CardBody(
                            [
                                dcc.Upload(
                                    id="upload-data",
                                    children=html.Div(
                                        [
                                            "Drag and Drop or ",
                                            html.A("Select Files"),
                                        ],
                                    ),
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
                ),
                dbc.Tab(
                    label="Report",
                    children=dbc.Card(
                        className="mt-3",
                        children=dbc.CardBody(
                            [
                                html.P("This is tab 2!", className="card-text"),
                                html.Div(className="tab2-thing"),
                                html.Div(className="tab2-thing"),
                                html.Div(className="tab2-thing"),
                                html.Div(className="tab2-thing"),
                                html.Div(className="tab2-thing"),
                                html.Div(className="tab2-thing"),
                                html.Div(className="tab2-thing"),
                                html.Div(className="tab2-thing"),
                                html.Div(className="tab2-thing"),
                            ]
                        ),
                    ),
                ),
                dbc.Tab(
                    label="Calculated",
                    children=html.P("Meow!"),
                ),
            ],
        ),
    ],
)


def make_layout():
    return [
        navbar,
        html.Div(
            id="interior-container",
            children=[
                aside,
                main,
            ],
        ),
    ]
