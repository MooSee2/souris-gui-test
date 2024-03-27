import sys

sys.dont_write_bytecode = True
import os
from datetime import datetime as dt
from datetime import time
from pathlib import Path

import dash_bootstrap_components as dbc
from dash import Dash, html
from dotenv import load_dotenv
from flask_caching import Cache
from loguru import logger

import components.callbacks.callbacks
from components.layout import make_layout

load_dotenv(".env")

LOG_PATH = Path("src/logs/app_log.log")

logger.remove(0)
logger.add(LOG_PATH, backtrace=True, rotation=time(hour=23), retention=5, level="TRACE")
logger.add(sys.stderr, level=os.getenv("LOGGING_LEVEL", "INFO"))
logger.debug(f"ENV LOG_LEVEL= {os.getenv('LOG_LEVEL')}")

now = dt.now().strftime("%Y-%m-%d %H:%M:%S.%f")
logger.info(f"Program starting at {now}")

external_stylesheets = [
    dbc.themes.BOOTSTRAP,
    dbc.icons.FONT_AWESOME,
]

app = Dash(
    name=__name__,
    title="Souris Apportionment App",
    external_stylesheets=external_stylesheets,
)

app._favicon = "assets/images/favicon.ico"

app.layout = html.Div(
    children=make_layout(),
    id="dash-root",
)

cache = Cache(
    app.server,
    config={
        "CACHE_TYPE": "filesystem",
        "CACHE_DIR": ".cache",
    },
)

if __name__ == "__main__":
    app.run(debug=True)
