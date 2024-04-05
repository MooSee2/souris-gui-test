from src.app_data.test_data import make_df_copies, make_dummy_data
import pandas as pd


def test_make_df_copies():
    input_data = {
        "05NA006",
        "05NB020",
        "05NB016",
        "05NC002",
        "05ND012",
    }

    output = make_df_copies(stations=input_data)
    assert len(output) == 5


def test_make_reservoirs():
    combined_dfs = make_dummy_data()
    assert not combined_dfs.empty
    assert len(combined_dfs) == 1728
    assert len(combined_dfs.columns) == 15


