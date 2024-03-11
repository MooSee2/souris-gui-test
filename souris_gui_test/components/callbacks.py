import base64
import datetime
import io

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


# @callback(
#     Output("output-inputs", "children"),
#     Input("apportion-button", "n_clicks"),
#     State("weyburn-pumpage-input", "value"),
#     State("pipeline-input", "value"),
#     State("long-creek-minor-project-diversion-input", "value"),
#     State("us-diversion-input", "value"),
#     prevent_initial_call=True,
# )
# def add_reported_flows(clicks, city_of_weyburn, the_lake, pumpage, pipe):
#     try:
#         return int(city_of_weyburn) + int(the_lake) + int(pumpage) + int(pipe)
#     except TypeError:
#         return 0
