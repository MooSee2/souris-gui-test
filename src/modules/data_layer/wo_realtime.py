import modules.data_layer.download_api_services as serv

ca_reservoir_stations = (
    "05NA006",
    "05NB020",
    "05NB016",
    "05NC002",
    "05ND012",
)

ca_discharge_stations = (
    "05NA003",
    "05NB001",
    "05NB011",
    "05NB014",
    "05NB018",
    "05NB033",
    "05NB035",
    "05NB036",
    "05NB038",
    "05NB039",
    "05NB040",
    "05NB041",
)


def get_wo_realtime_discharge(year):
    ca_discharge = serv.WaterOfficeRealTime()
    return ca_discharge.get(
        params={
            "stations[]": ca_discharge_stations,
            "start_date": f"{year}-01-01",
            "end_date": f"{year}-01-01",
            "parameters[]": 47,
        },
    )


def get_wo_realtime_reservoirs(year):
    ca_discharge = serv.WaterOfficeRealTime()
    return ca_discharge.get(
        params={
            "stations[]": ca_reservoir_stations,
            "start_date": f"{year}-01-01",
            "end_date": f"{year}-01-01",
            "parameters[]": 46,
        },
    )
