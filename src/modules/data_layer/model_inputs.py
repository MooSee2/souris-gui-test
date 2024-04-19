from dataclasses import dataclass


@dataclass
class SourisModelInputs:
    # Reported flows
    pipeline: int
    long_creek_minor_project_diversion: int
    us_diversion: int
    weyburn_pumpage: int
    weyburn_return_flow: int
    upper_souris_minor_diversion: int
    estevan_net_pumpage: int
    short_creek_diversions: int
    lower_souris_minor_diversion: int
    moose_mountain_minor_diversion: int
    # Discharge table
    discharge: int
    # Reservoir table
    reservoirs: int
    # Met table
    met: int
    #### CONFIGS ####
    appor_year: int
    appor_start: int
    appor_end: int
    evap_start: int
    evap_end: int
