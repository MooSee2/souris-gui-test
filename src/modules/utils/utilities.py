import datetime as dt
import pandas as pd

year_now = dt.datetime.now().year


def dummy_datetime(year=year_now):
    datetime = pd.date_range(f"{year}-01-01", f"{year}-12-31", freq="d").strftime("%Y-%m-%d")
    return pd.DataFrame({"date": datetime})
