from datetime import datetime as dt
from time import sleep
from typing import Optional, Union

import modules.data_layer as dl

# import modules.server as serv
import pandas as pd
import plotly.express as px
from dash import Input, Output, State, callback, dash_table, html
from dash.exceptions import PreventUpdate
from dash_app import cache

# from dataclasses import dataclass
from typing import Optional


class AppData:
    discharge: Optional[dict]
    met: Optional[dict]
    reservoir: Optional[dict]


app_data = AppData()


def _download_data(start_date, end_date) -> None:
    sleep(4)
    local_data = dl.load_data(start_date, end_date)
    # dict of table name to dataframe
    # return dict(zip({"discharge", "met", "reservoir"}, local_data))
    app_data.discharge, app_data.met, app_data.reservoir = local_data
    return local_data


# cache this one
@cache.memoize()
def get_data(start_date, end_date) -> None:
    sleep(1)
    return _download_data(start_date, end_date)


@callback(
    Output("load-data-modal", "is_open"),
    Input("load-data-button", "n_clicks"),
    State("load-data-modal", "is_open"),
)
def toggle_modal(n1: Optional[int], is_open: bool) -> bool:
    """Toggle load-data-modal open or closed.

    Parameters
    ----------
    n1 : Optional[int] by default, None
        Number of clicks from load-data-button.
    is_open : bool
        State of load-data-module display.
        True if open and False if closed.


    Returns
    -------
    Bool
        What state to set the load-data-modal display.
    """
    if n1 and not is_open:
        return True
    return False


# return not is_open if n1 else is_open


@callback(
    Output("loading-data-div", "children"),
    Output("data-downloaded-signal", "n_clicks"),
    Input("query-data-button", "n_clicks"),
)
# @cache.memoize()
def download_data(n_clicks):
    if n_clicks is None:
        raise PreventUpdate

    n_clicks = 0
    local_data = get_data(n_clicks, "end_date")
    # Read from actual load_data() that reads from servers

    return "Data loaded!", 1


@callback(
    Output("evap-start-picker", "date"),
    Output("evap-end-picker", "date"),
    Input("apportionment-year", "value"),
    State("evap-start-picker", "date"),
    State("evap-end-picker", "date"),
    prevent_initial_call=True,
)
def update_evap_years(selected_year, start_date, end_date):
    if not selected_year:
        selected_year = dt.now().year

    start_date = dt.strptime(f"{selected_year}-{start_date[5:]}", "%Y-%m-%d").date()
    end_date = dt.strptime(f"{selected_year}-{end_date[5:]}", "%Y-%m-%d").date()
    return start_date, end_date


@callback(
    Output("timeseries-plot", "figure"),
    Input("timeseries-dropdown", "value"),
    # State("timeseries-plot", "figure"),
    prevent_initial_call=True,
)
def timeseries_graph(staids):
    if not staids:
        raise PreventUpdate

    df = pd.concat([app_data.reservoir, app_data.met, app_data.discharge])

    fig = px.scatter()

    for staid in staids:
        fig.add_scatter(x=df.index.values, y=df[staid])

    return fig


# @callback(
#     Output("data-downloaded-div", "children"),
#     Input("query-data-button", "n_clicks"),
# )
# def download_data(_):
#     return None


# def parse_contents(contents, filename, date):
#     content_type, content_string = contents.split(",")

#     decoded = base64.b64decode(content_string)
#     try:
#         if "csv" in filename:
#             # Assume that the user uploaded a CSV file
#             df = pd.read_csv(io.StringIO(decoded.decode("utf-8")))
#         elif "xls" in filename:
#             # Assume that the user uploaded an excel file
#             df = pd.read_excel(io.BytesIO(decoded))
#     except Exception as e:
#         print(e)
#         return html.Div(["There was an error processing this file."])

#     return html.Div(
#         children=[
#             dash_table.DataTable(
#                 df.to_dict("records"),
#                 [{"name": i, "id": i} for i in df.columns],
#                 editable=True,
#             ),
#         ],
#     )


# @callback(
#     Output("output-data-upload", "children"),
#     Input("upload-data", "contents"),
#     State("upload-data", "filename"),
#     State("upload-data", "last_modified"),
# )
# def update_output(list_of_contents, list_of_names, list_of_dates):
#     if list_of_contents is not None:
#         return [
#             parse_contents(c, n, d)
#             for c, n, d in zip(list_of_contents, list_of_names, list_of_dates)
#         ]