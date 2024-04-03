import dash_bootstrap_components as dbc
from components.tabs import (
    discharge,
    graphs,
    met_data,
    report,
    reported_flows,
    reservoirs,
)


def tabs():
    return dbc.Tabs(
        [
            reported_flows(),
            discharge(),
            reservoirs(),
            met_data(),
            report(),
            graphs(),
        ],
    )
