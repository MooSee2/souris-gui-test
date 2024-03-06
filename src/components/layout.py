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
    [html.Div(style={"height": "20px", "width": "150px", "background": "blue"}, id="in-aside")]
)


tab1_content = dbc.Card(
    dbc.CardBody(
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
        ]
    ),
    className="mt-3",
)

tab2_content = dbc.Card(
    dbc.CardBody(
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
    className="mt-3",
)


tabs = dbc.Tabs(
    [
        dbc.Tab(tab1_content, label="Input"),
        dbc.Tab(tab2_content, label="Report"),
        dbc.Tab(html.P("Meow!"), label="Calculated"),
    ],
)


main = html.Main(
    children=[
        tabs,
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
