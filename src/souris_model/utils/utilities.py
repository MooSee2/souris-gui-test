from typing import Union

import numpy as np
import pandas as pd
from loguru import logger


def rename_monthly_index(data: Union[pd.Series, pd.DataFrame]) -> Union[pd.Series, pd.DataFrame]:
    """Calculate monthly values of a datetime indexed pandas Series

    Parameters
    ----------
    dataframe : pd.Series
        Series to calculate monthly values with

    Returns
    -------
    pd.Series
        Series of monthly values.  Index returned in the format yyyy-mm. e.g. January = 2022-1, February = 2022-2...
    """
    if isinstance(data, pd.DataFrame):
        return data.set_index(data.index.strftime("%Y-%m"))  # type: ignore
    if isinstance(data, pd.Series):
        data.index = data.index.strftime("%Y-%m")  # type: ignore
        return data


def check_nan_gaps(
    data: pd.DataFrame,
    staid: str,
) -> pd.DatetimeIndex:
    """Checks for nan values in first column and returns DateTimeIndex of missing values.

    Parameters
    ----------
    data : pd.DataFrame
        DateTimeIndex'ed DataFrame

    Returns
    -------
    DateTimeIndex
        DateTimeIndex of missing values
    """
    mask = data.iloc[:, 0].isna()
    return pd.DataFrame({f"{staid}_gap_dates": data[mask].index})


def issue_gap_warning(data: dict, freq: str) -> None:
    for station, gaps in data.items():
        if not gaps.empty:
            logger.warning(f"Warning: Data gaps found at {station}  Freq: {freq}")
    return


def join_data(data: dict) -> pd.DataFrame:
    joined_df = pd.DataFrame()
    for item in data:
        joined_df.join(item)
    return joined_df


def penman(
    df: pd.DataFrame,
    wind: str,
    temp: str,
    rel_hum: str,
    rad: str,
    ELEV: int,
) -> pd.DataFrame:
    """Returns the Penman calculation.

    Parameters
    ----------
    wind : pd.Series
        Units: m/s
    temp : pd.Series
        Units: C
    rel_hum : pd.Series
        Units: W/m2
    rad : pd.Series
        Units: MJ/m2
    ELEV : int
        Units: meters

    Returns
    -------
    pd.DataFrame

    Notes
    -----

    """
    # ANNEMOMETER_HEIGHT = 3
    df = df.copy()

    # wind speed [km/h] from wind speed [m/s]
    # df["daily_wind"] = df[wind].mul(4.544759748970231)

    # latent heat of vaporization of water [cal/g] from temperature [C]
    df["latent_heat"] = df[temp].mul(0.556).rsub(597.3)

    # saturated vapor pressure [mb] from temperature [C]
    df["sat_vapor"] = np.exp((df[temp].mul(17.26)).div((df[temp].add(237.3)))).rmul(6.11)

    # radiation [MJ/m2] from radiation [W/m2]
    df["daily_rad"] = df[rad].mul(0.0864)

    # pressure [mb] from elevation [m]
    df["atm_pressure"] = 1013.25 * (1 - 0.0000225577 * ELEV) ** 5.25588

    # dewpoint temperautre [C] from relative humidity and temperature [C]
    df["daily_dew"] = ((np.log(df[rel_hum].div(100)).add(df[temp].mul(17.27).div(df[temp].add(237.3)))).rdiv(17.27).sub(1)).rdiv(237.3)

    # dewpoint vapor pressure [mb] from temperature [C]
    df["vap_pressure"] = np.exp((df["daily_dew"].mul(17.26)).div(df["daily_dew"].add(237.3))).mul(6.11)

    # wind corrected to a height of 7.6 m above the ground [km/h] from wind [km/h] and
    # annemometer height [m] (set to 3 m as that's ECCC and USGS standard)
    df["adj_wind"] = df[wind].mul(4.544759748970231)

    # rate of change of vapor pressure at temp [mb/C] from latent heat of vaporization [cal/g],
    # saturated vapor pressure [mb], and temp [C]
    df["vapor_change"] = df["latent_heat"].mul(18.02).mul(df["sat_vapor"]).div(1.9872).div(df[temp].add(273.16).pow(2))

    # net radiation in units of evap [mm] from radiation [MJ/m2] and latent heat of vaporization of water [cal/g]
    df["net_rad"] = df["daily_rad"].mul(238.95).div(df["latent_heat"])

    # psychrometric constant [mb/C] from pressure [mb] and latent heat of vaporization of water [cal/g]
    df["gamma"] = df["atm_pressure"].mul(0.24).div(0.622).div(df["latent_heat"])

    # aerodynamic estimate of evaporation [mm] from saturated vapor pressure [mb], dewpoint vapor pressure [mb],
    # corrected wind [km/h], and elevation [m]
    df["Ea"] = (df["sat_vapor"].sub(df["vap_pressure"])).mul(10.1 / 30.4).mul(df["adj_wind"].mul(0.062139).add(1)).mul(1 + 0.0000328084 * ELEV)

    # Penman evaporation [mm] from vapor pressure change at temp [mb/C], net radiation in evap [mm], psychrometric
    # constant [mb/C], and aerodynamic evaporation [mm]
    df["penman"] = (df["vapor_change"].mul(df["net_rad"]).add(df["gamma"].mul(df["Ea"]))).div(df["vapor_change"].add(df["gamma"]))
    return df[["penman"]]


def debug_boxes_df(data: dict) -> pd.DataFrame:
    drop_list = (
        "box4",
        "box7",
        "box11",
        "box12",
        "box16",
        "box18",
        "box25",
        "box27",
        "box28",
        "box29",
        "box37",
        "box43",
    )
    data = {box: value for box, value in data.items() if box not in drop_list}
    df = pd.DataFrame(data.items(), columns=["box_num", "value_dam3"])
    df.replace({"box_num": "box47a"}, "box47", inplace=True)
    return df
