from time import sleep

import pandas as pd

import app_data.test_data as td
from modules.data_layer import nwis
from modules.data_layer import wo_realtime as wo
from souris.scripts.souris_main import main


def get_reservoir_data(apportionment_year: int):
    wo_realtime_reservoirs = wo.get_wo_realtime_reservoirs(apportionment_year)
    return wo_realtime_reservoirs


def get_discharge_data(apportionment_year: int):
    nwis_discharge = nwis.get_nwis_data(apportionment_year)
    wo_realtime_discharge = wo.get_wo_realtime_discharge(apportionment_year)
    return pd.concat([wo_realtime_discharge, nwis_discharge], axis=1)


def run_main(model_inputs):
    # Wrapper function for main app
    return main(model_inputs)
