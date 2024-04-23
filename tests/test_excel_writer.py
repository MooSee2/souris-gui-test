import pickle
from pathlib import Path

from src.souris.utils.excel_writer import souris_excel_writer


def test_souris_excel_writer():
    # Arrange
    with open("tests/test_data/excel_writer/souris_dates.pkl", "rb") as file:
        souris_dates = pickle.load(file)
    with open("tests/test_data/excel_writer/boxes.pkl", "rb") as file:
        boxes = pickle.load(file)
    with open("tests/test_data/excel_writer/discharge_daily_df.pkl", "rb") as file:
        discharge_daily_df = pickle.load(file)
    with open("tests/test_data/excel_writer/reservoir_sacs_daily.pkl", "rb") as file:
        reservoir_sacs_daily = pickle.load(file)
    with open("tests/test_data/excel_writer/roughbark_meteo_daily.pkl", "rb") as file:
        roughbark_meteo_daily = pickle.load(file)
    with open("tests/test_data/excel_writer/handsworth_meteo_daily.pkl", "rb") as file:
        handsworth_meteo_daily = pickle.load(file)
    with open("tests/test_data/excel_writer/oxbow_precip_daily.pkl", "rb") as file:
        oxbow_precip_daily = pickle.load(file)
    with open("tests/test_data/excel_writer/reservoir_sacs_monthly.pkl", "rb") as file:
        reservoir_sacs_monthly = pickle.load(file)

    report = souris_excel_writer(
        dates=souris_dates,
        boxes=boxes,
        daily_discharge=discharge_daily_df,
        daily_reservoir=reservoir_sacs_daily,
        daily_roughbark=roughbark_meteo_daily,
        daily_handsworth=handsworth_meteo_daily,
        daily_oxbow=oxbow_precip_daily,
        monthly_reservoir=reservoir_sacs_monthly,
        report_template=Path("src/souris/data/xlsx_template/BLANK_souris_natural_flow_apportionment_report.xlsx"),
    )

    with open("tests/test_report/test_report.xlsx", "wb") as file:
        file.write(report.getvalue())
