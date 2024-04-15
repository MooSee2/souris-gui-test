from time import sleep

import app_data.test_data as td
from modules.data_layer import nwis
from modules.data_layer import wo_realtime as wo

# from souris.scripts.souris_main import main


def get_reservoir_data(apportionment_year: int):
    wo_realtime_reservoirs = wo.get_wo_realtime_reservoirs(apportionment_year)
    # nwis_data = nwis.get_nwis_data(apportionment_year)
    return wo_realtime_reservoirs


def get_discharge_data(apportionment_year: int):
    wo_realtime_discharge = wo.get_wo_realtime_discharge(apportionment_year)
    # nwis_data = nwis.get_nwis_data(apportionment_year)
    return wo_realtime_discharge


def run_main(
    #### DATA ####
    # Reported Flows
    pipline_input,
    long_creek,
    us_diversion,
    weyburn_pumpage,
    weyburn_return,
    upper_souris,
    estevan_pumpage,
    short_creek,
    lower_souris,
    moose_mountain,
    # Discharge table
    discharge_data,
    # Reservoir table
    reservoir_date,
    # Met table
    met_data,
    #### CONFIGS ####
    appor_year,
    app_start,
    app_end,
    evap_start,
    evap_end,
):

    # souris_main.main(
    #     #### DATA ####
    #     # Reported Flows
    #     pipline_input,
    #     long_creek,
    #     us_diversion,
    #     weyburn_pumpage,
    #     weyburn_return,
    #     upper_souris,
    #     estevan_pumpage,
    #     short_creek,
    #     lower_souris,
    #     moose_mountain,
    #     # Discharge table
    #     discharge_data,
    #     # Reservoir table
    #     reservoir_date,
    #     # Met table
    #     met_data,
    #     #### CONFIGS ####
    #     appor_year,
    #     app_start,
    #     app_end,
    #     evap_start,
    #     evap_end,
    #     )
    sleep(5)
    return None
