import pandas as pd

import souris_model.utils.reservoir_capacity as rcap
import souris_model.utils.utilities as util

ca_reservoir_stations = (
    "05NA006",
    "05NB020",
    "05NB016",
    "05NC002",
    "05ND012",
)


def process_reservoir_sacs(
    reservoir_elevation_daily,
    wateryear,
) -> tuple[dict, dict]:
    reservoir_daily_dict = {staid: reservoir_elevation_daily[[staid, f"{staid}_approval"]] for staid in ca_reservoir_stations}

    # Assign Stage-Area-Capacity values
    reservoir_sacs_daily = {staid: rcap.assign_res_sac(staid=staid, dataframe=dataframe) for staid, dataframe in reservoir_daily_dict.items()}

    # Resample to monthly values
    reservoir_daily_dict_no_approval = {staid: reservoir_elevation_daily[[staid]] for staid in ca_reservoir_stations}
    reservoir_elevations_monthly = {staid: dataframe.groupby(pd.Grouper(freq="ME")).mean().round(3) for staid, dataframe in reservoir_daily_dict_no_approval.items()}
    reservoir_elevations_monthly = {staid: dataframe.loc[f"{wateryear}-01":f"{wateryear}-12"] for staid, dataframe in reservoir_elevations_monthly.items()}
    reservoir_elevations_monthly = {staid: util.rename_monthly_index(dataframe) for staid, dataframe in reservoir_elevations_monthly.items()}

    # Assign Stage-Area-Capacity values to monthly values
    reservoir_sacs_monthly = {staid: rcap.assign_res_sac(staid=staid, dataframe=dataframe) for staid, dataframe in reservoir_elevations_monthly.items()}

    # Page 19 of Procedures, subtract 8500 dam2 to account for natural lake
    reservoir_sacs_monthly["05NC002"]["area_dam2"] -= 8500
    return reservoir_sacs_daily, reservoir_sacs_monthly
