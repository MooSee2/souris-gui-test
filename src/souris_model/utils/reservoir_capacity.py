from datetime import datetime as dt
from numbers import Number

import pandas as pd
import souris_model.utils.services as serv


def assign_res_sac(staid: str, dataframe: pd.DataFrame) -> pd.DataFrame:
    SAC_TABLES = {
        "05ND012": "souris_model/data/stage_area_capacity_tables/grant_devine_sac.csv",
        "05NA006": "souris_model/data/stage_area_capacity_tables/larsen_sac.csv",
        "05NC002": "souris_model/data/stage_area_capacity_tables/moose_mountain_sac.csv",
        "05NB020": "souris_model/data/stage_area_capacity_tables/nickle_sac.csv",
        "05NB016": "souris_model/data/stage_area_capacity_tables/roughbark_sac.csv",
    }
    sac_table = pd.read_csv(SAC_TABLES[staid])
    data = dataframe.dropna().round(decimals=3).sort_values(by=[staid])
    merged_df = pd.merge_asof(data, sac_table, left_on=staid, right_on="elevation_m", direction="forward")  # left keys must be sorted i.e. stage/discharge
    merged_df = merged_df.drop("elevation_m", axis=1)
    merged_df.set_index(data.index, inplace=True)
    merged_df.sort_index(inplace=True)
    return merged_df


def lake_darling_condition(start_date: str, sherwood: Number) -> bool:
    """Check Lake Darling Conditional.

    Parameters
    ----------
    start_date : str
        Start date of the apportionment year.
    sherwood : Number
        The cumulative Natural Flow at Sherwood in DAM3 (Box44).

    Returns
    -------
    bool
        True or False representing the Lake Darling Conditionalal.

    Notes
    -----
    sherwood = Souris River near Sherwood, USGS STAID: 05114000
    sherwood = boxes["box44"] = boxes["box42"] + boxes["box43"] - boxes["box41"]

    Lake Darling Near Foxholm, ND, USGS STAID: 05115500
    PCode: 62614 = Lake or reservoir water surface elevation above NGVD 1929, feet

    Depending on the natural flow volume and elevation conditions at Lake Darling,
    the U.S. is entitled to 50% of the natural flow or 40% of the natural flow.
    # Condition 1 for 60/40 SK/ND split of natural flow
    # Annual NatFlow volume at Sherwood > 50000 DAM3
    # AND on June 1 of current year, Lake Darling elevation > 1594.8 feet
    # Condition 2 for 60/40 SK/ND split of natural flow
    # Annual NatFlow volume at Sherwood > 50000 DAM3
    # AND On June 1 of the current year, Lake Darling elevation > 1593.8 feet
    # AND Since the last time the elevation of Lake Darling was over 1594.8 feet on June 1st,
    #   the June 1st elevation of Lake Darling has not been less than 1593.8 feet.
    """
    NGVD29_OFFSET = 1500  # Gage height is quesied directly then converted to NGVD29.
    SHERWOOD_VOLUME_COND = 50000  # DAM3
    LAKE_DARLING_ELEV_COND_1 = 1594.8  # NGVD 29 feet
    LAKE_DARLING_ELEV_COND_2 = 1593.8  # NGVD 29 feet

    # Check Recommendation 1, condition 1, part A
    if sherwood <= SHERWOOD_VOLUME_COND:
        return False

    start_date = dt.strptime(start_date, "%Y-%m-%d")
    if start_date.year <= 2023:
        return True
    nwis_service = serv.NWISWaterService(service="dv")
    lake_darling = nwis_service.get(
        dict(
            sites="05115500",
            startDt=f"{start_date.year}-06-01",
            endDt=f"{start_date.year}-06-01",
            parameterCd="00065",  # Gage height (ft)
            format="json",
        )
    )

    # If running apportionment before June 1, default to True.
    if not lake_darling:
        return True

    lake_darling["value"] = lake_darling["value"] + NGVD29_OFFSET
    darling_current_elev = lake_darling.loc[f"{start_date.year}-06-01"]["value"]

    # Check Recommendation 1, condition 1, part B
    if darling_current_elev > LAKE_DARLING_ELEV_COND_1:
        return True

    # Check Recommendation 1, condition 2, part B
    if darling_current_elev <= LAKE_DARLING_ELEV_COND_2:
        return False

    # Check Recommendation 1, condition 2, part C
    if get_lake_darling_cond2_c(
        june1_elev=darling_current_elev,
        year=start_date.year,
        elev_lower_limit=LAKE_DARLING_ELEV_COND_2,
        elev_upper_limit=LAKE_DARLING_ELEV_COND_1,
    ):
        return True

    return False


def get_lake_darling_cond2_c(
    june1_elev: float,
    year: int,
    elev_lower_limit: float,
    elev_upper_limit: float,
) -> bool:
    """Check Lake Darling Condition 2, part c

    Parameters
    ----------
    june1_elev : float
        The elevation of Lake Darling on June 1 of the year parameter.
    year : int
        The year to check the June 1 Lake Darling elevation.
    elev_lower_limit : float
        Lower elevation limit to check if condition is met.
    elev_upper_limit : float
        Upper elevation limit to check if condition is met.

    Returns
    -------
    bool
        True if condition 2, part c is met.  False otherwise.

    Notes
    -----
    Condition 2 part C states:
    Since the last time the elevation of Lake Darling was over 486.095 meters (1594.8 feet) on June 1st,
    the June 1st elevation of Lake Darling has not been less than 485.79 meters (1593.8 feet) NGVD 29.

    E.g. If the apportionment year for the program is 2022, check if June 1, 2022 Lake Darling
    elevation is above 1593.8 feet.  If True, check if June 1, 2021 elevation is above 1593.8 feet.
    If False, the condition is not met.
    If True, check if June 1, 2020 is above 1593.8 feet.
    Continue checking years and as long as the June 1 elevation is above 1593.8, continue checking previous years.
    This process continues until the June 1 elevation is below 1593.8 and returns False,
    OR
    if the June 1 elevation is above 1594.8, return True as the condition of all years between the
    current apportionment year and the last time the June 1 elevation was above 1593.8 feet
    were all above 1593.8 feet.

    Futher example:
    Starting apportionment year: 2020
    June1, 2020 Lake Darling elevation: 1596.5 feet
        Return True because 1596.5 > 1594.8.
    """
    NGVD29_OFFSET = 1500  # Gage height is quesied directly then converted to NGVD29.

    if june1_elev > elev_upper_limit:
        return True

    year -= 1
    nwis_service = serv.NWISWaterService(service="dv")
    while june1_elev > elev_lower_limit:
        #  2023 met criteria, but prior data housed elsewhere so just return True.
        if year <= 2023:
            return True
        lake_darling = nwis_service.get(
            dict(
                sites="05115500",
                startDt=f"{year}-06-01",
                endDt=f"{year}-06-01",
                parameterCd="00065",  # Gage height (ft))
            )
        )
        lake_darling["value"] = lake_darling["value"] + NGVD29_OFFSET

        if lake_darling.empty:
            return False

        june1_elev_loc = lake_darling.loc[f"{year}-06-01"]

        june1_elev = june1_elev_loc["value"]
        if june1_elev > elev_lower_limit:
            if june1_elev > elev_upper_limit:
                return True
            year -= 1
            continue

        return False
    return False
