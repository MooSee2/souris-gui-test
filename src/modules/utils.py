datetime_conditional = [
    {
        "if": {
            "column_id": "datetime",
        },
        "backgroundColor": "#fafafa",
        "verticalAlign": "middle",
    },
]


def make_reservoir_approved_conditionals(stations=None):
    if stations is None:
        stations = {
            "05NA006",
            "05NB020",
            "05NB016",
            "05NC002",
            "05ND012",
        }
    return [
        {
            "if": {
                "filter_query": f'{{{station}_approval}} eq "approved"',
                "column_id": f"{station}_approval",
            },
            "backgroundColor": "#337538",
            "color": "white",
        }
        for station in stations
    ]


def make_reservoir_unapproved_conditionals(stations=None):
    if stations is None:
        stations = {
            "05NA006",
            "05NB020",
            "05NB016",
            "05NC002",
            "05ND012",
        }
    return [
        {
            "if": {
                "filter_query": f'{{{station}_approval}} eq "Provisional"',
                "column_id": f"{station}_approval",
            },
            "backgroundColor": "#0072B2",
            "color": "white",
            "verticalAlign": "middle",
        }
        for station in stations
    ]
