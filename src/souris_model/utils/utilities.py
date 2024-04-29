import functools
from pathlib import Path
from typing import Union

import numpy as np
import pandas as pd
from loguru import logger


def logger_wraps(*, entry=True, exit=True, level="DEBUG"):
    """Function decorator to log function information

    Parameters
    ----------
    entry : bool, optional
        _description_, by default True
    exit : bool, optional
        _description_, by default True
    level : str, optional
        _description_, by default "DEBUG"
    """

    def wrapper(func):
        name = func.__name__

        @functools.wraps(func)
        def wrapped(*args, **kwargs):
            logger_ = logger.opt(depth=1)
            if entry:
                logger_.log(level, "Entering '{}' (args={}, kwargs={})", name, args, kwargs)
            result = func(*args, **kwargs)
            if exit:
                logger_.log(level, "Exiting '{}' (result={})", name, result)
            return result

        return wrapped

    return wrapper


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
    dataframe: pd.DataFrame,
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
    ANNEMOMETER_HEIGHT = 3
    dataframe = dataframe.copy()

    # wind speed [km/h] from wind speed [m/s]
    dataframe["daily_wind"] = dataframe[wind] * 3.6

    # latent heat of vaporization of water [cal/g] from temperature [C]
    dataframe["latent_heat"] = 597.3 - 0.566 * dataframe[temp]

    # saturated vapor pressure [mb] from temperature [C]
    dataframe["sat_vapor"] = 6.11 * np.exp((17.26 * dataframe[temp]) / (dataframe[temp] + 237.3))

    # radiation [MJ/m2] from radiation [W/m2]
    dataframe["daily_rad"] = dataframe[rad] * 0.0864

    # pressure [mb] from elevation [m]
    dataframe["atm_pressure"] = 1013.25 * (1 - 0.0000225577 * ELEV) ** 5.25588

    # dewpoint temperautre [C] from relative humidity and temperature [C]
    dataframe["daily_dew"] = 237.3 / (17.27 / (np.log(dataframe[rel_hum] / 100) + 17.27 * dataframe[temp] / (237.3 + dataframe[temp])) - 1)

    # dewpoint vapor pressure [mb] from temperature [C]
    dataframe["vap_pressure"] = 6.11 * (np.exp((17.26 * dataframe["daily_dew"]) / (dataframe["daily_dew"] + 237.3)))

    # wind corrected to a height of 7.6 m above the ground [km/h] from wind [km/h] and
    # annemometer height [m] (set to 3 m as that's ECCC and USGS standard)
    dataframe["adj_wind"] = dataframe["daily_wind"] * (7.62 / ANNEMOMETER_HEIGHT) ** 0.25

    # rate of change of vapor pressure at temp [mb/C] from latent hear of vaporization [cal/g],
    # saturated vapor pressure [mb], and temp [C]
    dataframe["vapor_change"] = 18.02 * dataframe["latent_heat"] * dataframe["sat_vapor"] / 1.9872 / (273.16 + dataframe[temp]) ** 2

    # net radiation in units of evap [mm] from radiation [MJ/m2] and latent heat of vaporization of water [cal/g]
    dataframe["net_rad"] = 238.95 * dataframe["daily_rad"] / dataframe["latent_heat"]

    # psychrometric constant [mb/C] from pressure [mb] and latent heat of vaporization of water [cal/g]
    dataframe["gamma"] = 0.24 * dataframe["atm_pressure"] / 0.622 / dataframe["latent_heat"]

    # aerodynamic estimate of evaporation [mm] from saturated vapor pressure [mb], dewpoint vapor pressure [mb],
    # corrected wind [km/h], and elevation [m]
    dataframe["Ea"] = 10.1 / 30.4 * (dataframe["sat_vapor"] - dataframe["vap_pressure"]) * (1 + 0.062139 * dataframe["adj_wind"]) * (1 + 0.0000328084 * ELEV)

    # Penman evaporation [mm] from vapor pressure change at temp [mb/C], net radiation in evap [mm], psychrometric
    # constant [mb/C], and aerodynamic evaporation [mm]
    dataframe["penman"] = (dataframe["vapor_change"] * dataframe["net_rad"] + dataframe["gamma"] * dataframe["Ea"]) / (dataframe["vapor_change"] + dataframe["gamma"])
    return dataframe[["penman"]]


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
