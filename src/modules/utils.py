datetime_conditional = [
    {
        "if": {
            "column_id": "datetime",
        },
        "backgroundColor": "#fafafa",
        "verticalAlign": "middle",
    },
]


def make_conditionals(stations: set):
    return make_approved_conditionals(stations) + make_unapproved_conditionals(stations)


def make_approved_conditionals(stations):
    return [
        {
            "if": {
                "filter_query": f'{{{station}_approval}} eq "approved"',
                "column_id": f"{station}_approval",
            },
            "backgroundColor": "#D1E5F0",
            "color": "white",
        }
        for station in stations
    ]


def make_unapproved_conditionals(stations):
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
