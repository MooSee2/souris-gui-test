import pandas as pd


def process_return_aq_data(data: dict) -> pd.DataFrame:
    df = pd.DataFrame(data["Points"])

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
    return {data["UniqueId"]: df}
