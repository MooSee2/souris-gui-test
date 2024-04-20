import pandas as pd
import modules.data_layer.download_api_services as serv
import modules.data_layer.trapz_integration as trapz


def get_nwis_data(year):
    nwis = serv.NWISWaterService(service="dv")
    data = nwis.get(
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

    dfs = {}
    for staid, df in data.items():
        df[f"{staid}_approval"] = df["qualifiers"].apply(lambda x: "Approved" if "A" in x else "Unapproved")
        df.rename(columns={"value": staid}, inplace=True)
        df.drop("qualifiers", axis=1, inplace=True)
        dfs[staid] = df

    return pd.concat(list(dfs.values()), axis=1)
