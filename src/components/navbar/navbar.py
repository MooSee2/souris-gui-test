from dash import html
import dash_bootstrap_components as dbc

navbar = html.Div(
    className="navbar-container",
    children=[
        html.Div(
            children=[
                html.Img(src="assets/logo.svg", height="30px"),
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
