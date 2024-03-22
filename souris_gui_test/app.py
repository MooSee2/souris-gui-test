import sys
sys.dont_write_bytecode = True
import os

from dotenv import load_dotenv
from loguru import logger
from modules.dashboard import create_dashapp


# from flask_cache import Cache

# TODO caching and performance: https://dash.plotly.com/performance

load_dotenv()
logger.debug(f"ENV LOG_LEVEL= {os.getenv('LOG_LEVEL')}")


if __name__ == "__main__":
    app = create_dashapp()
    app.run(debug=True)
