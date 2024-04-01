import src.app_data.test_data as td


def get_app_data(apportionment_year: int) -> tuple:
    return (
        td.make_reservoirs().to_dict("records"),
        td.discharge_data.to_dict("records"),
        td.met_data.to_dict("records"),
    )
