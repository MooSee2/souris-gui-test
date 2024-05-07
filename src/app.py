import sys

sys.dont_write_bytecode = True
import os
from datetime import datetime as dt
from pathlib import Path

import dash_bootstrap_components as dbc
from dash import Dash, html
from dotenv import load_dotenv
from loguru import logger

import components.callbacks.callbacks
from components.layout.custom_index import index_string
from components.layout.layout import make_layout


load_dotenv()
LOG_PATH = Path("logs/app_log.log")

logger.remove(0)
logger.add(LOG_PATH, backtrace=True, level="TRACE", rotation="5 MB")
logger.add(sys.stderr, level=os.getenv("LOGGING_LEVEL", "INFO"))
logger.debug(f"ENV LOG_LEVEL= {os.getenv('LOG_LEVEL')}")

now = dt.now().strftime("%Y-%m-%d %H:%M:%S.%f")
logger.info(f"Program starting at {now}")


external_stylesheets = [
    # dbc.themes.BOOTSTRAP,
    dbc.icons.FONT_AWESOME,
]

app = Dash(
    name=__name__,
    assets_folder="assets",
    title="Souris Apportionment App",
    external_stylesheets=external_stylesheets,
    index_string=index_string,
)

app._favicon = "assets/images/favicon.ico"

app.layout = html.Div(
    children=make_layout(),
    id="dash-root",
)

if __name__ == "__main__":
    app.run(
        debug=os.getenv("DASH_DEBUG", False).lower() in ("true", "1", "t"),
        port=os.getenv("PORT", "5000"),
        host=os.getenv("ADDRESS", "127.0.0.1"),
    )
