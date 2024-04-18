import datetime as dt
from dataclasses import dataclass

ACREFT_TO_CFSDay = 0.504166666666665
CFSDay_TO_DAM3Day: float = 2.4465755455488
CMS_TO_CFS: float = 35.3146667214886
MM_TO_INCHES = 25.4
USGS_PCODE_CFS: str = "00060"
USGS_PCODE_CMS: str = "30208"
USGS_PCODE_ELEV_FT: str = "62614"
USGS_STAT_CODE_DAILY_MEAN: str = "00003"
USGS_STAT_CODE_OBS_AT_2400: str = "32400"


@dataclass
class Boxes:
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


@dataclass(frozen=True)
class Dates:
    wateryear: int
    start_apportion: str
    end_apportion: str
    evap_start_date: str
    evap_end_date: str
    _now = dt.datetime.now()
    now = _now.strftime("%Y%m%d%H%M")
    today = _now.strftime("%Y-%m-%d")
