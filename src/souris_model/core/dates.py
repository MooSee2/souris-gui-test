import datetime as dt
from dataclasses import dataclass
from typing import Optional

ACREFT_TO_CFSDay = 0.504166666666665
CFSDay_TO_DAM3Day: float = 2.4465755455488
CMS_TO_CFS: float = 35.3146667214886
MM_TO_INCHES = 25.4
USGS_PCODE_CFS: str = "00060"
USGS_PCODE_CMS: str = "30208"
USGS_PCODE_ELEV_FT: str = "62614"
USGS_STAT_CODE_DAILY_MEAN: str = "00003"
USGS_STAT_CODE_OBS_AT_2400: str = "32400"


@dataclass(frozen=True)
class Dates:
    """This class houses the dates used in the apportionment program."""

    wateryear: int
    start_apportion: str
    end_apportion: str
    evap_start_date: str
    evap_end_date: str
    _now = dt.datetime.now()
    now = _now.strftime("%Y%m%d%H%M")
    today = _now.strftime("%Y-%m-%d")
