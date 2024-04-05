import app_data.test_data as td


def get_app_data(apportionment_year: int) -> tuple:
    return (
        td.make_dummy_data(
            stations={
                "05NA006",
                "05NB020",
                "05NB016",
                "05NC002",
                "05ND012",
            }
        ).to_dict("records"),
        td.make_dummy_data(
            stations={
                "05NB001",
                "05NB036",
                "05NB011",
                "05NB018",
                "05NA003",
                "05NB040",
                "05NB041",
                "05NB038",
                "05NB014",
                "05NB035",
                "05NB033",
                "05NB039",
            },
        ).to_dict("records"),
        td.make_dummy_data(
            stations={
                "1234_wind_speed",
                "1234_air_temp",
                "1234_sol_rad",
                "1234_rel_humidity",
                "1234_precip",
                "4321_wind_speed",
                "4321_air_temp",
                "4321_sol_rad",
                "4321_rel_humidity",
                "4321_precip",
            }
        ).to_dict("records"),
    )
