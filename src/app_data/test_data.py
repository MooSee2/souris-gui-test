import pandas as pd

date_range = pd.date_range("2024-01-01", periods=100, freq="d")
date_range = [date.strftime("%Y-%m-%d") for date in date_range]


def make_df_copies(stations):
    data = pd.read_csv("app_data/real_time_data.csv")
    data = data[["Date", "Value", "Approval"]]

    df_copies = []
    for station in stations:
        new_df = data.copy()
        new_df.rename(
            {
                "Date": "datetime",
                "Value": f"{station}",
                "Approval": f"{station}_approval",
            },
            axis=1,
            inplace=True,
        )
        df_copies.append(new_df)

    return df_copies


def make_dummy_data(
    stations,
):
    unique_dfs = make_df_copies(stations=stations)
    return pd.concat(unique_dfs, axis=1)



discharge_data = pd.DataFrame(
    [
        {
            "datetime": date_range,
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
)
discharge_data["datetime"] = pd.date_range("2024-01-01", periods=100, freq="d")
discharge_data["datetime"] = discharge_data["datetime"].dt.strftime("%Y-%m-%d")
discharge_data.index.name = "datetime"

met_data = pd.DataFrame(
    [
        {
            "datetime": date_range,
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
)
met_data["datetime"] = pd.date_range("2024-01-01", periods=100, freq="d")
met_data["datetime"] = met_data["datetime"].dt.strftime("%Y-%m-%d")
met_data.index.name = "datetime"
