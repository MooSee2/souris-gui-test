# from src.components.tabs.reservoirs import _conditional_helper


def test__conditional_helper():
    station = "05NA006"
    # new_station = f"{{{station}}}"
    input_str = '{05NA006_approval} eq "approved"'
    split_str = input_str.split(" ")
    split_str[0] = f"{{{station}_approved}}"
    final_str = " ".join(split_str)
    ...


def test_make_reservoir_approvedl_conditionals():
    stations = {
        "05NA006",
        "05NB020",
        "05NB016",
        "05NC002",
        "05ND012",
    }
    output = [
        {
            "if": {
                "filter_query": f'{{{station}_approved}} eq "approved"',
                "column_id": "05NA006",
            },
            "backgroundColor": "#008000",
            "color": "white",
        }
        for station in stations
    ]
    ...
