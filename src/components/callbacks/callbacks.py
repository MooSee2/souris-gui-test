from datetime import datetime as dt
from time import sleep

# from dataclasses import dataclass
from typing import Optional, Union
from io import BytesIO
from pathlib import Path

# import modules.server as serv
import pandas as pd
import plotly.express as px
from dash import Input, Output, State, callback, dcc
from dash.exceptions import PreventUpdate

import modules.data_layer.data_layer as dl
import modules.data_layer.model_inputs as mi


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
    Output("met-status-btn", "n_clicks"),
    Input("load-2023-met-btn", "n_clicks"),
    prevent_initial_call="initial_duplicate",
)
def get_2023_met_data(n_clicks):
    if n_clicks is None or n_clicks <= 0:
        raise PreventUpdate

    df = pd.read_excel("app_data/2023_met_data.xlsx", engine="openpyxl", sheet_name="data")
    df.drop(df.index[:3], inplace=True)
    df = df.round(3)
    df["date"] = df["date"].dt.strftime("%Y-%m-%d")
    df.dropna(how="all", inplace=True)
    return df.to_dict("records"), 1


# @callback(
#     Output("reservoir-data", "data"),
#     Output("reservoir-status-btn", "n_clicks"),
#     Input("load-data-button", "n_clicks"),
#     State("apportionment-year", "value"),
#     prevent_initial_call=True,
# )
# def download_reservoir_data(n_clicks, apportionment_year: int):
#     if n_clicks is None or n_clicks <= 0:
#         raise PreventUpdate

#     reservoirs = dl.get_reservoir_data(apportionment_year)

#     return reservoirs.to_dict("records"), 1


@callback(
    Output("discharge-data", "data"),
    Output("reservoir-data", "data"),
    Output("raw-discharge", "data"),
    Output("raw-reservoir", "data"),
    # Output("apportion-button", "disabled"),
    # Output("timeseries-dropdown", "disabled"),
    Output("load-data-button", "n_clicks"),
    # Output("load-data-button", "n_clicks"),
    Input("load-data-button", "n_clicks"),
    State("apportionment-year", "value"),
    State("username-input", "value"),
    State("password-input", "value"),
    prevent_initial_call=True,
)
def download_discharge_reservoir_met_data(
    n_clicks,
    apportionment_year: int,
    username: str,
    password: str,
):
    if n_clicks is None or n_clicks <= 0:
        raise PreventUpdate

    discharge, reservoir = dl.get_data(apportionment_year, username=username, password=password)

    return discharge.to_dict("records"), reservoir.to_dict("records"), discharge.to_dict("records"), reservoir.to_dict("records"), 1


# @callback(
#     Output("apportion-button", "disabled"),
#     Input("discharge-status-btn", "n_clicks"),
#     Input("reservoir-status-btn", "n_clicks"),
#     prevent_initial_call=True,
# )
# def apportionment_btn_disabled(discharge_n_clicks, reservoir_n_clicks):
#     # if n_clicks is None or n_clicks <= 0:
#     #     raise PreventUpdate
#     if all([discharge_n_clicks, reservoir_n_clicks]):
#         return False
#     return True


@callback(
    Output("evap-start-picker", "date"),
    Output("evap-end-picker", "date"),
    Output("appor-start-picker", "date"),
    Output("appor-end-picker", "date"),
    Input("apportionment-year", "value"),
    State("evap-start-picker", "date"),
    State("evap-end-picker", "date"),
    State("appor-start-picker", "date"),
    State("appor-end-picker", "date"),
    prevent_initial_call=True,
)
def update_input_years(appor_year, evap_start, evap_end, appor_start, appor_end):
    if not appor_year:
        appor_year = now.year

    evap_start = dt.strptime(f"{appor_year}-{evap_start[5:]}", "%Y-%m-%d").date()
    evap_end = dt.strptime(f"{appor_year}-{evap_end[5:]}", "%Y-%m-%d").date()
    appor_start = dt.strptime(f"{appor_year}-{appor_start[5:]}", "%Y-%m-%d").date()
    appor_end = dt.strptime(f"{appor_year}-{appor_end[5:]}", "%Y-%m-%d").date()
    return evap_start, evap_end, appor_start, appor_end


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
    # Output("report-container", "children", allow_duplicate=True),
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
    return False


@callback(
    Output("report-download", "data"),
    Input("report-download-btn", "n_clicks"),
    prevent_initial_call=True,
)
def download_report(n_clicks):
    if n_clicks == 0 or n_clicks is None:
        raise PreventUpdate

    filecache = Path(".filecache")

    # Grab first file in cache.  This should only ever be the most recent report.
    report = next(filecache.glob("*"))

    return dcc.send_file(report)


@callback(
    # Output("report-container", "children"),
    Output("calculation-modal", "is_open"),
    # Output("report-download", "data"),
    Output("report-download-btn", "disabled"),
    Output("main-tabs", "active_tab"),
    Output("apportion-button", "n_clicks"),
    # Output to report boxes
    Output("box-1-value", "children"),
    Output("box-2-value", "children"),
    Output("box-3-value", "children"),
    Output("box-4-value", "children"),
    Output("box-5a-value", "children"),
    Output("box-6-value", "children"),
    Output("box-7-value", "children"),
    Output("box-8-value", "children"),
    Output("box-9-value", "children"),
    Output("box-10-value", "children"),
    Output("box-11-value", "children"),
    Output("box-12-value", "children"),
    Output("box-13-value", "children"),
    Output("box-14-value", "children"),
    Output("box-15-value", "children"),
    Output("box-16-value", "children"),
    Output("box-17-value", "children"),
    Output("box-18-value", "children"),
    Output("box-19-value", "children"),
    Output("box-20-value", "children"),
    Output("box-21-value", "children"),
    Output("box-22-value", "children"),
    Output("box-23a-value", "children"),
    Output("box-24-value", "children"),
    Output("box-25-value", "children"),
    Output("box-26-value", "children"),
    Output("box-27-value", "children"),
    Output("box-28-value", "children"),
    Output("box-29-value", "children"),
    Output("box-30-value", "children"),
    Output("box-31-value", "children"),
    Output("box-32-value", "children"),
    Output("box-33-value", "children"),
    Output("box-34-value", "children"),
    Output("box-35-value", "children"),
    Output("box-36-value", "children"),
    Output("box-37-value", "children"),
    Output("box-38-value", "children"),
    Output("box-39-value", "children"),
    Output("box-40-value", "children"),
    Output("box-41-value", "children"),
    Output("box-42-value", "children"),
    Output("box-43-value", "children"),
    Output("box-44-value", "children"),
    Output("box-45a-value", "children"),
    Output("box-46-value", "children"),
    Output("box-47a-value", "children"),
    Output("box-48-value", "children"),
    Output("box-49-value", "children"),
    Output("box-50-value", "children"),
    Input("apportion-button", "n_clicks"),
    #### DATA ####
    # Reported Flows.
    #  If reported flows change and are added to the GUI, they
    #  will then need to be referenced here as input values to the model
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
    # Discharge table
    State("discharge-data", "data"),
    # Reservoir table
    State("reservoir-data", "data"),
    # Met table
    State("met-data", "data"),
    #### CONFIGS ####
    State("apportionment-year", "value"),
    State("appor-start-picker", "date"),
    State("appor-end-picker", "date"),
    State("evap-start-picker", "date"),
    State("evap-end-picker", "date"),
    State("raw-discharge", "data"),
    State("raw-reservoir", "data"),
    State("raw-met", "data"),
    prevent_initial_call=True,
)
def calculate_apportionment(
    n_clicks,
    #### DATA ####
    # Reported Flows
    pipline_input,
    long_creek,
    us_diversion,
    weyburn_pumpage,
    weyburn_return,
    upper_souris,
    estevan_pumpage,
    short_creek,
    lower_souris,
    moose_mountain,
    # Discharge table
    discharge_data,
    # Reservoir table
    reservoir_data,
    # Met table
    met_data,
    #### CONFIGS ####
    appor_year,
    appor_start,
    appor_end,
    evap_start,
    evap_end,
    raw_discharge,
    raw_reservoirs,
    raw_met,
):
    """This function collects all the inputs and data for the apportionment calculation"""
    if n_clicks == 0 or n_clicks is None:
        raise PreventUpdate

    discharge = pd.DataFrame(discharge_data)
    discharge["date"] = pd.to_datetime(discharge["date"])
    discharge.set_index("date", inplace=True)

    reservoirs = pd.DataFrame(reservoir_data)
    reservoirs["date"] = pd.to_datetime(reservoirs["date"])
    reservoirs.set_index("date", inplace=True)

    met = pd.DataFrame(met_data)
    met["date"] = pd.to_datetime(met["date"])
    met.set_index("date", inplace=True)

    model_inputs = mi.SourisModelInputs(
        # Reported flows
        pipeline=pipline_input,
        long_creek_minor_project_diversion=long_creek,
        us_diversion=us_diversion,
        weyburn_pumpage=weyburn_pumpage,
        weyburn_return_flow=weyburn_return,
        upper_souris_minor_diversion=upper_souris,
        estevan_net_pumpage=estevan_pumpage,
        short_creek_diversions=short_creek,
        lower_souris_minor_diversion=lower_souris,
        moose_mountain_minor_diversion=moose_mountain,
        # Discharge table
        discharge=discharge,
        raw_discharge=raw_discharge,
        # Reservoir table
        reservoirs=reservoirs,
        raw_reservoirs=raw_reservoirs,
        # Met table
        met=met,
        raw_met=raw_met,
        #### CONFIG
        appor_year=appor_year,
        appor_start=appor_start,
        appor_end=appor_end,
        evap_start=evap_start,
        evap_end=evap_end,
    )

    boxes = dl.run_main(model_inputs)

    # dcc.send_bytes(report_stream.getvalue(), filename),
    return (
        # Close modal if open
        False,
        # Enable Report download button
        False,
        # Set active tab
        "report-tab",
        # Return n_clicks for loading component of app. calculation button
        1,
        # Output Boxes
        boxes.box_1,
        boxes.box_2,
        boxes.box_3,
        boxes.box_4,
        boxes.box_5a,
        # boxes.box_5b,
        boxes.box_6,
        boxes.box_7,
        boxes.box_8,
        boxes.box_9,
        boxes.box_10,
        boxes.box_11,
        boxes.box_12,
        boxes.box_13,
        boxes.box_14,
        boxes.box_15,
        boxes.box_16,
        boxes.box_17,
        boxes.box_18,
        boxes.box_19,
        boxes.box_20,
        boxes.box_21,
        boxes.box_22,
        boxes.box_23a,
        # boxes.box_23b,
        boxes.box_24,
        boxes.box_25,
        boxes.box_26,
        boxes.box_27,
        boxes.box_28,
        boxes.box_29,
        boxes.box_30,
        boxes.box_31,
        boxes.box_32,
        boxes.box_33,
        boxes.box_34,
        boxes.box_35,
        boxes.box_36,
        boxes.box_37,
        boxes.box_38,
        boxes.box_39,
        boxes.box_40,
        boxes.box_41,
        boxes.box_42,
        boxes.box_43,
        boxes.box_44,
        boxes.box_45a,
        # boxes.box_45b,
        boxes.box_46,
        boxes.box_47a,
        # boxes.box_47b,
        boxes.box_48,
        boxes.box_49,
        boxes.box_50,
    )


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
