from datetime import datetime as dt

current_year = dt.now().year
available_years = [{"label": year, "value": year} for year in range(2023, current_year + 1)]
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


################################################################
# These lists of dicts are used for making table column headers.
# Each item is a column and each 'name' is a row in the header and the id is the reference to access that column header.

# TODO finish approvals for all stations
discharge_station_names = [
    {"editable": False, "name": ["Discharge", " ", " ", "Date"], "id": "date"},
    {"name": ["Discharge", "Units: m\u00b3/s", "Long Creek near Estevan", "05NB001"], "id": "05NB001", "type": "numeric"},
    {"name": ["Discharge", "Units: m\u00b3/s", "Long Creek near Estevan", "05NB001"], "id": "05NB001_approval"},
    {"name": ["Discharge", "Units: m\u00b3/s", "Souris River below Rafterty", "05NB036"], "id": "05NB036", "type": "numeric"},
    {"name": ["Discharge", "Units: m\u00b3/s", "Souris River below Rafterty", "05NB036"], "id": "05NB036_approval"},
    {"name": ["Discharge", "Units: m\u00b3/s", "Yellowgrass Ditch", "05NB011"], "id": "05NB011", "type": "numeric"},
    {"name": ["Discharge", "Units: m\u00b3/s", "Yellowgrass Ditch", "05NB011"], "id": "05NB011_approval"},
    {"name": ["Discharge", "Units: m\u00b3/s", "Tatagra Lake Drain", "05NB018"], "id": "05NB018", "type": "numeric"},
    {"name": ["Discharge", "Units: m\u00b3/s", "Tatagra Lake Drain", "05NB018"], "id": "05NB018_approval"},
    {"name": ["Discharge", "Units: m\u00b3/s", "Long Creek at Western Crossing", "05NA003"], "id": "05NA003", "type": "numeric"},
    {"name": ["Discharge", "Units: m\u00b3/s", "Long Creek at Western Crossing", "05NA003"], "id": "05NA003_approval"},
    {"name": ["Discharge", "Units: m\u00b3/s", "Souris River near Ralph", "05NB040"], "id": "05NB040", "type": "numeric"},
    {"name": ["Discharge", "Units: m\u00b3/s", "Souris River near Ralph", "05NB040"], "id": "05NB040_approval"},
    {"name": ["Discharge", "Units: m\u00b3/s", "Roughbark Creek above Rafferty Res.", "05NB041"], "id": "05NB041", "type": "numeric"},
    {"name": ["Discharge", "Units: m\u00b3/s", "Roughbark Creek above Rafferty Res.", "05NB041"], "id": "05NB041_approval"},
    {"name": ["Discharge", "Units: m\u00b3/s", "Boundary Res. Diversion Canal", "05NB038"], "id": "05NB038", "type": "numeric"},
    {"name": ["Discharge", "Units: m\u00b3/s", "Boundary Res. Diversion Canal", "05NB038"], "id": "05NB038_approval"},
    {"name": ["Discharge", "Units: m\u00b3/s", "Jewel Creek near Goodwater", "05NB014"], "id": "05NB014", "type": "numeric"},
    {"name": ["Discharge", "Units: m\u00b3/s", "Jewel Creek near Goodwater", "05NB014"], "id": "05NB014_approval"},
    {"name": ["Discharge", "Units: m\u00b3/s", "Cooke Creek near Goodwater", "05NB035"], "id": "05NB035", "type": "numeric"},
    {"name": ["Discharge", "Units: m\u00b3/s", "Cooke Creek near Goodwater", "05NB035"], "id": "05NB035_approval"},
    {"name": ["Discharge", "Units: m\u00b3/s", "Moseley Creek near Halbrite", "05NB033"], "id": "05NB033", "type": "numeric"},
    {"name": ["Discharge", "Units: m\u00b3/s", "Moseley Creek near Halbrite", "05NB033"], "id": "05NB033_approval"},
    {"name": ["Discharge", "Units: m\u00b3/s", "Tributary near Outram", "05NB039"], "id": "05NB039", "type": "numeric"},
    {"name": ["Discharge", "Units: m\u00b3/s", "Tributary near Outram", "05NB039"], "id": "05NB039_approval"},
]


reservoir_station_names = [
    {"editable": False, "name": ["Reservoir Elevation", "Elevation: meters", " ", "Date"], "id": "date"},
    {"editable": True, "name": ["Reservoir Elevation", "Elevation: meters", "Larson", "05NA006"], "id": "05NA006", "type": "numeric"},
    {"editable": True, "name": ["Reservoir Elevation", "Elevation: meters", "Larson", "05NA006"], "id": "05NA006_approval"},
    {"editable": True, "name": ["Reservoir Elevation", "Elevation: meters", "Nickle Lake", "05NB020"], "id": "05NB020", "type": "numeric"},
    {"editable": True, "name": ["Reservoir Elevation", "Elevation: meters", "Nickle Lake", "05NB020"], "id": "05NB020_approval"},
    {"editable": True, "name": ["Reservoir Elevation", "Elevation: meters", "Roughbark", "05NB016"], "id": "05NB016", "type": "numeric"},
    {"editable": True, "name": ["Reservoir Elevation", "Elevation: meters", "Roughbark", "05NB016"], "id": "05NB016_approval"},
    {"editable": True, "name": ["Reservoir Elevation", "Elevation: meters", "Moose Mountain Lake", "05NC002"], "id": "05NC002", "type": "numeric"},
    {"editable": True, "name": ["Reservoir Elevation", "Elevation: meters", "Moose Mountain Lake", "05NC002"], "id": "05NC002_approval"},
    {"editable": True, "name": ["Reservoir Elevation", "Elevation: meters", "Grant Devine", "05ND012"], "id": "05ND012", "type": "numeric"},
    {"editable": True, "name": ["Reservoir Elevation", "Elevation: meters", "Grant Devine", "05ND012"], "id": "05ND012_approval"},
]

met_station_names = [
    {"editable": False, "name": ["Roughbark", " ", "Date"], "id": "date"},
    {"name": ["Roughbark", "Wind Speed", "m/s"], "id": "05NB016_wind_speed", "type": "numeric"},
    {"name": ["Roughbark", "Wind Speed", "m/s"], "id": "05NB016_wind_speed_approval"},
    {"name": ["Roughbark", "Air Temperature", "C"], "id": "05NB016_air_temp", "type": "numeric"},
    {"name": ["Roughbark", "Air Temperature", "C"], "id": "05NB016_air_temp_approval"},
    {"name": ["Roughbark", "Solar Radiation", "w/m\u00b2"], "id": "05NB016_sol_rad", "type": "numeric"},
    {"name": ["Roughbark", "Solar Radiation", "w/m\u00b2"], "id": "05NB016_sol_rad_approval"},
    {"name": ["Roughbark", "Relative Humidity", "%"], "id": "05NB016_rel_humidity", "type": "numeric"},
    {"name": ["Roughbark", "Relative Humidity", "%"], "id": "05NB016_rel_humidity_approval"},
    {"name": ["Roughbark", "Precipitation", "mm"], "id": "05NB016_precip", "type": "numeric"},
    {"name": ["Roughbark", "Precipitation", "mm"], "id": "05NB016_precip_approval"},
    {"name": ["Handsworth", "Wind Speed", "m/s"], "id": "05NCM01_wind_speed", "type": "numeric"},
    {"name": ["Handsworth", "Wind Speed", "m/s"], "id": "05NCM01_wind_speed_approval"},
    {"name": ["Handsworth", "Air Temperature", "C"], "id": "05NCM01_air_temp", "type": "numeric"},
    {"name": ["Handsworth", "Air Temperature", "C"], "id": "05NCM01_air_temp_approval"},
    {"name": ["Handsworth", "Solar Radiation", "w/m\u00b2"], "id": "05NCM01_sol_rad", "type": "numeric"},
    {"name": ["Handsworth", "Solar Radiation", "w/m\u00b2"], "id": "05NCM01_sol_rad_approval"},
    {"name": ["Handsworth", "Relative Humidity", "%"], "id": "05NCM01_rel_humidity", "type": "numeric"},
    {"name": ["Handsworth", "Relative Humidity", "%"], "id": "05NCM01_rel_humidity_approval"},
    {"name": ["Handsworth", "Precipitation", "mm"], "id": "05NCM01_precip", "type": "numeric"},
    {"name": ["Handsworth", "Precipitation", "mm"], "id": "05NCM01_precip_approval"},
]
