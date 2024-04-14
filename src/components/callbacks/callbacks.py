from datetime import datetime as dt
from time import sleep

# from dataclasses import dataclass
from typing import Optional, Union

# import modules.server as serv
import pandas as pd
import plotly.express as px
from dash import Input, Output, State, callback, dash_table, html
from dash.exceptions import PreventUpdate

import modules.data_layer.data_layer as dl

# import src.modules.data_layer.download_api_services as dl

# from app_data import stations as const

# # cache this one
# # @cache.memoize()
# def get_data(start_date, end_date) -> None:
#     sleep(1)
#     return _download_data(start_date, end_date)
now = dt.now()

stations_dict = [
    {"id": "05NA006", "type": "reservoir", "name": "Larsen Reservoir", "unique_id": "013d9d474541460aa3b1de4381276c38"},
    {"id": "05NB020", "type": "reservoir", "name": "Nickle Lake", "unique_id": "988537b8321f47a5a421bfa23c19263a"},
    {"id": "05NB016", "type": "reservoir", "name": "Roughbark Reservoir", "unique_id": "cd827ce017344fd7b2764dceab9d6989"},
    {"id": "05NC002", "type": "reservoir", "name": "Moose Mountain Lake", "unique_id": "21a5a52a1f8447ffa6c872429ef94a39"},
    {"id": "05ND012", "type": "reservoir", "name": "Grant Devine Reservoir", "unique_id": "fda763c4468b47bc9d693a14a6b77ba2"},
    {"id": "05NB001", "type": "discharge", "name": "Long Creek near Estevan", "unique_id": "ec83a47a06d4410e84ba94d384fb0523"},
    {"id": "05NB036", "type": "discharge", "name": "Souris River below Rafferty Reservoir", "unique_id": "8f6f1b90e5f34a0cb08ed1c7a81f11c2"},
    {"id": "05NB011", "type": "discharge", "name": "Yellograss Ditch", "unique_id": "d8cadb5a4c524fd1a8b172a04d00382b"},
    {"id": "05NB018", "type": "discharge", "name": "Tatagwa Lake Drain", "unique_id": "8572ab68835341a09f093ef947d167b2"},
    {"id": "05NA003", "type": "discharge", "name": "Long Creek at Western Crossing", "unique_id": "2e2cb41a826c4743ac2e12ce08c96310"},
    {"id": "05NB040", "type": "discharge", "name": "Souris River near Ralph", "unique_id": "83d5168d48194b2ab0520a0510c51d80"},
    {"id": "05NB041", "type": "discharge", "name": "Roughbark Creek above Rafferty Res.", "unique_id": "2e7f3f3b51bd4605b240a21fb0e17009"},
    {"id": "05NB038", "type": "discharge", "name": "Boundary Reservoir Diversion Canal", "unique_id": "62744ab8cf244767ae9d78307db39668"},
    {"id": "05NB014", "type": "discharge", "name": "Jewel Creek near Goodwater", "unique_id": "2cb7747424bc49b3ae2e7acf16dfb7d9"},
    {"id": "05NB035", "type": "discharge", "name": "Cooke Creek near Goodwater", "unique_id": "4f97b149655e4ec8bfa16b35b9933d7a"},
    {"id": "05NB033", "type": "discharge", "name": "Moseley Creek near Halbrite", "unique_id": "d124778abe524653ac32e82212cfe41b"},
    {"id": "05NB039", "type": "discharge", "name": "Tributary near Outram", "unique_id": "098e25d30c7244b4a158927efb324d4d"},
]

unique_id_to_staid = {station["unique_id"]: station["id"] for station in stations_dict}

stations = [
    ("05NA006", "reservoir", "Larsen Reservoir", "013d9d474541460aa3b1de4381276c38"),
    ("05NB020", "reservoir", "Nickle Lake", "988537b8321f47a5a421bfa23c19263a"),
    ("05NB016", "reservoir", "Roughbark Reservoir", "cd827ce017344fd7b2764dceab9d6989"),
    ("05NC002", "reservoir", "Moose Mountain Lake", "21a5a52a1f8447ffa6c872429ef94a39"),
    ("05ND012", "reservoir", "Grant Devine Reservoir", "fda763c4468b47bc9d693a14a6b77ba2"),
    ("05NB001", "discharge", "Long Creek near Estevan", "ec83a47a06d4410e84ba94d384fb0523"),
    ("05NB036", "discharge", "Souris River below Rafferty Reservoir", "8f6f1b90e5f34a0cb08ed1c7a81f11c2"),
    ("05NB011", "discharge", "Yellograss Ditch", "d8cadb5a4c524fd1a8b172a04d00382b"),
    ("05NB018", "discharge", "Tatagwa Lake Drain", "8572ab68835341a09f093ef947d167b2"),
    ("05NA003", "discharge", "Long Creek at Western Crossing", "2e2cb41a826c4743ac2e12ce08c96310"),
    ("05NB040", "discharge", "Souris River near Ralph", "83d5168d48194b2ab0520a0510c51d80"),
    ("05NB041", "discharge", "Roughbark Creek above Rafferty Res.", "2e7f3f3b51bd4605b240a21fb0e17009"),
    ("05NB038", "discharge", "Boundary Reservoir Diversion Canal", "62744ab8cf244767ae9d78307db39668"),
    ("05NB014", "discharge", "Jewel Creek near Goodwater", "2cb7747424bc49b3ae2e7acf16dfb7d9"),
    ("05NB035", "discharge", "Cooke Creek near Goodwater", "4f97b149655e4ec8bfa16b35b9933d7a"),
    ("05NB033", "discharge", "Moseley Creek near Halbrite", "d124778abe524653ac32e82212cfe41b"),
    ("05NB039", "discharge", "Tributary near Outram", "098e25d30c7244b4a158927efb324d4d"),
]

# def make_dropdown_options(data: set[tuple]) -> list[dict]:
#     dropdowns = [{"label": staid, "value": name, "group": group} for staid, name, group in data]
#     return sorted(dropdowns, key=lambda x: (x["group"], x["label"]))


# @callback(
#     Output("load-data-modal", "is_open"),
#     Input("load-data-button", "n_clicks"),
#     State("load-data-modal", "is_open"),
# )
# def toggle_modal(n1: Optional[int], is_open: bool) -> bool:
#     """Toggle load-data-modal open or closed.

#     Parameters
#     ----------
#     n1 : Optional[int] by default, None
#         Number of clicks from load-data-button.
#     is_open : bool
#         State of load-data-module display.
#         True if open and False if closed.


#     Returns
#     -------
#     Bool
#         What state to set the load-data-modal display.
#     """
#     if n1 and not is_open:
#         return True
#     return False


@callback(
    Output("discharge-data", "data", allow_duplicate=True),
    Output("reservoir-data", "data", allow_duplicate=True),
    Output("met-data", "data", allow_duplicate=True),
    Input("apportionment-year", "value"),
    prevent_initial_call="initial_duplicate",
)
def update_dummy_datetime(year):
    datetime = pd.date_range(f"{year}-01-01", f"{year}-12-31", freq="d").strftime("%Y-%m-%d")
    dummy_data = pd.DataFrame({"date": datetime})
    return (
        dummy_data.to_dict("records"),
        dummy_data.to_dict("records"),
        dummy_data.to_dict("records"),
    )


@callback(
    Output("met-data", "data", allow_duplicate=True),
    Input("load-2023-met-btn", "n_clicks"),
    prevent_initial_call="initial_duplicate",
)
def update_dummy_datetime(n_clicks):
    if n_clicks is None or n_clicks <= 0:
        raise PreventUpdate

    df = pd.read_excel("app_data/2023_met_data.xlsx", engine="openpyxl", sheet_name="data")
    df.drop(df.index[:3], inplace=True)
    df = df.round(3)
    df["date"] = df["date"].dt.strftime("%Y-%m-%d")
    df.dropna(how="all", inplace=True)
    return df.to_dict("records")


@callback(
    # Output("loading-data-div", "children"),
    Output("reservoir-data", "data"),
    # Output("discharge-data", "data"),
    # Output("met-data", "data"),
    # Output("apportion-button", "disabled"),
    # Output("timeseries-dropdown", "disabled"),
    # Output("load-data-button", "n_clicks"),
    Input("load-data-button", "n_clicks"),
    State("apportionment-year", "value"),
    prevent_initial_call=True,
)
def download_reservoir_data(n_clicks, apportionment_year: int):
    if n_clicks is None or n_clicks <= 0:
        raise PreventUpdate

    reservoirs = dl.get_reservoir_data(apportionment_year)

    return reservoirs.to_dict("records")


@callback(
    Output("discharge-data", "data"),
    Input("load-data-button", "n_clicks"),
    State("apportionment-year", "value"),
    prevent_initial_call=True,
)
def download_discharge_data(n_clicks, apportionment_year: int):
    if n_clicks is None or n_clicks <= 0:
        raise PreventUpdate

    discharge = dl.get_discharge_data(apportionment_year)

    return discharge.to_dict("records")


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
        selected_year = now.year

    start_date = dt.strptime(f"{selected_year}-{start_date[5:]}", "%Y-%m-%d").date()
    end_date = dt.strptime(f"{selected_year}-{end_date[5:]}", "%Y-%m-%d").date()
    return start_date, end_date


@callback(
    Output("timeseries-plot", "figure"),
    Output("time-series-loader", "parent_style"),
    Input("timeseries-dropdown", "value"),
    Input("reservoir-data", "data"),
    Input("met-data", "data"),
    Input("discharge-data", "data"),
    prevent_initial_call=True,
)
def timeseries_graph(staids, reservoir_data, met_data, discharge_data):
    if not staids:
        return (
            {
                "layout": {
                    "xaxis": {"visible": False},
                    "yaxis": {"visible": False},
                    "annotations": [
                        {
                            "text": "No Data Selected.",
                            "xref": "paper",
                            "yref": "paper",
                            "showarrow": False,
                            "font": {"size": 28},
                        }
                    ],
                }
            },
            {"display": "none"},
        )

    reservoir_data = pd.DataFrame(reservoir_data)
    met_data = pd.DataFrame(met_data)
    discharge_data = pd.DataFrame(discharge_data)

    df = pd.concat([reservoir_data, met_data, discharge_data])
    df.index = pd.DatetimeIndex(pd.to_datetime(df["datetime"]))

    fig = px.scatter()

    for staid in staids:
        fig.add_scatter(x=df.index.values, y=df[staid])

    return (
        fig,
        {"display": "none"},
    )


@callback(
    Output("calculation-modal", "is_open", allow_duplicate=True),
    Input("calc-cancel-button", "n_clicks"),
    prevent_initial_call=True,
)
def toggle_calculation_modal(_) -> bool:
    """Toggle calculation-modal open or closed.

    Parameters
    ----------
    n1 : Optional[int] by default, None
        Number of clicks from apportion-button.
    is_open : bool
        State of modal display.
        True if open and False if closed.


    Returns
    -------
    Bool
        What state to set the modal display.
    """
    return False


@callback(
    Output("report-container", "children", allow_duplicate=True),
    Output("calculation-modal", "is_open", allow_duplicate=True),
    Input("calc-continue-button", "n_clicks"),
    prevent_initial_call=True,
)
def toggle_calculation_modal(_) -> bool:
    """Toggle calculation-modal open or closed.

    Parameters
    ----------
    n1 : Optional[int] by default, None
        Number of clicks from apportion-button.
    is_open : bool
        State of modal display.
        True if open and False if closed.


    Returns
    -------
    Bool
        What state to set the modal display.
    """
    return html.P("Blank Report goes here from modal continue button", className="card-text"), False


# def detect_missing_reported_flows(reported_flows: tuple) -> dict:


@callback(
    Output("report-container", "children"),
    Output("calculation-modal", "is_open"),
    Input("apportion-button", "n_clicks"),
    State("pipeline-input", "value"),
    State("long-creek-minor-project-diversion-input", "value"),
    State("us-diversion-input", "value"),
    State("weyburn-pumpage-input", "value"),
    State("weyburn-return-flow-input", "value"),
    State("upper-souris-minor-diversion-input", "value"),
    State("estevan-net-pumpage-input", "value"),
    State("short-creek-diversions-input", "value"),
    State("lower-souris-minor-diversion-input", "value"),
    State("moose-mountain-minor-diversion-input", "value"),
    prevent_initial_call=True,
)
def calculate_apportionment(n_clicks, *inputs):
    if n_clicks == 0 or n_clicks is None:
        raise PreventUpdate

    if not all(inputs):
        # TODO detect which stations are missing reported flows and ask the user if they want to continue
        return html.P("Blank Report goes here from apportion button", className="card-text"), True

    return html.Div(className="tab2-thing"), False


# @callback(
#     Output("timeseries-plot", "figure"),
#     Input("query-data-button", "n_clicks"),
#     prevent_initial_call=True,
# )
# def timeseries_graph_message(clicks):
#     if clicks > 0:
#         return {
#             "layout": {
#                 "xaxis": {"visible": False},
#                 "yaxis": {"visible": False},
#                 "annotations": [
#                     {
#                         "text": "Select station to view time-series data.",
#                         "xref": "paper",
#                         "yref": "paper",
#                         "showarrow": False,
#                         "font": {"size": 28},
#                     }
#                 ],
#             }
#         }

#     raise PreventUpdate


# @callback(
#     Output("data-downloaded-div", "children"),
#     Input("query-data-button", "n_clicks"),
# )
# def get_box_data(_):
#     return None


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
