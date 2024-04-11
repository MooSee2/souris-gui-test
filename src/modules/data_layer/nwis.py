import modules.data_layer.download_api_services as serv


def get_nwis_data(year):
    nwis = serv.NWISWaterService(service="dv")
    return nwis.get(
        params=dict(
            sites=[
                "05113600",
                "05114000",
            ],
            startDT=f"{year}-01-01",
            endDT=f"{year}-12-31",
            parameterCd="00060",
            format="json",
        )
    )
