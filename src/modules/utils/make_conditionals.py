datetime_conditional = [
    {
        "if": {
            "column_id": "date",
        },
        "backgroundColor": "#fafafa",
        "verticalAlign": "middle",
    },
]


def make_conditionals(stations: set):
    return make_approved_conditionals(stations)  # + make_missing_value_conditionals(stations) + datetime_conditional


# make_striping_conditional() +
#  + make_unapproved_conditionals(stations)


def make_approved_conditionals(stations):
    return [
        {
            "if": {
                "filter_query": f"{{{station}_approval}} = 'Approved'",
                "column_id": f"{station}_approval",
            },
            "backgroundColor": "#D1E5F0",
            "color": "black",
        }
        for station in stations
    ]


# def make_unapproved_conditionals(stations):
#     return [
#         {
#             "if": {
#                 "filter_query": f'{{{station}_approval}} eq "Provisional"',
#                 "column_id": f"{station}_approval",
#             },
#             "backgroundColor": "#0072B2",
#             "color": "white",
#             "verticalAlign": "middle",
#         }
#         for station in stations
#     ]


def make_missing_value_conditionals(stations):
    return [
        {
            "if": {
                "filter_query": f"{station} = ''",
                "column_id": station,
            },
            "backgroundColor": "tomato",
            "color": "white",
        }
        for station in stations
    ]


def make_striping_conditional():
    return [
        {
            "if": {"row_index": "odd"},
            "backgroundColor": "rgb(220, 220, 220)",
        },
    ]
