import dash
from dash import html

ISRB_web_link = "https://ijc.org/en/srb"
ijc_logo = "images/ijc_logo.svg"


def navbar():
    return html.Div(
        className="navbar-container",
        children=[
            html.A(
                className="logo-wrapper",
                href=ISRB_web_link,
                style={"textDecoration": "none"},
                children=[
                    html.Img(
                        className="logo-container",
                        src=dash.get_asset_url(ijc_logo),
                        height="30px",
                    ),
                    html.H1(
                        children=[
                            "International Souris River Board",
                        ]
                    ),
                ],
            ),
        ],
    )
