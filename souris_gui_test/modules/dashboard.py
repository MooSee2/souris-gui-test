import components.callbacks
import dash_bootstrap_components as dbc
import plotly.graph_objects as go
import sqlalchemy as sa
from components.layout import make_layout
from dash import Dash, Input, Output, dcc, html

from .models import gapminder
from .server import db


def create_dash_app(server):
    external_stylesheets = [
        dbc.themes.BOOTSTRAP,
        dbc.icons.FONT_AWESOME,
    ]

    app = Dash(
        __name__,
        server=server,
        external_stylesheets=external_stylesheets,
    )

    app.layout = html.Div(
        children=make_layout(),
        id="dash-root",
    )
    return app
