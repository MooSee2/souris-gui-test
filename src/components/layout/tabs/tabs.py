import dash_bootstrap_components as dbc
from components.layout.tabs.report.report import make_report_panels
from components.layout.tabs import (
    discharge,
    graphs,
    met,
    reported_flows,
    reservoirs,
)


def tabs():
    return dbc.Tabs(
        # TODO remove active_tab for production.  Only used for quick testing of tabs.
        id="main-tabs",
        # active_tab="report-tab",
        children=[
            reported_flows.make_reported_flows_tab(),
            discharge.make_discharge_tab(),
            reservoirs.make_reservoirs_tab(),
            met.make_met_tab(),
            make_report_panels(),
            graphs.graphs(),
        ],
    )
