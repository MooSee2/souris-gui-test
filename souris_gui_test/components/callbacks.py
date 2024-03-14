import base64
import datetime
import io
from datetime import datetime as dt
import data.test_data as td
import plotly.express as px


import pandas as pd
from dash import Input, Output, State, callback, dash_table, html


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
#         [
#             html.H5(filename),
#             html.H6(datetime.datetime.fromtimestamp(date)),
#             dash_table.DataTable(
#                 df.to_dict("records"),
#                 [{"name": i, "id": i} for i in df.columns],
#                 editable=True,
#             ),
#             # html.Hr(),
#             # For debugging, display the raw contents provided by the web browser
#             # html.Div("Raw Content"),
#             # html.Pre(
#             #     contents[0:200] + "...", style={"whiteSpace": "pre-wrap", "wordBreak": "break-all"}
#             # ),
#         ],
#         id=filename,
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
)
def timeseries_graph(staid):
    data = td.discharge_data
    fig = px.line(data_frame=data, x=data.index, y="05NB001")
    return fig
