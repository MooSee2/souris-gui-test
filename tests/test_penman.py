import pandas as pd
from src.souris_model.utils.utilities import penman


def test_penman():
    met_data = pd.read_csv("tests/test_data/test_2023_met_data.csv", index_col="date")
    df = met_data[[col for col in met_data.columns if "05NB016" in col]]
    roughbark_penman_daily = penman(
        df=df,
        wind="05NB016_wind_speed",
        temp="05NB016_air_temp",
        rel_hum="05NB016_rel_humidity",
        rad="05NB016_sol_rad",
        ELEV=567,
    )
    ...
