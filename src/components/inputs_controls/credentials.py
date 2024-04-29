import dash_bootstrap_components as dbc
from dash import dcc, html

from app_data import stations as const


def credentials():
    return html.Div(
        className="input-container",
        children=[
            # html.Div(
            #     className="header-info-container",
            #     children=[
            #         html.Div(
            #             className="HH6",
            #             children=["Apportionment Year"],
            #         ),
            #         html.Div(id="apport-year-tip", className="info-container", children=html.Div(className="fa-solid fa-info")),
            #     ],
            # ),
            # dbc.Tooltip(
            #     "The year to apportion.  By default, the current year.",
            #     target="apport-year-tip",
            # ),
            html.Div(
                className="header-info-container",
                children=[
                    dcc.Input(
                        id="username-input",
                        type="text",
                        placeholder="username",
                    ),
                    html.Div(id="username-tip", className="info-container", children=html.Div(className="fa-solid fa-info")),
                ],
            ),
            html.Div(
                className="header-info-container",
                children=[
                    dcc.Input(
                        id="password-input",
                        type="password",
                        placeholder="password",
                    ),
                    html.Div(id="password-tip", className="info-container", children=html.Div(className="fa-solid fa-info")),
                ],
            ),
            dbc.Tooltip(
                "Username for WO partner realtime service.",
                target="username-tip",
            ),
            dbc.Tooltip(
                "Password for WO partner realtime service.",
                target="password-tip",
            ),
        ],
    )
