import pandas as pd

from modules.data_layer import nwis
from modules.data_layer import wo_realtime as wo
from src.souris_model.souris_main import main


# def get_reservoir_data(apportionment_year: int):
#     wo_realtime_reservoirs = wo.get_wo_realtime_reservoirs(apportionment_year)
#     return wo_realtime_reservoirs


def get_data(
    apportionment_year: int,
    username: str,
    password: str,
):
    # wo_realtime_partner = wo.get_wo_realtime_partner_met(apportionment_year)
    nwis_discharge = nwis.get_nwis_data(apportionment_year)
    wo_realtime_discharge = wo.get_wo_realtime_public_discharge(apportionment_year)
    wo_realtime_reservoirs = wo.get_wo_realtime_public_reservoirs(apportionment_year)
    return pd.concat([wo_realtime_discharge, nwis_discharge], axis=1), wo_realtime_reservoirs


def run_main(model_inputs):
    # Wrapper function for main app
    return main(model_inputs)
