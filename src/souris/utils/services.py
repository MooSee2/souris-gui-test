import asyncio
import copy
import json
from io import StringIO
from typing import Union

import aiohttp
import pandas as pd
import requests

_UTC_neg7_stations = [
    "05AE036",
    "05AE029",
    "05AE027",
    "11AA032",
    "11AA031",
    "11AA001",
    "11AA025",
    "11AA005",
]


def is_iterable(obj):
    try:
        iter(obj)
        return True
    except TypeError:
        return False


class NWISWaterService:
    def __init__(
        self,
        service: str,
        freq: Union[str, None] = None,
    ) -> None:
        self._url = f"https://waterservices.usgs.gov/nwis/{service}"
        self._freq = freq

    def _get(self, params: dict) -> None:
        if "sites" in params and is_iterable(params["sites"]):
            params["sites"] = ",".join(params["sites"])

        response = requests.get(
            self._url,
            params=params,
            headers={"user-agent": "python"},
        )

        if response.status_code >= 200 and response.status_code <= 299:
            return response.json()
        raise Exception(f"Error: {response.url}")

    def load_json(
        self,
        local_path: str = "tests/test_data/test_data_12323233_discharge.json",
    ):
        with open(local_path, "r") as f:
            return json.load(f)

    def parse_method_id(self, method_field):
        if "Provisional" in method_field:
            return "_provisional"
        if "Furnished" in method_field:
            return "_furnished"
        return ""

    def remove_nwis_mask(self, df: pd.DataFrame) -> pd.DataFrame:
        df.loc[df["value"] == -999999.0, "value"] = float("NaN")
        return df

    def parse_nwis_json(self, data) -> list:
        """Parse json data from nwis into a dictionary of
        stations mapped to a list of dicts of their data.

        Parameters
        ----------
        data : json
            json data from nwis.

        Returns
        -------
        dict
            Station ID number: list of data dicts.
        """
        parsed_data = {}
        for series in data["value"]["timeSeries"]:
            staid = series["sourceInfo"]["siteCode"][0]["value"]
            for value in series["values"]:
                method_field = value["method"][0]["methodDescription"]
                method = self.parse_method_id(method_field=method_field)
                parsed_data[f"{staid}{method}"] = [
                    {
                        "datetime": point["dateTime"],
                        "value": (float(point["value"]) if point["value"] != "-999999.0" else float("NaN")),
                        "qualifiers": point["qualifiers"],
                    }
                    for point in value["value"]
                ]
        return parsed_data

    def nwis_to_dataframes(self, data: dict, params: dict) -> dict:
        dfs = {staid: pd.DataFrame(df) for staid, df in data.items()}
        dfs = {staid: df.set_index(pd.DatetimeIndex(df["datetime"])) for staid, df in dfs.items() if not df.empty}
        dfs = {staid: df.drop(["datetime"], axis=1) for staid, df in dfs.items()}
        dfs = {staid: self.remove_nwis_mask(df) for staid, df in dfs.items()}

        if params.get("startDt") and params.get("endDt") and self._freq:
            idx = pd.date_range(
                start=params["startDt"],
                end=params["endDt"],
                freq=self._freq,
            )
            dfs = {staid: df.reindex(idx) for staid, df in dfs.items()}
        return dfs

    def get(self, params: dict) -> dict[str, pd.DataFrame]:
        data = self._get(params=params)
        data = self.parse_nwis_json(data)
        data = self.nwis_to_dataframes(data, params)
        return data


class NWISWaterData:
    def __init__(
        self,
        service: str,
        freq: Union[str, None] = None,
    ) -> None:
        self._url = f"https://nwis.waterdata.usgs.gov/usa/nwis/{service}"
        self._freq = freq

    def _get(self, params: dict) -> None:
        if isinstance(params["parameterCd"], list):
            paramcds = params["parameterCd"]
            params |= {f"cb_{paramcd}": "on" for paramcd in paramcds}

        r = requests.Request(
            "get",
            self._url,
            params=params,
            headers={"user-agent": "python"},
        )
        url = r.prepare().url
        return self.get_nwis_rdb(url)

    def get_nwis_rdb(self, url: str) -> pd.DataFrame:
        df = pd.read_csv(url, comment="#", delimiter="\t", skiprows=31)
        df = df.loc[1:,]  # first row is garbage data always
        return df

    def _parse_nwis_rdb_helper(self, df: pd.DataFrame, params: dict) -> pd.DataFrame:
        df["datetime"] = pd.to_datetime(df["datetime"])
        df = df.set_index(pd.DatetimeIndex(df["datetime"]))
        df = df.drop(columns=["agency_cd", "datetime"])

        if all([params.get("begin_date"), params.get("end_date"), self._freq]):
            idx = pd.date_range(start=params["begin_date"], end=params["end_date"], freq=self._freq)
            df = df.reindex(idx)
        df = df.apply(pd.to_numeric, errors="ignore")
        return df

    def load_rdb(
        self,
        local_path: str = "tests/test_data/485831110252101_met_data.rdb",
    ):
        df = pd.read_csv(local_path, comment="#", delimiter="\t", skiprows=31)
        return df.loc[1:,]  # first row is garbage data always

    def get(self, params: dict, local_data: bool = False) -> dict[str, pd.DataFrame]:
        data = self.load_rdb() if local_data else self._get(params=params)
        data = self._parse_nwis_rdb_helper(data, params)
        data = {params["site_no"]: data}
        return data


class WaterOfficeRealTime:
    """
    https://wateroffice.ec.gc.ca/services/links_e.html
    Returns instantaneous data, usually 5 minute freq.

    """

    def __init__(
        self,
        freq: Union[str, None] = None,
        **_,
    ) -> None:
        self._url = "https://wateroffice.ec.gc.ca/services/real_time_data/csv/inline?"
        self._freq = freq

    def add_time_suffix(self, params: dict):
        start = params.pop("start_date")
        end = params.pop("end_date")

        params["start_date"] = (pd.to_datetime(start) + pd.offsets.Hour(6)).strftime("%Y-%m-%d %X")
        params["end_date"] = (pd.to_datetime(end) + pd.offsets.Hour(6)).strftime("%Y-%m-%d %X")
        return params

    def _get(self, params: dict) -> str:
        """Download station time-series data from WaterOffice API.

        Parameters
        ----------

        Returns
        -------

        Notes
        -----
        Dates sent to the WaterOffice API are assumed to be UTC+00:00
        """
        response = requests.get(
            url=self._url,
            params=params,
            headers={"user-agent": "python"},
        )
        return response.text

    def _df_process_helper(self, df: pd.DataFrame) -> pd.DataFrame:
        """Helper function for processing dataframes from WaterOffice

        Parameters
        ----------
        df : pd.DataFrame
            pandas DataFrame of time-series data

        Returns
        -------
        pd.DataFrame
            Processed DataFrame.

        Notes
        -----
        The timestamp data comes with a UTC offset of 0 and is represented by a "Z"
        This is accounted for by tz_convert(None) and subtracting 6 hours to get to MST.
        """
        TZ_OFFSET = -6  # -6 for CST
        #  No mistake, the ID column has a leading space.
        col_names = {
            " ID": "staid",
            "Date": "datetime",
            "Parameter/Paramètre": "parameter",
            "Value/Valeur": "value",
            "Qualifier/Qualificatif": "qualifiers",
            "Symbol/Symbole": "symbol",
            "Approval/Approbation": "approval",
        }
        df = df.rename(columns=col_names)
        df["datetime"] = pd.to_datetime(df["datetime"])
        df["datetime"] = df["datetime"] + pd.offsets.Hour(TZ_OFFSET)
        df["datetime"] = df["datetime"].dt.tz_localize(None)
        df["approval"] = df["approval"].replace(["Final/Finales"], "Final")
        df["approval"] = df["approval"].replace(["Provisional/Provisoire"], "Provisional")
        return df

    def _process_wateroffice_dataframes(self, stations: list, params: dict) -> list:
        """Take in list of DataFrames and process them into time-series data

        Parameters
        ----------
        stations : list
            List of Pandas DataFrames.

        Returns
        -------
        list
            List of processed Pandas DataFrames.
        """
        df = pd.read_csv(StringIO(stations))
        df = self._df_process_helper(df)
        dfs = dict(iter(df.groupby("staid")))
        dfs = {staid: df.set_index(pd.DatetimeIndex(df["datetime"])) for staid, df in dfs.items() if not df.empty}

        if all([params.get("start_date"), params.get("end_date"), self._freq]):
            idx = pd.date_range(start=params["start_date"], end=params["end_date"], freq=self._freq)
            return_dfs = {}
            for staid, df in dfs.items():
                df = df.drop(["datetime"], axis=1)
                df = df.reindex(idx, fill_value=float("NaN"))
                df.index.name = "datetime"
                return_dfs[staid] = df

            return return_dfs
        return dfs

    def get(self, params: dict) -> dict[str, pd.DataFrame]:
        params = self.add_time_suffix(params)
        data = self._get(params=params)
        return self._process_wateroffice_dataframes(data, params)


class MESOnet:
    """Get mesonet data, only supports gildford for specific elements at the moment.
    refactor later to generalize renaming of the columns.  Maybe remove from function.
    """

    def __init__(
        self,
        freq: Union[str, None] = None,
        **_,
    ) -> None:
        self._url = "https://mesonet.climate.umt.edu/api/v2/observations/daily/"
        self._freq = freq

    def _process_gilford_dataframes(self, results: list, params: dict) -> pd.DataFrame:
        dataframes = [pd.DataFrame(data) for data in results]
        dataframes = [df.set_index(pd.DatetimeIndex(df["datetime"])) for df in dataframes]
        dataframes = [df.drop(["datetime", "station"], axis=1) for df in dataframes]
        dataframe = pd.concat(dataframes, axis=1)
        dataframe = dataframe.rename(
            {
                "Average Precipitation [mm]": "precip",
                "Average Relative Humidity [%]": "rel_hum",
                "Average Wind Speed @ 8 ft [m/s]": "wind_speed",
                "Average Solar Radiation [W/m²]": "sol_rad",
                "Average Air Temperature @ 8 ft [°C]": "air_temp",
            },
            axis=1,
        )
        dataframe = dataframe.add_prefix("mdagildf_")
        if all([params.get("begin_date"), params.get("end_date"), self._freq]):
            idx = pd.date_range(start=params["begin_date"], end=params["end_date"], freq=self._freq)
            df = df.reindex(idx)
        return dataframe

    async def _download_gilford(self, element: str, params: dict):
        async with aiohttp.ClientSession() as session:
            query_params = copy.deepcopy(params)
            query_params["elements"] = element
            async with session.get(self._url, params=query_params) as response:
                if response.status == 200:
                    return await response.json()
                print(f"Error: {response.status}")
                return None

    async def get(self, elements: list, params: dict) -> pd.DataFrame:
        tasks = [
            self._download_gilford(
                element,
                params,
            )
            for element in elements
        ]
        results = await asyncio.gather(*tasks)
        return self._process_gilford_dataframes(results, params)
