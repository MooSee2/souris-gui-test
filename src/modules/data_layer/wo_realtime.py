import os

import pandas as pd

import modules.data_layer.api_retrievers as serv
import modules.data_layer.trapz_integration as trapz

ca_reservoir_stations = (
    "05NA006",
    "05NB020",
    "05NB016",
    "05NC002",
    "05ND012",
)

ca_discharge_stations = (
    "05NA003",
    "05NB001",
    "05NB011",
    "05NB014",
    "05NB018",
    "05NB033",
    "05NB035",
    "05NB036",
    "05NB038",
    "05NB039",
    "05NB040",
    "05NB041",
)

# "Wind Speed", "m/s": 35
# "Air Temperature", "C": 1
# "Precipitation", "mm": 19?
# "Solar Radiation", "w/m2": 27
# "Relative Humidity", "%": 28

met_codes = {
    "35": "wind_speed",
    "1": "air_temp",
    "19": "precip",
    "27": "sol_rad",
    "28": "rel_humidity",
}


def drop_and_rename_columns(data: dict[str : pd.DataFrame]):
    drop_columns = {station: df.drop(["parameter", "qualifiers", "symbol", "staid", "datetime"], axis=1) for station, df in data.items()}
    return {station: df.rename(columns={"value": station, "approval": f"{station}_approval"}) for station, df in drop_columns.items()}


# def calc_trapz_integration(data):
#     return {staid: trapz.daily_value_integration(dataframe, column=staid, freq="h").round(3) for staid, dataframe in data.items()}


# def resolve_approvals(data):
#     # mouse = {}
#     # for staid, df in data.items():
#     #     df = df.resample("D").apply(lambda x: x.mode())
#     #     mouse[staid] = df
#     # return mouse
#     return {staid: df.resample("D").apply(lambda x: x.mode())[[f"{staid}_approval"]] for staid, df in data.items()}


# def join_values_and_approvals(
#     values: dict,
#     approvals: dict,
#     staids: list,
# ):
#     dfs = []
#     for staid in staids:
#         df = pd.concat([values[staid], approvals[staid]], axis=1)
#         mask = df[f"{staid}_approval"] == "Unknown"
#         df.loc[mask, staid] = float("NaN")
#         dfs.extend([df])
#     # return pd.concat(list(values.values()) + list(approvals.values()), axis=1)
#     return pd.concat(dfs, axis=1)


# # def set_dtype_float(data: dict[str, pd.DataFrame]):
# #     return {staid: df.astype(float) for staid, df in data.items()}


# def fill_approvals(data):
#     return_dict = {}
#     for staid, df in data.items():
#         mask = ~df[f"{staid}_approval"].isin(["Approved", "Provisional", "Final"])
#         df.loc[mask, f"{staid}_approval"] = "Unknown"
#         return_dict[staid] = df
#     return return_dict


def process_data(data: dict[str, pd.DataFrame], staids: list) -> pd.DataFrame:
    processed_data = drop_and_rename_columns(data)
    # approval_dvs = resolve_approvals(processed_data)
    # value_dvs = calc_trapz_integration(processed_data)
    # infilled_approvals = fill_approvals(approval_dvs)
    # joined = join_values_and_approvals(value_dvs, infilled_approvals, staids)
    joined = pd.concat(list(processed_data.values()), axis=1)
    joined["date"] = joined.index.strftime("%Y-%m-%d")
    # Last row is always garbage because trapz integration cuts it off.
    # joined.drop(joined.index[-1], inplace=True)

    return joined


def get_wo_realtime_public_discharge(year: int) -> pd.DataFrame:
    ca_discharge = serv.WaterOfficePublicRealTime()

    raw_data = ca_discharge.get(
        params={
            "stations[]": ca_discharge_stations,
            "start_date": f"{year}-01-01",
            "end_date": f"{year}-12-31",
            "parameters[]": 6,
        },
    )

    return process_data(raw_data, staids=ca_discharge_stations)


def get_wo_realtime_public_reservoirs(year: int):
    ca_discharge = serv.WaterOfficePublicRealTime()
    raw_data = ca_discharge.get(
        params={
            "stations[]": ca_reservoir_stations,
            "start_date": f"{year}-01-01",
            "end_date": f"{year}-12-31",
            "parameters[]": 3,
        },
    )

    return process_data(raw_data, staids=ca_reservoir_stations)


def process_met_data(data: dict[str : pd.DataFrame]) -> pd.DataFrame:
    grouped_data = data["05NB016"].groupby("parameter")
    renamed_columns = {station: group.rename(columns={"value": station, "approval": f"{station}_approval"}) for station, group in grouped_data}
    return


def get_wo_realtime_partner_met(year: int):
    partner_realtime = serv.WaterOfficePartnerRealTime(username=os.getenv("WORT_USERNAME"), password=os.getenv("WORT_PASSWORD"))
    raw_data = partner_realtime.get(
        params={
            "stations[]": ["05NB016", "05NCM01"],
            "start_date": f"2023-05-01%2000:00:00",
            "end_date": f"2023-05-05%2023:59:59",
            "parameters[]": ["35", "1", "19", "27", "28"],
        }
    )

    return process_met_data(raw_data)
