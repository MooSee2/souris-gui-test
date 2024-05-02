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
        # TODO remove active_tab for production.  Only used for quick testing of tabs.
        active_tab="report-tab",
        children=[
            reported_flows(),
            discharge(),
            reservoirs(),
            met_data(),
            report.make_report_panels(),
            graphs(),
        ],
    )
