import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.inspection import inspect
from sqlalchemy.pool import SingletonThreadPool

"""This could be a class, but Dash is stateless and stateful
objects may cause side effects
"""

# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy

# class Config(object):
#     SQLALCHEMY_DATABASE_URI = 'sqlite:///app.db'
#     SQLALCHEMY_TRACK_MODIFICATIONS = False

# db = SQLAlchemy()


# def create_app():
#     server = Flask(__name__)
#     server.config.from_object(Config)
#     db.init_app(server)
    
#     with server.app_context():
#         df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder2007.csv')
#         df.to_sql('gapminder2007', con=db.engine, if_exists='replace')

#     from .dashboard import create_dashapp
#     dash_app = create_dashapp(server)
#     return server # or dash app if you use debug mode in dash import SQLAlchemy

# class Config(object):
#     SQLALCHEMY_DATABASE_URI = 'sqlite:///app.db'
#     SQLALCHEMY_TRACK_MODIFICATIONS = False

# db = SQLAlchemy()


# def create_app():
#     server = Flask(__name__)
#     server.config.from_object(Config)
#     db.init_app(server)
    
#     with server.app_context():
#         df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder2007.csv')
#         df.to_sql('gapminder2007', con=db.engine, if_exists='replace')

#     from .dashboard import create_dashapp
#     dash_app = create_dashapp(server)
#     return server # or dash app if you use debug mode in dash

engine = create_engine(
    "sqlite+pysqlite:///:memory:",
    connect_args={"check_same_thread": False},
    poolclass=SingletonThreadPool,
)


def commit_df_to_db(data: dict[str, pd.DataFrame]) -> None:
    """Commit df to DB where the the input dictionary keys are
    DB table names such as: "discharge," "reservoir," or "met"
    and the items are DataFrames of the associated data.

    Parameters
    ----------
    data : dict[str, pd.DataFrame]
        Dictionary of Station types to DataFrames.

    Return
    ------
    None
    """
    with engine.connect() as conn:
        for name, data in data.items():
            data.to_sql(name=name, con=conn, if_exists="replace", index=False)
    return None

# sql = f"SELECT * FROM {table} WHERE dataset IN ({str(staid[0])})"

def from_db(sql: str) -> pd.DataFrame:
    with engine.connect() as conn:
        df = pd.read_sql(sql, con=conn)

    df.index = pd.DatetimeIndex(pd.to_datetime(df.index))
    return df
