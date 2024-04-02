import dash

# import dash_bootstrap_components as dbc
from dash import html


# def get_logo():
#     return (
#         html.Img(
#             src=dash.get_asset_url("assets/images/logo.svg"),
#             height="30px",
#         ),
#     )
ISRB_web_link = "https://ijc.org/en/srb"


def navbar():
    return html.Div(
        className="navbar-container",
        children=[
            html.A(
                className="logo-wrapper",
                href=ISRB_web_link,
                style={"textDecoration": "none"},
                children=[
                    # html.Img(
                    #     className="logo-container",
                    #     src=dash.get_asset_url("images/usgs_logo.png"),
                    #     height="30px",
                    # ),
                    html.Img(
                        className="logo-container",
                        src=dash.get_asset_url("images/ijc_logo.svg"),
                        height="30px",
                    ),
                    html.H1(children=["International Souris River Board"]),
                ],
            ),
        ],
    )


# dbc.NavbarSimple(
#     id="navbar",
#     children=[
#         dbc.NavItem(
#             dbc.NavLink("Page 1", href="#"),
#         ),
#     ],
#     brand="IJC",
#     brand_href="#",
#     color="primary",
#     dark=True,
# )
