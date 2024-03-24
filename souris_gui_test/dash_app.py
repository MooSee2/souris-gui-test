import os
import sys

sys.dont_write_bytecode = True

import components.callbacks.callbacks
import dash_bootstrap_components as dbc
from flask_caching import Cache
from components.layout import make_layout
from dash import Dash, html
from dotenv import load_dotenv
from loguru import logger


load_dotenv()
logger.debug(f"ENV LOG_LEVEL= {os.getenv('LOG_LEVEL')}")

external_stylesheets = [
    dbc.themes.BOOTSTRAP,
    dbc.icons.FONT_AWESOME,
]

app = Dash(
    name=__name__,
    external_stylesheets=external_stylesheets,
)

app.layout = html.Div(
    children=make_layout(),
    id="dash-root",
)

cache = Cache(
    app.server,
    config={
        "CACHE_TYPE": "filesystem",
        "CACHE_DIR": "data_cache",
    },
)

if __name__ == "__main__":
    app.run(debug=True)
