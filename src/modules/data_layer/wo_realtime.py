import pandas as pd

import modules.data_layer.download_api_services as serv
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


def drop_and_rename_columns(data: dict[str : pd.DataFrame]):
    drop_columns = {station: df.drop(["parameter", "qualifiers", "symbol", "staid", "datetime"], axis=1) for station, df in data.items()}
    return {station: df.rename(columns={"value": station, "approval": f"{station}_approval"}) for station, df in drop_columns.items()}


def calc_trapz_integration(data):
    return {staid: trapz.daily_value_integration(dataframe, column=staid, freq="h").round(3) for staid, dataframe in data.items()}


def resolve_approvals(data):
    return {staid: df.resample("D").apply(lambda x: x.mode())[[f"{staid}_approval"]] for staid, df in data.items()}


def join_values_and_approvals(values, approvals):
    return pd.concat(list(values.values()) + list(approvals.values()), axis=1)


# def set_dtype_float(data: dict[str, pd.DataFrame]):
#     return {staid: df.astype(float) for staid, df in data.items()}


def fill_approvals(data):
    return_dict = {}
    for staid, df in data.items():
        mask = ~df[f"{staid}_approval"].isin(["Approved", "Provisional"])
        df.loc[mask, f"{staid}_approval"] = "Unverified"
        return_dict[staid] = df
    return return_dict


def process_data(data: dict[str, pd.DataFrame]):
    processed_data = drop_and_rename_columns(data)
    approval_dvs = resolve_approvals(processed_data)
    value_dvs = calc_trapz_integration(processed_data)
    infilled_approvals = fill_approvals(approval_dvs)
    joined = join_values_and_approvals(value_dvs, infilled_approvals)
    joined["date"] = joined.index.strftime("%Y-%m-%d")
    # Last row is always garbage because trapz integration cuts it off.
    joined.drop(joined.index[-1], inplace=True)

    return joined


def get_wo_realtime_discharge(year):
    ca_discharge = serv.WaterOfficeRealTime()

    raw_data = ca_discharge.get(
        params={
            "stations[]": ca_discharge_stations,
            "start_date": f"{year}-01-01",
            "end_date": f"{year}-12-31",
            "parameters[]": 47,
        },
    )

    return process_data(raw_data).fillna("-6999")


def get_wo_realtime_reservoirs(year):
    ca_discharge = serv.WaterOfficeRealTime()
    raw_data = ca_discharge.get(
        params={
            "stations[]": ca_reservoir_stations,
            "start_date": f"{year}-01-01",
            "end_date": f"{year}-12-31",
            "parameters[]": 46,
        },
    )

    return process_data(raw_data)
