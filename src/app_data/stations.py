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


################################################################
# These lists of dicts are used for making table column headers.
# Each item is a column and each 'name' is a row in the header and the id is the reference to access that column header.

# TODO finish approvals for all stations
discharge_station_names = [
    {"name": ["Discharge", " ", " ", "Datetime"], "id": "datetime"},
    {"name": ["Discharge", "Units: m\u00b3/s", "Long Creek near Estevan", "05NB001"], "id": "05NB001"},
    {"name": ["Discharge", "Units: m\u00b3/s", "Long Creek near Estevan", "05NB001 Approval"], "id": "05NB001_approval"},
    {"name": ["Discharge", "Units: m\u00b3/s", "Souris River below Rafterty", "05NB036"], "id": "05NB036"},
    {"name": ["Discharge", "Units: m\u00b3/s", "Souris River below Rafterty", "05NB036 Approval"], "id": "05NB036_approval"},
    {"name": ["Discharge", "Units: m\u00b3/s", "Yellowgrass Ditch", "05NB011"], "id": "05NB011"},
    {"name": ["Discharge", "Units: m\u00b3/s", "Yellowgrass Ditch", "05NB011 Approval"], "id": "05NB011_approval"},
    {"name": ["Discharge", "Units: m\u00b3/s", "Tatagra Lake Drain", "05NB018"], "id": "05NB018"},
    {"name": ["Discharge", "Units: m\u00b3/s", "Tatagra Lake Drain", "05NB018 Approval"], "id": "05NB018_approval"},
    {"name": ["Discharge", "Units: m\u00b3/s", "Long Creek at Western Crossing", "05NA003"], "id": "05NA003"},
    {"name": ["Discharge", "Units: m\u00b3/s", "Long Creek at Western Crossing", "05NA003 Approval"], "id": "05NA003_approval"},
    {"name": ["Discharge", "Units: m\u00b3/s", "Souris River near Ralph", "05NB040"], "id": "05NB040"},
    {"name": ["Discharge", "Units: m\u00b3/s", "Souris River near Ralph", "05NB040 Approval"], "id": "05NB040_approval"},
    {"name": ["Discharge", "Units: m\u00b3/s", "Roughbark Creek above Rafferty Res.", "05NB041"], "id": "05NB041"},
    {"name": ["Discharge", "Units: m\u00b3/s", "Roughbark Creek above Rafferty Res.", "05NB041 Approval"], "id": "05NB041_approval"},
    {"name": ["Discharge", "Units: m\u00b3/s", "Boundary Res. Diversion Canal", "05NB038"], "id": "05NB038"},
    {"name": ["Discharge", "Units: m\u00b3/s", "Boundary Res. Diversion Canal", "05NB038 Approval"], "id": "05NB038_approval"},
    {"name": ["Discharge", "Units: m\u00b3/s", "Jewel Creek near Goodwater", "05NB014"], "id": "05NB014"},
    {"name": ["Discharge", "Units: m\u00b3/s", "Jewel Creek near Goodwater", "05NB014 Approval"], "id": "05NB014_approval"},
    {"name": ["Discharge", "Units: m\u00b3/s", "Cooke Creek near Goodwater", "05NB035"], "id": "05NB035"},
    {"name": ["Discharge", "Units: m\u00b3/s", "Cooke Creek near Goodwater", "05NB035 Approval"], "id": "05NB035_approval"},
    {"name": ["Discharge", "Units: m\u00b3/s", "Moseley Creek near Halbrite", "05NB033"], "id": "05NB033"},
    {"name": ["Discharge", "Units: m\u00b3/s", "Moseley Creek near Halbrite", "05NB033 Approval"], "id": "05NB033_approval"},
    {"name": ["Discharge", "Units: m\u00b3/s", "Tributary near Outram", "05NB039"], "id": "05NB039"},
    {"name": ["Discharge", "Units: m\u00b3/s", "Tributary near Outram", "05NB039 Approval"], "id": "05NB039_approval"},
]


reservoir_station_names = [
    {"editable": False, "name": ["Reservoir Elevation", "Elevation: meters", " ", "Datetime"], "id": "datetime"},
    {"editable": True, "name": ["Reservoir Elevation", "Elevation: meters", "Larson", "05NA006"], "id": "05NA006"},
    {"editable": True, "name": ["Reservoir Elevation", "Elevation: meters", "Larson", "05NA006"], "id": "05NA006_approval"},
    {"editable": True, "name": ["Reservoir Elevation", "Elevation: meters", "Nickle Lake", "05NB020"], "id": "05NB020"},
    {"editable": True, "name": ["Reservoir Elevation", "Elevation: meters", "Nickle Lake", "05NB020"], "id": "05NB020_approval"},
    {"editable": True, "name": ["Reservoir Elevation", "Elevation: meters", "Roughbark", "05NB016"], "id": "05NB016"},
    {"editable": True, "name": ["Reservoir Elevation", "Elevation: meters", "Roughbark", "05NB016"], "id": "05NB016_approval"},
    {"editable": True, "name": ["Reservoir Elevation", "Elevation: meters", "Moose Mountain Lake", "05NC002"], "id": "05NC002"},
    {"editable": True, "name": ["Reservoir Elevation", "Elevation: meters", "Moose Mountain Lake", "05NC002"], "id": "05NC002_approval"},
    {"editable": True, "name": ["Reservoir Elevation", "Elevation: meters", "Grant Devine", "05ND012"], "id": "05ND012"},
    {"editable": True, "name": ["Reservoir Elevation", "Elevation: meters", "Grant Devine", "05ND012"], "id": "05ND012_approval"},
]

met_station_names = [
    {"name": ["Roughbark", " ", "Datetime"], "id": "datetime"},
    {"name": ["Roughbark", "Wind Speed", "m/s"], "id": "1234_wind_speed"},
    {"name": ["Roughbark", "Wind Speed Approval", "m/s"], "id": "1234_wind_speed_approval"},
    {"name": ["Roughbark", "Air Temperature", "C"], "id": "1234_air_temp"},
    {"name": ["Roughbark", "Air Temperature Approval", "C"], "id": "1234_air_temp_approval"},
    {"name": ["Roughbark", "Solar Radiation", "w/m\u00b2"], "id": "1234_sol_rad"},
    {"name": ["Roughbark", "Solar Radiation Approval", "w/m\u00b2"], "id": "1234_sol_rad_approval"},
    {"name": ["Roughbark", "Relative Humidity", "%"], "id": "1234_rel_humidity"},
    {"name": ["Roughbark", "Relative Humidity Approval", "%"], "id": "1234_rel_humidity_approval"},
    {"name": ["Roughbark", "Precipitation", "mm"], "id": "1234_precip"},
    {"name": ["Roughbark", "Precipitation Approval", "mm"], "id": "1234_precip_approval"},
    {"name": ["Handsworth", "Wind Speed", "m/s"], "id": "4321_wind_speed"},
    {"name": ["Handsworth", "Wind Speed Approval", "m/s"], "id": "4321_wind_speed_approval"},
    {"name": ["Handsworth", "Air Temperature", "C"], "id": "4321_air_temp"},
    {"name": ["Handsworth", "Air Temperature Approval", "C"], "id": "4321_air_temp_approval"},
    {"name": ["Handsworth", "Solar Radiation", "w/m\u00b2"], "id": "4321_sol_rad"},
    {"name": ["Handsworth", "Solar Radiation Approval", "w/m\u00b2"], "id": "4321_sol_rad_approval"},
    {"name": ["Handsworth", "Relative Humidity", "%"], "id": "4321_rel_humidity"},
    {"name": ["Handsworth", "Relative Humidity Approval", "%"], "id": "4321_rel_humidity_approval"},
    {"name": ["Handsworth", "Precipitation", "mm"], "id": "4321_precip"},
    {"name": ["Handsworth", "Precipitation Approval", "mm"], "id": "4321_precip_approval"},
]
