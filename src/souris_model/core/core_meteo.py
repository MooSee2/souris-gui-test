import pandas as pd

import src.souris_model.core.dates as dates
import souris_model.utils.utilities as util

"""
    # -----------------------------------------------------------------------------------------#
    #                               Meteo Data processing                                      #
    #                              05NB016, 05NCM01, Oxbow                                     #
    # -----------------------------------------------------------------------------------------#
    # Roughbark: 05NB016
    # Handsworth: 05NCM01
    # Monthly precipitation is determined by summing all of the precipitation that
    # occurred over the associated month
    # Units are downloaded in mm
    # Oxbow data comes through as daily values from climate.weather.gc.ca.
    # Missing days from Oxbow are indexed with values = NaN by default
    Meteo data is only available on caaq servers.  No public data yet.
    Old python: Roughbark meteo as 05NB016
    excel: Roughbark meteo as 05NBM01
    The Souris manual labels Roughbark meteo station as 05NBM01
    and Roughbark reservoir level is 05NB016
"""
MM_TO_METERS = 0.001


def process_instant_meteo(
    dates: dates.Dates,
    roughbark_instant: dict,
    handsworth_instant: dict,
) -> tuple:
    # Drop Approval cols, don't need'em.
    roughbark_meteo_instant = {staid: dataframe.drop(columns=["approval"]) for staid, dataframe in roughbark_instant.items()}
    handsworth_meteo_instant = {staid: dataframe.drop(columns=["approval"]) for staid, dataframe in handsworth_instant.items()}

    # Resample to daily values
    # Pop precip data, it get's resampled differently
    roughbark_precip_daily = roughbark_meteo_instant.pop("05NB016_precip").select_dtypes("number").resample("D", origin=f"{dates.wateryear}-01-01").sum()
    handsworth_precip_daily = handsworth_meteo_instant.pop("05NCM01_precip").select_dtypes("number").resample("D", origin=f"{dates.wateryear}-01-01").sum()

    precip_daily = {
        "05NB016_precip": roughbark_precip_daily,
        "05NCM01_precip": handsworth_precip_daily,
    }

    roughbark_meteo_daily = {staid: dataframe.select_dtypes("number").resample("D", origin=f"{dates.wateryear}-01-01").mean().round(3) for staid, dataframe in roughbark_meteo_instant.items()}
    handsworth_meteo_daily = {staid: dataframe.select_dtypes("number").resample("D", origin=f"{dates.wateryear}-01-01").mean().round(3) for staid, dataframe in handsworth_meteo_instant.items()}

    roughbark_meteo_daily = {
        staid: util.fill_gaps_nan(
            dataframe=dataframe,
            start_date=dates.start_pull,
            end_date=dates.end_pull,
            freq="D",
        )
        for staid, dataframe in roughbark_meteo_daily.items()
    }
    handsworth_meteo_daily = {
        staid: util.fill_gaps_nan(
            dataframe=dataframe,
            start_date=dates.start_pull,
            end_date=dates.end_pull,
            freq="D",
        )
        for staid, dataframe in handsworth_meteo_daily.items()
    }

    roughbark_meteo_daily = {staid: dataframe.rename(columns={"value": f"{staid}"}) for staid, dataframe in roughbark_meteo_daily.items()}
    handsworth_meteo_daily = {staid: dataframe.rename(columns={"value": f"{staid}"}) for staid, dataframe in handsworth_meteo_daily.items()}

    return precip_daily, roughbark_meteo_daily, handsworth_meteo_daily


def process_penman(
    dates: dates.Dates,
    roughbark_meteo_daily: pd.DataFrame,
    handsworth_meteo_daily: pd.DataFrame,
) -> tuple:
    # -----------------------------------------------------------------------------------------#
    #                                    Penman Calculations                                   #
    # -----------------------------------------------------------------------------------------#
    # Perform the penman calculation for both the Roughbark and Handsworth stations
    # Monthly evaporation is determined by summing the daily averages for the associated month
    roughbark_penman_daily = util.penman(
        dataframe=roughbark_meteo_daily,
        wind="05NB016_wind_speed",
        temp="05NB016_air_temp",
        rel_hum="05NB016_rel_humidity",
        rad="05NB016_sol_rad",
        ELEV=567,
    )
    handsworth_penman_daily = util.penman(
        dataframe=handsworth_meteo_daily,
        wind="05NCM01_wind_speed",
        temp="05NCM01_air_temp",
        rel_hum="05NCM01_rel_humidity",
        rad="05NCM01_sol_rad",
        ELEV=682,
    )
    roughbark_meteo_daily = roughbark_meteo_daily.join(roughbark_penman_daily)
    handsworth_meteo_daily = handsworth_meteo_daily.join(handsworth_penman_daily)

    # For January, February, March, November, and December:
    # evaporation is considered negligible due to cold weather and general ice cover

    handsworth_meteo_daily.loc[handsworth_meteo_daily.index.month.isin([11, 12]), "penman"] = 0
    roughbark_meteo_daily.loc[roughbark_meteo_daily.index.month.isin([11, 12]), "penman"] = 0

    roughbark_meteo_daily.loc[f"{dates.wateryear}-01-01" : dates.evap_start_date, "penman"] = 0
    handsworth_meteo_daily.loc[f"{dates.wateryear}-01-01" : dates.evap_start_date, "penman"] = 0

    # Calculate monthy sums and convert summation to meters of evaporation
    roughbark_penman_monthly_sum = util.rename_monthly_index(roughbark_meteo_daily[["penman"]].resample("ME").sum())
    handsworth_penman_monthly_sum = util.rename_monthly_index(handsworth_meteo_daily[["penman"]].resample("ME").sum())

    roughbark_meteo_daily = roughbark_meteo_daily * MM_TO_METERS
    handsworth_meteo_daily = handsworth_meteo_daily * MM_TO_METERS
    roughbark_penman_monthly_sum = roughbark_penman_monthly_sum * MM_TO_METERS
    handsworth_penman_monthly_sum = handsworth_penman_monthly_sum * MM_TO_METERS
    return (
        roughbark_penman_monthly_sum,
        handsworth_penman_monthly_sum,
        roughbark_meteo_daily,
        handsworth_meteo_daily,
    )
