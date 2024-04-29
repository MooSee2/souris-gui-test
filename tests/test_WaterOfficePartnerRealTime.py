import os

from dotenv import load_dotenv

from src.modules.data_layer.download_api_services import WaterOfficePartnerRealTime


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
