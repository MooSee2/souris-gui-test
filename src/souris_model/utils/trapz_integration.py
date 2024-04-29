import pandas as pd


def trap_area(df: pd.DataFrame, column: str) -> pd.DataFrame:
    df["t_diff_seconds"] = df.index.to_series().diff().dt.total_seconds().shift(-1)
    df["area"] = (df[column] + df[column].shift(-1)) * df["t_diff_seconds"] * 0.5
    return df


def calc_daily_values(df: pd.DataFrame, column: str) -> pd.DataFrame:
    df = df.groupby(pd.Grouper(freq="d")).sum()
    df[column] = df["area"].div(df["t_diff_seconds"])
    # Drop last row as NaN
    return df.iloc[:-1]


def daily_value_integration(df: pd.DataFrame, column: str, freq: str) -> pd.DataFrame:
    """Perform trapazoidal integration on a DataFrame with a DateTimeIndex
    to return daily mean values.

    Parameters
    ----------
    df : pd.DataFrame
        Pandas DataFrame
    column : str
        Column of numeric values to integrate.
    freq : str
        The frequency to normalize data to before interpolation and integration.
        Normally this is the original frequency of the data but with mixed frequency data
        the preference is to resample to the lowest frequency.  E.g.: If mixing
        5-minute and 1-hour freqency data, set freq to 1-hour: "h"

    Returns
    -------
    pd.DataFrame
        DateFrame resampled to daily averages.
    """
    df = df.asfreq(freq, fill_value=float("NaN"))
    df = df[[column]].interpolate(method="linear")
    df = trap_area(df, column)
    df = calc_daily_values(df, column)
    return df[[column]]
