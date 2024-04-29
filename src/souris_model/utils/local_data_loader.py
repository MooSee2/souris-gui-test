from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, Optional, Union

import pandas as pd


@dataclass
class LocalExcel:
    data: pd.DataFrame
    approval: Optional[dict]
    source: Optional[dict]
    units: Optional[dict]
    ca_reservoir_stations: tuple = (
        "05NA006",
        "05NB020",
        "05NB016",
        "05NC002",
        "05ND012",
    )
    ca_discharge_stations: tuple = (
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
    precip_columns: tuple = (
        "05NB016_precip",
        "05NCM01_precip",
        "oxbow_precip",
    )
    roughbark_meteo_columns: tuple = (
        "05NB016_wind_speed",
        "05NB016_temperature",
        "05NB016_rel_humidity",
        "05NB016_radiation",
    )
    handsworth_meteo_columns: tuple = (
        "05NCM01_wind_speed",
        "05NCM01_temperature",
        "05NCM01_rel_humidity",
        "05NCM01_radiation",
    )

    @staticmethod
    def _drop_nans(df: pd.DataFrame) -> tuple:
        df = df.dropna(axis=1, how="all")
        return df.dropna(axis=0, how="all")

    @staticmethod
    def _process_excel(df: pd.DataFrame, units: dict) -> pd.DataFrame:
        """Process input excel data.  ft3/s is converted to m3/s

        Parameters
        ----------
        df : pd.DataFrame
            pd.DataFrame of excel data.
        units : dict
            Units from excel in the form of a dictionary staid" units

        Returns
        -------
        pd.DataFrame
            Processed override data ready to use.
        """
        CFS_TO_CMS = 0.0283168
        df.rename(columns={"Station_ID": "datetime"}, inplace=True)
        # drop any rows that don't have a datetime.
        df = df[df["datetime"].notna()]
        df["datetime"] = pd.to_datetime(df["datetime"])
        df.set_index("datetime", inplace=True)

        for staid, unit in units.items():
            df[staid] = df[staid] * CFS_TO_CMS if unit == "ft3/s" else df[staid]

        # drop columns and rows is all values in col or row are nan.
        df = df.dropna(axis=1, how="all")
        df = df.dropna(axis=0, how="all")
        return df

    @classmethod
    def load_excel(cls, filepath: Union[Path, str]) -> LocalExcel:
        df = pd.read_excel(filepath, engine="openpyxl", sheet_name="data")

        # Access metadata in excel. Row 1 = approvals, 2 = source, 3 = units
        metadata = (df.iloc[1].to_dict(), df.iloc[1].to_dict(), df.iloc[3].to_dict())
        for data in metadata:
            del data["Station_ID"]

        approval, source, units = metadata

        # Time-series data starts at row 4 in DataFrame but is row 6 in Excel.
        df = cls._process_excel(df.iloc[4:].copy(), units=units)
        df = df.astype(float)
        return LocalExcel(df, approval, source, units)

    def _process_met_data(self) -> tuple:
        roughbark_meteo_daily = {staid: self.data[[staid]].copy() for staid in self.data.columns if staid in self.roughbark_meteo_columns}

        handsworth_meteo_daily = {staid: self.data[[staid]].copy() for staid in self.data.columns if staid in self.handsworth_meteo_columns}
        return roughbark_meteo_daily, handsworth_meteo_daily

    def to_dicts(
        self,
    ) -> tuple[dict, dict, dict, dict, dict]:
        """
        Need to return:
        precip_daily,
        discharge_daily,
        reservoir_elevation_daily,
        roughbark_meteo_daily,
        handsworth_meteo_daily,

        column names must line up with what's in excel template.
        """

        reservoir_elevation_daily = {staid: self.data[[staid]].copy() for staid in self.data.columns if staid in self.ca_reservoir_stations}
        reservoir_elevation_daily = {staid: df.rename(columns={staid: "value"}) for staid, df in reservoir_elevation_daily.items()}

        discharge_daily = {staid: self.data[[staid]].copy() for staid in self.data.columns if staid in self.ca_discharge_stations}

        if "05114000" in self.data.columns:
            discharge_daily["05114000"] = self.data[["05114000"]].copy()
        if "05113600" in self.data.columns:
            discharge_daily["05113600"] = self.data[["05113600"]].copy()

        discharge_daily = {staid: df.rename(columns={staid: "value"}) for staid, df in discharge_daily.items()}

        precip_daily = {staid: self.data[[staid]].copy() for staid in self.data.columns if staid in self.precip_columns}
        precip_daily = {staid: df.rename(columns={staid: "value"}) for staid, df in precip_daily.items()}

        roughbark_meteo_daily, handsworth_meteo_daily = self._process_met_data()

        return (
            discharge_daily,
            reservoir_elevation_daily,
            precip_daily,
            roughbark_meteo_daily,
            handsworth_meteo_daily,
        )

    def to_override_dicts(self):
        (
            discharge_daily,
            reservoir_elevation_daily,
            precip_daily,
            roughbark_meteo_daily,
            handsworth_meteo_daily,
        ) = self.to_dicts()

        discharge_daily = {staid: self._drop_nans(df) for staid, df in discharge_daily.items()}

        reservoir_elevation_daily = {staid: self._drop_nans(df) for staid, df in reservoir_elevation_daily.items()}

        precip_daily = {staid: self._drop_nans(df) for staid, df in precip_daily.items()}

        roughbark_meteo_daily = {staid: self._drop_nans(df) for staid, df in roughbark_meteo_daily.items()}

        handsworth_meteo_daily = {staid: self._drop_nans(df) for staid, df in handsworth_meteo_daily.items()}

        return (
            discharge_daily,
            reservoir_elevation_daily,
            precip_daily,
            roughbark_meteo_daily,
            handsworth_meteo_daily,
        )
