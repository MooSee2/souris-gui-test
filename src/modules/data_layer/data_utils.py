import pandas as pd
from typing import Union


def process_return_aq_data(data: dict) -> Union[pd.DataFrame, None]:
    df = pd.DataFrame(data["Points"])

    # AQ will always return something, but it may not have data.
    if df.empty:
        return None

    df["value"] = df["Value"].apply(pd.Series)

    df.drop(
        "Value",
        axis=1,
        inplace=True,
    )

    df.rename(
        {"Timestamp": "datetime"},
        axis=1,
        inplace=True,
    )
    df["datetime"] = pd.to_datetime(df["datetime"])
    return {"unique_id": data["UniqueId"], "data": df}
