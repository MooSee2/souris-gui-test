import os

from dash import Dash, html
from dotenv import load_dotenv
from loguru import logger

import components.callbacks
from components.layout import make_layout
import dash_bootstrap_components as dbc

# from flask_cache import Cache

# TODO caching and performance: https://dash.plotly.com/performance

load_dotenv()
logger.debug(f"ENV LOG_LEVEL= {os.getenv('LOG_LEVEL')}")

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = html.Div(
    children=make_layout(),
    id="dash-root",
)

if __name__ == "__main__":
    app.run(debug=True)
