import pandas as pd


def load_data(start_date, end_date) -> tuple[pd.DataFrame]:
    import app_data.test_data as td

    return td.discharge_data, td.met_data, td.reservoir_data
