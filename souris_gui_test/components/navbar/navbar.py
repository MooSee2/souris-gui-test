import dash_bootstrap_components as dbc

navbar = dbc.NavbarSimple(
    id="navbar",
    children=[
        dbc.NavItem(
            dbc.NavLink("Page 1", href="#"),
        ),
    ],
    brand="IJC",
    brand_href="#",
    color="primary",
    dark=True,
)
