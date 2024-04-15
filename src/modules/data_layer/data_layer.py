from time import sleep
import app_data.test_data as td
from modules.data_layer import nwis
from modules.data_layer import wo_realtime as wo


def get_reservoir_data(apportionment_year: int):
    wo_realtime_reservoirs = wo.get_wo_realtime_reservoirs(apportionment_year)
    # nwis_data = nwis.get_nwis_data(apportionment_year)
    return wo_realtime_reservoirs


def get_discharge_data(apportionment_year: int):
    wo_realtime_discharge = wo.get_wo_realtime_discharge(apportionment_year)
    # nwis_data = nwis.get_nwis_data(apportionment_year)
    return wo_realtime_discharge


def run_main(*args):
    sleep(5)
    return None
