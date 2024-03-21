import pandas as pd

reservoir_data = pd.DataFrame(
    [
        {
            "datetime": "2023-01-09",
            "05NA006": i,
            "05NB020": i * 10,
            "05NB016": i * 100,
            "05NC002": i * -1,
            "05ND012": i * -10,
        }
        for i in range(100)
    ],
    index=pd.date_range("2024-01-01", periods=100, freq="d")
)
reservoir_data["datetime"] = reservoir_data.index.strftime('%Y-%m-%d')
reservoir_data.index.name = "datetime"

discharge_data = pd.DataFrame(
    [
        {
            "05NB001": i * -100,
            "05NB036": i * 7,
            "05NB011": i * 88,
            "05NB018": i * 510,
            "05NA003": i * -5,
            "05NB040": i * 5,
            "05NB041": i * 50,
            "05NB038": i * 8,
            "05NB014": i * 5,
            "05NB035": i * 9,
            "05NB033": i * 7,
            "05NB039": i * 12,
        }
        for i in range(100)
    ],
    index=pd.date_range("2024-01-01", periods=100, freq="d"),
)
discharge_data.index.name = "datetime"

met_data = pd.DataFrame(
    [
        {
            "1234_wind_speed": i,
            "1234_air_temp": i * 10,
            "1234_sol_rad": i * 100,
            "1234_rel_humidity": i * -1,
            "1234_precip": i * -10,
            "4321_wind_speed": i,
            "4321_air_temp": i * 10,
            "4321_sol_rad": i * 100,
            "4321_rel_humidity": i * -1,
            "4321_precip": i * -10,
        }
        for i in range(100)
    ],
    index=pd.DatetimeIndex(pd.date_range("2024-01-01", periods=100, freq="d"))
)
met_data.index.name = "datetime"
