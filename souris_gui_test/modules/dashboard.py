import sqlalchemy as sa
import plotly.graph_objects as go

from .server import db
from .models import gapminder
from dash import Dash, html, dcc, Input, Output


def create_dashapp(server):
    # Initialize the app
    app = Dash(__name__, server=server)

    # App layout
    app.layout = html.Div()

    return app
