from src.components.tabs.reservoirs import make_reservoir_approved_conditionals, make_reservoir_unapproved_conditionals


def test_make_reservoir_approved_conditionals():
    stations = {
        "05NA006",
        # "05NB020",
        # "05NB016",
        # "05NC002",
        # "05ND012",
    }
    outputs = make_reservoir_approved_conditionals(stations=stations)
    expected = {
        "if": {
            "filter_query": '{05NA006_approval} eq "approved"',
            "column_id": "05NA006",
        },
        "backgroundColor": "#337538",
        "color": "white",
    }
    assert outputs[0] == expected


def test_make_reservoir_unapproved_conditionals():
    stations = {
        "05NA006",
        # "05NB020",
        # "05NB016",
        # "05NC002",
        # "05ND012",
    }
    outputs = make_reservoir_unapproved_conditionals(stations=stations)
    expected = {
        "if": {
            "filter_query": '{05NA006_approval} eq "Provisional"',
            "column_id": "05NA006",
        },
        "backgroundColor": "#0072B2",
        "color": "white",
        "verticalAlign": "middle",
    }
    assert outputs[0] == expected
