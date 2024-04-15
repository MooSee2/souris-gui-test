import base64
import json
from datetime import datetime, timedelta
from io import StringIO

import defusedxml.ElementTree as ET
import pandas as pd
import requests
from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA
from requests import Session


def caaq_login(
    user: str,
    password: str,
) -> Session:
    """Establish connection to query AQ data

    Parameters
    ----------
    credential_ini : str, optional
        Path to secrets.ini file that contains login info.

    Returns
    -------
    Session
        requests session object for CA AQ servers

    Notes
    -----
    ini format:
    [credentials]
    user = xxx
    password = yyy

    ******* NEVER PASS verify=False to a request!!!! *******
    verify=False DISABLES SSL certification.  That is a huge security vulnerability.

    """
    aq_base_url = "https://wsc.aquaticinformatics.net:443/AQUARIUS/Publish/v2/"

    # Get AQ public key
    url = f"{aq_base_url}session/publickey"
    try:
        response = requests.get(url)
    except requests.exceptions.SSLError as e:
        print("SSL Error. Possible solutions:\n" "1) If you are connected to a VPN or on a private network (in an office), provide the SSL Intercept Certificate.\n 2) Disconnect from the VPN.\n")
        raise SystemExit from e

    data = json.loads(response.text)["Xml"]

    # Generate encrypted RSA password from AQ public key
    rsa_password = gen_rsa_password(data, password)

    # Post credentials
    aq_session = requests.Session()
    url = f"{aq_base_url}session"
    aq_session.post(
        url,
        data={"Username": user, "EncryptedPassword": rsa_password},
    )
    return aq_session


def gen_rsa_password(
    aq_pubkey_xml: str,
    password: str,
) -> str:
    """Generate an encrypted base64 password to establish connection with CA AQ servers.

    Parameters
    ----------
    aq_pubkey_xml : str
        The value from the key "Xml" in a response.text that has been converted to a dictionary.
    password : str
        A user password that matches a user login credential.
        Currently the credentials reside in secrets.ini

    Returns
    -------
    str
        base64 utf-8 string representation of the user password.
    """
    ET_RSA = ET.fromstring(aq_pubkey_xml)
    modulus = int.from_bytes(base64.b64decode(ET_RSA[0].text), "big")
    exponent = int.from_bytes(base64.b64decode(ET_RSA[1].text), "big")
    pub_key = RSA.construct((modulus, exponent))

    # Encrypt password to send to AQ
    cipher_rsa = PKCS1_OAEP.new(pub_key)
    rsa_password = cipher_rsa.encrypt(bytes(password, "utf-8"))
    # Convert encrypted password to base 64 for AQ
    return base64.b64encode(rsa_password).decode("utf-8")


def query_ts_uniqueID(
    staid: str,
    prefix: str,
    aq_session: requests.Session,
) -> str:
    # This section queries for the AQ station (staid) for a list of dictionaries
    # of available time-series and searches for the TS unique ID to query for in the next step.
    # The TS identifier is the timeseries_prefix@staid and is tied to a hashed UniqueId field.
    url = "https://wsc.aquaticinformatics.net:443/AQUARIUS/Publish/v2/GetTimeSeriesDescriptionList"
    params = {"LocationIdentifier": staid}
    response = aq_session.get(url, params=params)
    jdata = json.loads(response.text)

    # Find TS unique ID.  Turn this to function.
    for timeseries in jdata["TimeSeriesDescriptions"]:  # list of dicts of TS descriptions
        if timeseries["Identifier"] == f"{prefix}@{staid}":
            return timeseries["UniqueId"]


def get_caaq(
    staid: str,
    start_date: str,
    end_date: str,
    timeseries_prefix: str,
    aq_session: Session,
) -> pd.DataFrame:
    """Downloads time-series data from Canadian AQ and returns a
    DateTimeIndex'ed DataFrame.  Assumes AQ Publish access.

    Parameters
    ----------
    staid : str
        Station ID
    start_date : str
        Start date to pull data.  yyyy-mm-dd format.
    end_date : str
        Start date to pull data.  yyyy-mm-dd format.
    timeseries_prefix : str
        Aquarius time-series prefix, e.g. Discharge.Working
    aq_session : Session
        requests Session connected to caaq servers.
    base_url : str | None
        Base url to query data with. By default, None

    Returns
    -------
    pd.DataFrame
        DateTimeIndex'ed DataFrame.
        Date range begins at 00:00 of start_date and ends on 00:00 of end_date

    Notes
    -----
    Just to be clear about date ranges:
    get_CAAQ(
        staid="05NB001",
        start_date=2022-01-01,
        end_date=2022-04-01,
        timeseries_prefix="Discharge.Working",
    )
    would query the Discharge.Working time-series at 05NB001 and would
    return a dataframe that begins at 2022-01-01 00:00 and
    ends on 2022-04-01 00:00

    real_time public option:  https://wateroffice.ec.gc.ca/services/links_e.html
    """
    BASE_URL = "https://wsc.aquaticinformatics.net:443/AQUARIUS/Publish/v2/"
    time_series_uniqueID = query_ts_uniqueID(
        staid=staid,
        prefix=timeseries_prefix,
        aq_session=aq_session,
    )
    # Data retrieved from AQ begins at 00:00 ends at 18:00 of the end_date as opposed to 00:00
    # We need data until 00:00, so add some buffer time to cover the requested range.
    # I wonder if the +6 has to do with UTC time-zones.  May need to grab the
    # UTC offset from the initial AQ query.
    start_date_6 = datetime.strptime(start_date, "%Y-%m-%d") + timedelta(hours=6)
    end_date_6 = datetime.strptime(end_date, "%Y-%m-%d") + timedelta(hours=6)

    # Get station data
    header = {
        "TimeSeriesUniqueIds": time_series_uniqueID,
        "QueryFrom": start_date_6,
        "QueryTo": end_date_6,
        "UtcOffset": "-6",
    }
    response = aq_session.get(f"{BASE_URL}GetTimeSeriesData?", params=header)
    rdata = response.json()

    # Process data to DataFrame
    dataframe = pd.json_normalize(rdata, ["Points"])
    # dataframe = dataframe.rename(columns={"ApprovalName1": "Approval"})
    dataframe["Timestamp"] = pd.to_datetime(dataframe["Timestamp"].array)
    dataframe.set_index("Timestamp", inplace=True)
    dataframe = dataframe.tz_localize(None)
    dataframe["NumericValue1"] = pd.to_numeric(dataframe["NumericValue1"])
    dataframe = dataframe.rename(columns={"ApprovalName1": "approval", "NumericValue1": "value"})
    return dataframe[["value", "approval"]]


def get_meteo(
    staid: str,
    start_date: str,
    end_date: str,
    aq_session: Session,
) -> dict:
    """Downloads wind speed, radiation, temperature, relative humidity and precipitation
    data from caaq servers and returns them as a dictionary of DataFrames.

    Parameters
    ----------
    staid : str
        Station ID
    start_date : str
        Start date to pull data.  Format as yyyy-mm-dd
    end_date : str
        End date to pull data.  Format as yyyy-mm-dd
    aq_session : Session
        requests Session connected to caaq servers.

    Returns
    -------
    dict
        Dictionary of meteo data wind_speed, radiation, temperature, rel_humidity, precip
    Notes
    -----
    Roughbark: 05NB016
    Handsworth: 05NCM01
    """
    wind_speed = get_caaq(
        staid=staid,
        start_date=start_date,
        end_date=end_date,
        timeseries_prefix="Wind Vel.Telemetry",
        aq_session=aq_session,
    )
    # wind_speed = wind_speed.rename(columns={"NumericValue1": "wind_speed"})
    wind_speed["approval"] = wind_speed["approval"].replace(["Preliminary"], "Provisional")

    radiation = get_caaq(
        staid=staid,
        start_date=start_date,
        end_date=end_date,
        timeseries_prefix="Radiation.Telemetry",
        aq_session=aq_session,
    )
    # radiation = radiation.rename(columns={"NumericValue1": "radiation"})
    radiation["approval"] = radiation["approval"].replace(["Preliminary"], "Provisional")

    temperature = get_caaq(
        staid=staid,
        start_date=start_date,
        end_date=end_date,
        timeseries_prefix="Air Temp.Telemetry",
        aq_session=aq_session,
    )
    # temperature = temperature.rename(columns={"NumericValue1": "temperature"})
    temperature["approval"] = temperature["approval"].replace(["Preliminary"], "Provisional")

    rel_humidity = get_caaq(
        staid=staid,
        start_date=start_date,
        end_date=end_date,
        timeseries_prefix="Rel Humidity.Telemetry",
        aq_session=aq_session,
    )
    # rel_humidity = rel_humidity.rename(columns={"NumericValue1": "rel_humidity"})
    rel_humidity["approval"] = rel_humidity["approval"].replace(["Preliminary"], "Provisional")

    precip = get_caaq(
        staid=staid,
        start_date=start_date,
        end_date=end_date,
        timeseries_prefix="Accumulated Precip.Telemetry",
        aq_session=aq_session,
    )
    # precip = precip.rename(columns={"NumericValue1": f"{staid}_precip"})
    precip["approval"] = precip["approval"].replace(["Preliminary"], "Provisional")

    return {
        f"{staid}_wind_speed": wind_speed,
        f"{staid}_radiation": radiation,
        f"{staid}_temperature": temperature,
        f"{staid}_rel_humidity": rel_humidity,
        f"{staid}_precip": precip,
    }


def get_oxbow(
    start_date: str,
    end_date: str,
) -> pd.DataFrame:
    """Retrieves Oxbow total precipitation data in mm as a
    DateTimeIndex'ed DataFrame.

    Parameters
    ----------
    start_date : str
        Start date to trim DataFrame.  Format as yyyy-mm-dd
    end_date : str
        End date to trim DataFrame.  Format as yyyy-mm-dd

    Returns
    -------
    pd.DataFrame
        DataFrame of daily precipitation values in mm at Oxbow, staid: 2981

    Notes
    -----
    Data is queried by the year, it is necessary to trim the DataFrame to
    the expected date range using the start_date and end_date arguments.
    """
    url = f"https://climate.weather.gc.ca/climate_data/bulk_data_e.html?format=csv&stationID=2981&Year={start_date[:4]}&timeframe=2&submit=Download+Data"

    dataframe = pd.read_csv(url)
    dataframe = dataframe.loc[:, ["Date/Time", "Total Precip (mm)"]]
    dataframe.rename(
        columns={"Date/Time": "Timestamp", "Total Precip (mm)": "NumericValue1"},
        inplace=True,
    )
    dataframe["Timestamp"] = pd.to_datetime(dataframe["Timestamp"].array)
    dataframe.set_index("Timestamp", inplace=True)
    dataframe["NumericValue1"] = pd.to_numeric(dataframe["NumericValue1"])
    dataframe = dataframe.loc[start_date:end_date]
    return dataframe
