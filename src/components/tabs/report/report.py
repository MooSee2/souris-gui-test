import dash_bootstrap_components as dbc
from dash import html
from components.tabs.report.long_creek_basin import make_long_creek_basin_panel
from components.tabs.report.upper_souris_basin import make_upper_souris_basin_panel
from components.tabs.report.lower_souris_moose import make_lower_souris_moose_panel
from components.tabs.report.summary_panel import make_summary_panel


def make_report_panels():
    return dbc.Tab(
        label="Report",
        tab_id="report-tab",
        children=dbc.Card(
            className="mt-3",
            children=dbc.CardBody(
                id="report-container",
                children=[
                    make_long_creek_basin_panel(),
                    make_upper_souris_basin_panel(),
                    make_lower_souris_moose_panel(),
                    make_summary_panel(),
                ],
            ),
        ),
    )
