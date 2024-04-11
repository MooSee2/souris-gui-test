import app_data.test_data as td
from modules.data_layer import nwis
from modules.data_layer import wo_realtime as wo


def get_app_data(apportionment_year: int) -> tuple:
    wo_realtime_reservoirs = wo.get_wo_realtime_reservoirs(apportionment_year)
    wo_realtime_discharge = wo.get_wo_realtime_discharge(apportionment_year)
    nwis_data = nwis.get_nwis_data(apportionment_year)
    return wo_realtime_reservoirs, wo_realtime_discharge, nwis_data
