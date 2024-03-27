import os
from typing import Union

import pandas as pd

import src.modules.data_layer.CAAQ_download as du
from modules.data_layer import timeseries_client as aqts

stations_dict = [
    {"id": "05NA006", "type": "reservoir", "name": "Larsen Reservoir", "unique_id": "013d9d474541460aa3b1de4381276c38"},
    {"id": "05NB020", "type": "reservoir", "name": "Nickle Lake", "unique_id": "988537b8321f47a5a421bfa23c19263a"},
    {"id": "05NB016", "type": "reservoir", "name": "Roughbark Reservoir", "unique_id": "cd827ce017344fd7b2764dceab9d6989"},
    {"id": "05NC002", "type": "reservoir", "name": "Moose Mountain Lake", "unique_id": "21a5a52a1f8447ffa6c872429ef94a39"},
    {"id": "05ND012", "type": "reservoir", "name": "Grant Devine Reservoir", "unique_id": "fda763c4468b47bc9d693a14a6b77ba2"},
    {"id": "05NB001", "type": "discharge", "name": "Long Creek near Estevan", "unique_id": "ec83a47a06d4410e84ba94d384fb0523"},
    {"id": "05NB036", "type": "discharge", "name": "Souris River below Rafferty Reservoir", "unique_id": "8f6f1b90e5f34a0cb08ed1c7a81f11c2"},
    {"id": "05NB011", "type": "discharge", "name": "Yellograss Ditch", "unique_id": "d8cadb5a4c524fd1a8b172a04d00382b"},
    {"id": "05NB018", "type": "discharge", "name": "Tatagwa Lake Drain", "unique_id": "8572ab68835341a09f093ef947d167b2"},
    {"id": "05NA003", "type": "discharge", "name": "Long Creek at Western Crossing", "unique_id": "2e2cb41a826c4743ac2e12ce08c96310"},
    {"id": "05NB040", "type": "discharge", "name": "Souris River near Ralph", "unique_id": "83d5168d48194b2ab0520a0510c51d80"},
    {"id": "05NB041", "type": "discharge", "name": "Roughbark Creek above Rafferty Res.", "unique_id": "2e7f3f3b51bd4605b240a21fb0e17009"},
    {"id": "05NB038", "type": "discharge", "name": "Boundary Reservoir Diversion Canal", "unique_id": "62744ab8cf244767ae9d78307db39668"},
    {"id": "05NB014", "type": "discharge", "name": "Jewel Creek near Goodwater", "unique_id": "2cb7747424bc49b3ae2e7acf16dfb7d9"},
    {"id": "05NB035", "type": "discharge", "name": "Cooke Creek near Goodwater", "unique_id": "4f97b149655e4ec8bfa16b35b9933d7a"},
    {"id": "05NB033", "type": "discharge", "name": "Moseley Creek near Halbrite", "unique_id": "d124778abe524653ac32e82212cfe41b"},
    {"id": "05NB039", "type": "discharge", "name": "Tributary near Outram", "unique_id": "098e25d30c7244b4a158927efb324d4d"},
]

unique_id_to_staid = {station["unique_id"]: station["id"] for station in stations_dict}


def process_return_aq_data(data: dict) -> Union[pd.DataFrame, None]:
    df = pd.DataFrame(data["Points"])

    # AQ will always return something, but it may not have data.
    if df.empty:
        return None

    df["value"] = df["Value"].apply(pd.Series)

    df.rename(
        {"Timestamp": "datetime", "value": data["UniqueId"]},
        axis=1,
        inplace=True,
    )
    # df["datetime"] = pd.to_datetime(df["datetime"]).dt.tz_localize(None)
    df.index = pd.DatetimeIndex(pd.to_datetime(df["datetime"])).tz_localize(None)

    df.drop(
        ["Value", "datetime"],
        axis=1,
        inplace=True,
    )

    return {"unique_id": data["UniqueId"], "data": df}


def post_process_aq_dfs(data: dict, type: str) -> pd.DataFrame:
    """Process return data from get_caaq_data() to single DataFrame grouped by type.

    Parameters
    ----------
    data : dict
        Returned dictionary from get_caaq_data()
    type : str
        "discharge", "reservoirs", "met"

    Returns
    -------
    pd.DataFrame
        DataFrame ready to send to Dash datatables in app.
    """
    filtered_df_types = [d for d in data for f in stations_dict if (d.get("unique_id") == f.get("unique_id") and f.get("type") == type)]
    # reservoirs = [station["data"].rename({"value": station['unique_id']}, axis=1, inplace=True) for station in reservoirs]
    data = [d[key] for d in filtered_df_types for key in d if isinstance(key, str)]
    data = data[1::2]
    data = pd.concat(data, axis=1)
    data.rename(unique_id_to_staid, axis=1, inplace=True)
    data = data.round(decimals=3)
    data["datetime"] = data.index.astype(str)
    return data


# Returns list of dicts: {unique_id: DataFrame}
def get_caaq_data(start_date: str, end_date: str, stations: list) -> dict[str, pd.DataFrame]:
    aq_user = os.getenv("AQ_USERNAME")
    aq_password = os.getenv("AQ_PASSWORD")
    server = os.getenv("AQTS_SERVER")

    unique_ids = [unique_id for *_, unique_id in stations]

    payloads = [
        {
            "TimeSeriesUniqueId": unique_id,
            "QueryFrom": start_date,
            "QueryTo": end_date,
            # "ApplyRounding": "true",
        }
        for unique_id in unique_ids
    ]

    with aqts.timeseries_client(server, aq_user, aq_password) as session:
        return_data = [session.publish.get("/GetTimeSeriesCorrectedData", params=payload) for payload in payloads]

        return [du.process_return_aq_data(data) for data in return_data]
