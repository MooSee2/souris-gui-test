"""
-*- coding: utf-8 -*-
St Mary-Milk program configuration classes.  Handle app settings and date parsing.
"""

import datetime as dt
from dataclasses import dataclass
from pathlib import Path
from typing import Union

import tomli as toml

ACREFT_TO_CFSDay = 0.504166666666665
CFSDay_TO_DAM3Day: float = 2.4465755455488
CMS_TO_CFS: float = 35.3146667214886
MM_TO_INCHES = 25.4
USGS_PCODE_CFS: str = "00060"
USGS_PCODE_CMS: str = "30208"
USGS_PCODE_ELEV_FT: str = "62614"
USGS_STAT_CODE_DAILY_MEAN: str = "00003"
USGS_STAT_CODE_OBS_AT_2400: str = "32400"


@dataclass  # (frozen=True)
class SourisConfig:
    wateryear: int
    use_local_data_only: bool
    use_gildford_met: bool
    evap_start_date: str
    evap_end_date: str
    box_5b: int
    box_11: int
    box_12: int
    box_16: int
    box_18: int
    box_25: int
    box_27: int
    box_28: int
    box_29: int
    box_37: int
    nwis_access_level: int = 1

    def __post_init__(self):
        self.evap_start_date = f"{self.wateryear}-{self.evap_start_date}"
        self.evap_end_date = f"{self.wateryear}-{self.evap_end_date}"

    @classmethod
    def load_config(cls, cfg_path: Union[str, Path]):
        with open(cfg_path, "rb") as f:
            toml_data = toml.load(f)
        return cls(
            wateryear=toml_data["settings"]["wateryear"],
            use_local_data_only=toml_data["settings"]["use_local_data_only"],
            use_gildford_met=toml_data["settings"]["use_gildford_met"],
            evap_start_date=toml_data["settings"]["evap_start_date"],
            evap_end_date=toml_data["settings"]["evap_end_date"],
            box_5b=toml_data["boxes"]["box_5b_pipeline"],
            box_11=toml_data["boxes"]["box_11_MINOR_PROJECT_DIVERSION"],
            box_12=toml_data["boxes"]["box_12_US_DIVERSION_BETWEEN_EAST_AND_WEST_CROSSING"],
            box_16=toml_data["boxes"]["box_16_CITY_OF_WAYBURN_PUMPAGE"],
            box_18=toml_data["boxes"]["box_18_CITY_OF_WAYBURN_RETURN_FLOW"],
            box_25=toml_data["boxes"]["box_25_MINOR_PROJECT_DIVERSIONS"],
            box_27=toml_data["boxes"]["box_27_CITY_OF_EXTEVAN_NET_PUMPAGE"],
            box_28=toml_data["boxes"]["box_28_SHORT_CREEK_DRIVERS_TO_US"],
            box_29=toml_data["boxes"]["box_29_MINOR_PROJECT_DIVERSIONS"],
            box_37=toml_data["boxes"]["box_37_MINOR_PROJECT_DIVERSIONS"],
        )


@dataclass(frozen=True)
class SourisDates:
    wateryear: int
    now: str = ""
    today: str = ""
    start_pull: str = ""
    end_pull: str = ""
    start_apportion: str = ""
    end_apportion: str = ""
    evap_start_date: str = ""
    evap_end_date: str = ""

    def __post_init__(self):
        """Simple date validation"""
        dt.datetime.strptime(self.now, "%Y%m%d%H%M")
        dt.datetime.strptime(self.today, "%Y-%m-%d")
        dt.datetime.strptime(self.start_pull, "%Y-%m-%d")
        dt.datetime.strptime(self.end_pull, "%Y-%m-%d")
        dt.datetime.strptime(self.start_apportion, "%Y-%m-%d")
        dt.datetime.strptime(self.end_apportion, "%Y-%m-%d")
        dt.datetime.strptime(self.evap_start_date, "%Y-%m-%d")
        dt.datetime.strptime(self.evap_end_date, "%Y-%m-%d")

    @classmethod
    def make_dates(cls, wateryear: int):
        _now = dt.datetime.now()
        now = _now.strftime("%Y%m%d%H%M")
        today = _now.strftime("%Y-%m-%d")

        if wateryear is None:
            wateryear = _now.year

        start_pull = f"{wateryear}-01-01"
        end_pull = f"{wateryear}-12-31"
        start_apportion = f"{wateryear}-03-01"
        end_apportion = f"{wateryear}-10-31"
        evap_start_date = f"{wateryear}-04-01"
        evap_end_date = f"{wateryear}-10-31"

        return cls(
            wateryear=wateryear,
            now=now,
            today=today,
            start_pull=start_pull,
            end_pull=end_pull,
            start_apportion=start_apportion,
            end_apportion=end_apportion,
            evap_start_date=evap_start_date,
            evap_end_date=evap_end_date,
        )
