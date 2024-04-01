import dash_bootstrap_components as dbc
from dash import html


def report():
    return dbc.Tab(
        label="Report",
        children=dbc.Card(
            className="mt-3",
            children=dbc.CardBody(
                [
                    html.P("Report goes here", className="card-text"),
                    html.Div(className="tab2-thing"),
                ]
            ),
        ),
    )
