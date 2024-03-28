import dash
from dash import dash_table
import pandas as pd
from collections import OrderedDict

# Assuming you have a DataFrame 'df'
df = pd.DataFrame(
    {
        "Status": ["Approved", "Pending", "Rejected", "Approved"],
        "Column2": ["A", "B", "C", "D"],
    }
)


data = OrderedDict(
    [
        (
            "Date",
            [
                "2015-01-01",
                "2015-10-24",
                "2016-05-10",
                "2017-01-10",
                "2018-05-10",
                "2018-08-15",
            ],
        ),
        # ("Region", ["Montreal", "Toronto", "New York City", "Miami", "San Francisco", "London"]),
        ("Temperature", [1, -20, 3.512, 4, 10423, -441.2]),
        (
            "Temperature_approval",
            [
                "approved",
                "approved",
                "approved",
                "unapproved",
                "unapproved",
                "approved",
            ],
        ),
        ("Humidity", [10, 20, 30, 40, 50, 60]),
        (
            "Humidity_approval",
            [
                "approved",
                "approved",
                "approved",
                "unapproved",
                "unapproved",
                "approved",
            ],
        ),
        ("Pressure", [2, 10924, 3912, -10, 3591.2, 15]),
        (
            "Pressure_approval",
            [
                "approved",
                "unapproved",
                "unapproved",
                "approved",
                "approved",
                "approved",
            ],
        ),
    ]
)

df = pd.DataFrame(data)


app = dash.Dash(__name__)

app.layout = dash_table.DataTable(
    id="table",
    columns=[{"name": i, "id": i} for i in df.columns],
    data=df.to_dict("records"),
    style_data_conditional=[
        {
            "if": {
                "filter_query": '{Humidity_approval} eq "approved"',
                "column_id": "Humidity",
            },
            "backgroundColor": "#008000",
            "color": "white",
        },
        {
            "if": {
                "filter_query": '{Humidity_approval} eq "unapproved"',
                "column_id": "Humidity",
            },
            "backgroundColor": "#FF1515",
            "color": "white",
        },
        {
            "if": {
                "filter_query": '{Pressure_approval} eq "approved"',
                "column_id": "Pressure",
            },
            "backgroundColor": "#008000",
            "color": "white",
        },
        {
            "if": {
                "filter_query": '{Pressure_approval} eq "unapproved"',
                "column_id": "Pressure",
            },
            "backgroundColor": "#FF1515",
            "color": "white",
        },
        {
            "if": {
                "filter_query": '{Temperature_approval} eq "unapproved"',
                "column_id": "Temperature",
            },
            "backgroundColor": "#FF1515",
            "color": "white",
        },
    ],
    hidden_columns=["Temperature_approval", "Pressure_approval", "Humidity_approval"],
    editable=True
)

if __name__ == "__main__":
    app.run(debug=True)


# import dash
# import dash_table
# import pandas as pd

# # Assuming you have a DataFrame 'df'
# df = pd.DataFrame({
#     'Status': ['Approved', 'Pending', 'Rejected', 'Approved'],
#     'Column2': ['A', 'B', 'C', 'D']
# })

# app = dash.Dash(__name__)

# app.layout = dash_table.DataTable(
#     id='table',
#     columns=[{"name": i, "id": i} for i in df.columns],
#     data=df.to_dict('records'),
#     style_data_conditional=[
#         {
#             'if': {
#                 'filter_query': '{Status} eq "Approved"',
#                 'column_id': 'Column2'
#             },
#             'backgroundColor': '#008000',  # Hex code for green
#             'color': 'white'
#         }
#     ]
# )

# if __name__ == '__main__':
#     app.run_server(debug=True)


# from dash import Dash, dash_table
# import pandas as pd
# from collections import OrderedDict

# data = OrderedDict(
#     [
#         (
#             "Date",
#             [
#                 "2015-01-01",
#                 "2015-10-24",
#                 "2016-05-10",
#                 "2017-01-10",
#                 "2018-05-10",
#                 "2018-08-15",
#             ],
#         ),
#         # ("Region", ["Montreal", "Toronto", "New York City", "Miami", "San Francisco", "London"]),
#         ("Temperature", [1, -20, 3.512, 4, 10423, -441.2]),
#         (
#             "Temperature_approval",
#             [
#                 "approved",
#                 "approved",
#                 "approved",
#                 "unapproved",
#                 "unapproved",
#                 "approved",
#             ],
#         ),
#         ("Humidity", [10, 20, 30, 40, 50, 60]),
#         (
#             "Humidity_approval",
#             [
#                 "approved",
#                 "approved",
#                 "approved",
#                 "unapproved",
#                 "unapproved",
#                 "approved",
#             ],
#         ),
#         ("Pressure", [2, 10924, 3912, -10, 3591.2, 15]),
#         (
#             "Pressure_approval",
#             [
#                 "approved",
#                 "unapproved",
#                 "unapproved",
#                 "approved",
#                 "approved",
#                 "approved",
#             ],
#         ),
#     ]
# )

# # df = pd.DataFrame(data)

# app = Dash(__name__)


# def highlight_above_and_below_first_row(df):
#     df_numeric_columns = df.select_dtypes("number")
#     return [
#         {
#             "if": {
#                 "filter_query": "{{{}}} == {}".format(
#                     df[f"{col}_approval"], "approval"
#                 ),
#                 "column_id": col,
#             },
#             "backgroundColor": "#3D9970",
#             "color": "white",
#         }
#         for col in df_numeric_columns.columns
#     ]


# app.layout = dash_table.DataTable(
#     data=df.to_dict("records"),
#     hidden_columns=["Humidity_approval", "Pressure_approval", "Temperature_approval"],
#     columns=[{"name": i, "id": i} for i in df.columns],
#     style_data_conditional=[
#         {
#             "if": {"column_id": "a", "filter_query": "{a} gt 3"},
#             "backgroundColor": "#3D9970",
#             "color": "white",
#         },
#     ],
#     editable=True,
#     fill_width=False,
# )


# if __name__ == "__main__":
#     app.run_server(debug=True)
