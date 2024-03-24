import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.inspection import inspect




# class SQLEngineSerializer:
#     def serialize(self):
#         return {c: getattr(self, c) for c in inspect(self).attrs.keys()}

#     @staticmethod
#     def serialize_list(l):
#         return [m.serialize() for m in l]


def make_dropdown_options(data: set[tuple]) -> list[dict]:
    dropdowns = [{"label": staid, "value": name, "group": group} for staid, name, group in data]
    return sorted(dropdowns, key=lambda x: x["group"])


def load_data(start_date, end_date) -> tuple[pd.DataFrame]:
    import data.test_data as td

    return td.discharge_data, td.met_data, td.reservoir_data
