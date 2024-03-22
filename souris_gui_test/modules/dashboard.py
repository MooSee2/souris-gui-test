
from dash import Dash, html
import components.callbacks
from components.layout import make_layout
import dash_bootstrap_components as dbc

def create_dashapp() -> Dash:

    external_stylesheets = [
        dbc.themes.BOOTSTRAP,
        dbc.icons.FONT_AWESOME,
    ]

    app = Dash(
        name="__main__",
        external_stylesheets=external_stylesheets,
    )

    app.layout = html.Div(
        children=make_layout(),
        id="dash-root",
    )
    return app
