import os

import pandas as pd
from dotenv import load_dotenv

from src.modules.data_layer.download_api_services import WaterOfficePartnerRealTime

# from src.modules.data_layer.wo_realtime import process_data


def test_get_token():
    load_dotenv("tests/.env")
    partner_realtime = WaterOfficePartnerRealTime(
        username=os.getenv("WORT_USERNAME"),
        password=os.getenv("WORT_PASSWORD"),
    )
    partner_realtime._get_token()
    assert isinstance(partner_realtime._token, str)
    assert len(partner_realtime._token) == 64


def test_get():
    load_dotenv("tests/.env")
    partner_realtime = WaterOfficePartnerRealTime(
        username=os.getenv("WORT_USERNAME"),
        password=os.getenv("WORT_PASSWORD"),
    )

    # "Wind Speed", "m/s": 35
    # "Air Temperature", "C": 1
    # "Precipitation", "mm": 19?
    # "Solar Radiation", "w/m2": 27
    # "Relative Humidity", "%": 28
    # ["05NB016", "05NCM01"]
    # [35, 1, 19, 27, 28]

    data = partner_realtime.get(
        params={
            "stations[]": ["05NB016", "05NCM01"],
            "start_date": "2023-05-01%2000:00:00",
            "end_date": "2023-05-05%2023:59:59",
            "parameters[]": ["35", "1", "19", "27", "28"],
        }
    )
    assert len(data) == 2
    assert data["05NB016"].shape[0] == 456
    assert data["05NCM01"].shape[0] == 480


# met_codes = {
#     35: "wind_speed",
#     1: "air_temp",
#     19: "precip",
#     27: "sol_rad",
#     28: "rel_humidity",
# }


# def process_met_data(data: dict[str : pd.DataFrame]) -> pd.DataFrame:
#     grouped_data = data["05NB016"].groupby("parameter")
#     renamed_columns = {station: group.rename(columns={"value": station, "approval": f"{station}_approval"}) for station, group in grouped_data}
#     drop_columns = {station: group.drop(columns=["parameter", "qualifiers", "symbol"], axis=1) for station, group in renamed_columns.items()}
#     return


# def test_process():
#     load_dotenv("tests/.env")
#     partner_realtime = WaterOfficePartnerRealTime(
#         username=os.getenv("WORT_USERNAME"),
#         password=os.getenv("WORT_PASSWORD"),
#     )

#     data = partner_realtime.get(
#         params={
#             "stations[]": ["05NB016"],
#             "start_date": "2023-05-01%2000:00:00",
#             "end_date": "2023-05-05%2023:59:59",
#             "parameters[]": ["35", "1", "19", "27", "28"],
#         }
#     )

#     processed = process_met_data(data)
#     ...


def test_get_05NB036():
    load_dotenv("tests/.env")
    partner_realtime = WaterOfficePartnerRealTime(
        username=os.getenv("WORT_USERNAME"),
        password=os.getenv("WORT_PASSWORD"),
    )

    data = partner_realtime.get(
        params={
            "stations[]": "05NB036",
            "start_date": "2023-05-01%2000:00:00",
            "end_date": "2023-05-05%2023:59:59",
            "parameters[]": 6,
        }
    )
    ...
