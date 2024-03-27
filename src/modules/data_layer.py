import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.inspection import inspect


def make_dropdown_options(data: set[tuple]) -> list[dict]:
    dropdowns = [{"label": staid, "value": name, "group": group} for staid, name, group in data]
    return sorted(dropdowns, key=lambda x: x["group"])


def load_data(start_date, end_date) -> tuple[pd.DataFrame]:
    import app_data.test_data as td

    return td.discharge_data, td.met_data, td.reservoir_data

#TODO data access layer better
