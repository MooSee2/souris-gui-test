import pandas as pd

import src.modules.data_layer.api_retrievers as serv

CFS_TO_CMS = 0.0283168466


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
            access=0,
        )
    )

    dfs = {}
    for staid, df in data.items():
        df[f"{staid}_approval"] = df["qualifiers"].apply(lambda x: "Approved" if "A" in x else "Unapproved")
        df.rename(columns={"value": staid}, inplace=True)
        df.drop("qualifiers", axis=1, inplace=True)
        df[staid] = df[staid].mul(CFS_TO_CMS).round(3)
        dfs[staid] = df

    return pd.concat(list(dfs.values()), axis=1)
