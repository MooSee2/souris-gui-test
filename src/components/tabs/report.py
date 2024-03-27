import dash_bootstrap_components as dbc
from dash import html

report = dbc.Tab(
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
)
