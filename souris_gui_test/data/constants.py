from datetime import datetime as dt

current_year = dt.now().year
available_years = [{"label": year, "value": year} for year in range(2022, current_year + 1)]
available_years.reverse()

stations = {
    ("Long Creek near Estevan", "05NB001", "Rivers"),
    ("Souris River below Rafterty", "05NB036", "Rivers"),
    ("Yellowgrass Ditch", "05NB011", "Rivers"),
    ("Tatagra Lake Drain", "05NB018", "Rivers"),
    ("Long Creek at Western Crossing", "05NA003", "Rivers"),
    ("Souris River near Ralph", "05NB040", "Rivers"),
    ("Roughbark Creek above Rafferty Res.", "05NB041", "Rivers"),
    ("Boundary Res. Diversion Canal", "05NB038", "Rivers"),
    ("Jewel Creek near Goodwater", "05NB014", "Rivers"),
    ("Cooke Creek near Goodwater", "05NB035", "Rivers"),
    ("Moseley Creek near Halbrite", "05NB033", "Rivers"),
    ("Tributary near Outram", "05NB039", "Rivers"),
    ("Larson", "05NA006", "Reservoirs"),
    ("Nickle Lake", "05NB020", "Reservoirs"),
    ("Roughbark", "05NB016", "Reservoirs"),
    ("Moose Mountain Lake", "05NC002", "Reservoirs"),
    ("Grant Devine", "05ND012", "Reservoirs"),
    ("Roughbark Wind Speed, Units: m/s", "1234_wind_speed", "Met Stations"),
    ("Roughbark Air Temperature, Units: C", "1234_air_temp", "Met Stations"),
    ("Roughbark Solar Radiation, Units: w/m", "1234_sol_rad", "Met Stations"),
    ("Roughbark Relative Humidity, Units: %", "1234_rel_humidity", "Met Stations"),
    ("Roughbark Precipitation, Units: mm", "1234_precip", "Met Stations"),
    ("Handsworth Wind Speed, Units: m/s", "4321_wind_speed", "Met Stations"),
    ("Handsworth Air Temperature, Units: C", "4321_air_temp", "Met Stations"),
    ("Handsworth Solar Radiation, Units: w/m\u00b2", "4321_sol_rad", "Met Stations"),
    ("Handsworth Relative Humidity, Units: %", "4321_rel_humidity", "Met Stations"),
    ("Handsworth Precipitation, Units: mm", "4321_precip", "Met Stations"),
}

discharge_station_names = [
    {"name": ["Discharge", "Units: m\u00b3/s", "Long Creek near Estevan", "05NB001"], "id": "05NB001"},
    {"name": ["Discharge", "Units: m\u00b3/s", "Souris River below Rafterty", "05NB036"], "id": "05NB036"},
    {"name": ["Discharge", "Units: m\u00b3/s", "Yellowgrass Ditch", "05NB011"], "id": "05NB011"},
    {"name": ["Discharge", "Units: m\u00b3/s", "Tatagra Lake Drain", "05NB018"], "id": "05NB018"},
    {"name": ["Discharge", "Units: m\u00b3/s", "Long Creek at Western Crossing", "05NA003"], "id": "05NA003"},
    {"name": ["Discharge", "Units: m\u00b3/s", "Souris River near Ralph", "05NB040"], "id": "05NB040"},
    {"name": ["Discharge", "Units: m\u00b3/s", "Roughbark Creek above Rafferty Res.", "05NB041"], "id": "05NB041"},
    {"name": ["Discharge", "Units: m\u00b3/s", "Boundary Res. Diversion Canal", "05NB038"], "id": "05NB038"},
    {"name": ["Discharge", "Units: m\u00b3/s", "Jewel Creek near Goodwater", "05NB014"], "id": "05NB014"},
    {"name": ["Discharge", "Units: m\u00b3/s", "Cooke Creek near Goodwater", "05NB035"], "id": "05NB035"},
    {"name": ["Discharge", "Units: m\u00b3/s", "Moseley Creek near Halbrite", "05NB033"], "id": "05NB033"},
    {"name": ["Discharge", "Units: m\u00b3/s", "Tributary near Outram", "05NB039"], "id": "05NB039"},
]

reservoir_station_names = [
    {"name": ["Reservoir Elevation", "Elevation: meters", "Station ID", "Datetime"], "id": "datetime"},
    {"name": ["Reservoir Elevation", "Elevation: meters", "05NA006", "Larson"], "id": "05NA006"},
    {"name": ["Reservoir Elevation", "Elevation: meters", "05NB020", "Nickle Lake"], "id": "05NB020"},
    {"name": ["Reservoir Elevation", "Elevation: meters", "05NB016", "Roughbark"], "id": "05NB016"},
    {"name": ["Reservoir Elevation", "Elevation: meters", "05NC002", "Moose Mountain Lake"], "id": "05NC002"},
    {"name": ["Reservoir Elevation", "Elevation: meters", "05ND012", "Grant Devine"], "id": "05ND012"},
]

# {"name": "", "id": ""},
met_station_names = [
    # {"name": ["Datetime", "Units", "l"], "id": "index"},
    {"name": ["Roughbark", "Units: m/s", "Wind Speed"], "id": "1234_wind_speed"},
    {"name": ["Roughbark", "Units: C", "Air Temperature"], "id": "1234_air_temp"},
    {"name": ["Roughbark", "Units: w/m\u00b2", "Solar Radiation"], "id": "1234_sol_rad"},
    {"name": ["Roughbark", "Units: %", "Relative Humidity"], "id": "1234_rel_humidity"},
    {"name": ["Roughbark", "Units: mm", "Precipitation"], "id": "1234_precip"},
    {"name": ["Handsworth", "Units: m/s", "Wind Speed"], "id": "4321_wind_speed"},
    {"name": ["Handsworth", "Units: C", "Air Temperature"], "id": "4321_air_temp"},
    {"name": ["Handsworth", "Units: w/m\u00b2", "Solar Radiation"], "id": "4321_sol_rad"},
    {"name": ["Handsworth", "Units: %", "Relative Humidity"], "id": "4321_rel_humidity"},
    {"name": ["Handsworth", "Units: mm", "Precipitation"], "id": "4321_precip"},
]
