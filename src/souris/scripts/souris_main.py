"""
****************************************************************************************
This python script calculates the natural flow on the Souris basin, and produces a
 .xlsx apportionment report in the natural flow report folder.

The script scrapes data from ECCC AQ NG, Water Office, climate.weather.gc.ca,
 and USGS NWIS, based on station numbers and date ranges.

User settings are loaded through a .env file that is not tracked in Git.

Version 1.0 - Brianna Vaagen, ECCC, (July 2022),
 based on preliminary version made by Habeeb Balogun (March 2020)

Version 2.0- Jonathan O'Connell, joconnell@usgs.gov (November 2023)

*WARNING: this script is written based off the 2022 Souris Apportionment Procedures,
 and maybe not produce accurate results for prior years*
"""

import os
from datetime import datetime as dt
from pathlib import Path

import pandas as pd
from loguru import logger

import souris.core.configs as cfg
import souris.core.core_meteo as met
import souris.core.core_reservoirs as res
import souris.utils.reservoir_capacity as rcap
import souris.utils.utilities as util
from modules.data_layer.model_inputs import SourisModelInputs


# TODO send script version num to excel
def main(
    model_inputs: SourisModelInputs,
) -> int:
    CMS_TO_DAM3days = 86.4  # 0.001 * 86400
    MM_TO_METERS = 0.001
    M_TO_DAM = 0.1
    RESERVOIR_SEEPAGE = 0.015
    TEMPLATE_PATH = Path("souris/data/xlsx_template/BLANK_souris_natural_flow_apportionment_report.xlsx")

    with logger.catch():
        dt_dt_now = dt.now()
        dt_now = dt_dt_now.strftime("%Y-%m-%d %H:%M:%S.%f")
        logger.info(f"Program starting at {dt_now}")
        logger.debug(f"CWD: {os.getcwd()}")

        # ca_reservoir_stations = (
        #     "05NA006",
        #     "05NB020",
        #     "05NB016",
        #     "05NC002",
        #     "05ND012",
        # )
        # ca_discharge_stations = (
        #     "05NA003",
        #     "05NB001",
        #     "05NB011",
        #     "05NB014",
        #     "05NB018",
        #     "05NB033",
        #     "05NB035",
        #     "05NB036",
        #     "05NB038",
        #     "05NB039",
        #     "05NB040",
        #     "05NB041",
        # )
        # nwis_discharge_stations = (
        #     "05113600",
        #     "05114000",
        # )

        logger.info("Reading Inputs...")
        # These are adapter classes so I don't have to rewrite some of the below code.
        # If new reported flows are added then then it would be best to add them here
        # to use them in the code below.
        reported_flows = cfg.Boxes(
            box_5b=model_inputs.pipeline,
            box_11=model_inputs.long_creek_minor_project_diversion,
            box_12=model_inputs.us_diversion,
            box_16=model_inputs.weyburn_pumpage,
            box_18=model_inputs.weyburn_return_flow,
            box_25=model_inputs.upper_souris_minor_diversion,
            box_27=model_inputs.estevan_net_pumpage,
            box_28=model_inputs.short_creek_diversions,
            box_29=model_inputs.lower_souris_minor_diversion,
            box_37=model_inputs.moose_mountain_minor_diversion,
        )
        souris_dates = cfg.Dates(
            wateryear=model_inputs.appor_year,
            start_apportion=model_inputs.appor_start,
            end_apportion=model_inputs.appor_end,
            evap_start_date=model_inputs.evap_start,
            evap_end_date=model_inputs.evap_end,
        )
        logger.info("Inputs Read!")

        # Met data
        roughbark_meteo_daily = model_inputs.met[[col for col in model_inputs.met.columns if "05NB016" in col]]
        handsworth_meteo_daily = model_inputs.met[[col for col in model_inputs.met.columns if "05NCM01" in col]]

        # Precip data
        precip_daily = pd.concat([roughbark_meteo_daily["05NB016_precip"], handsworth_meteo_daily["05NCM01_precip"]], axis=1)
        precip_daily.loc[precip_daily.index.month.isin([1, 2, 3, 4, 11, 12])] = 0

        precip_monthly = util.rename_monthly_index(precip_daily.resample("ME").sum()) * MM_TO_METERS

        # -----------------------------------------------------------------------------------------#
        #                                    Penman Calculations                                   #
        # -----------------------------------------------------------------------------------------#
        # Perform the penman calculation for both the Roughbark and Handsworth stations
        # Monthly evaporation is determined by summing the daily averages for the associated month
        logger.info("Calculating reservoir loss...")
        (
            roughbark_penman_monthly_sum,
            handsworth_penman_monthly_sum,
            roughbark_meteo_daily,
            handsworth_meteo_daily,
        ) = met.process_penman(
            dates=souris_dates,
            roughbark_meteo_daily=roughbark_meteo_daily,
            handsworth_meteo_daily=handsworth_meteo_daily,
        )

        # -----------------------------------------------------------------------------------------#
        #                                  Reservoir Loss Calculations                             #
        # -----------------------------------------------------------------------------------------#
        """A constant monthly seepage value (RESERVOIR_SEEPAGE) of 0.015 m is assumed year-round
        Calculate the net evaporation:
        evap (m) - precip (m) and add seepage (m) then convert m to dam"""
        roughbark_loss = (roughbark_penman_monthly_sum["penman"] - precip_monthly["05NB016_precip"] + RESERVOIR_SEEPAGE) * M_TO_DAM

        handsworth_loss = (handsworth_penman_monthly_sum["penman"] - precip_monthly["05NCM01_precip"] + RESERVOIR_SEEPAGE) * M_TO_DAM

        # oxbow_loss = (handsworth_penman_monthly_sum["penman"] - precip_monthly["oxbow_precip"] + RESERVOIR_SEEPAGE) * M_TO_DAM

        ############################################################################################
        #                                  End Reservoir Loss Calculations                         #
        ############################################################################################

        # # -----------------------------------------------------------------------------------------#
        # #                              Assign reservoir Stage-Area-Capacities                      #
        # # -----------------------------------------------------------------------------------------#
        # May need to break up reservoir data into the {staid: df} format to reuse this function.
        reservoir_sacs_daily, reservoir_sacs_monthly = res.process_reservoir_sacs(
            reservoir_elevation_daily,
            wateryear=souris_dates.wateryear,
        )

        # -----------------------------------------------------------------------------------------#
        #                                  Box Calculations                                        #
        # -----------------------------------------------------------------------------------------#
        logger.info("Begin box calculations...")
        # * 1.1.1 Larsen Reservoir Storage Change
        boxes["box1"] = reservoir_sacs_daily["05NA006"]["capacity_dam3"].iloc[-1] - reservoir_sacs_daily["05NA006"]["capacity_dam3"].iloc[0]
        # * 1.1.2 Larsen Reservoir Net Evaporation & Seepage
        boxes["box2"] = (reservoir_sacs_monthly["05NA006"]["area_dam2"] * roughbark_loss).sum()
        # * 1.1.3 Larsen Reservoir Diversion
        boxes["box3"] = boxes["box1"] + boxes["box2"]
        # * 1.2 Town of Radville Pumpage
        # boxes["box4"] = 0  # box 4 is obsolete as of 2017
        boxes["box5a"] = int(discharge_daily["05113600"].sum().sum() * CMS_TO_DAM3days)
        # * 1.3.2 Long Creek near Estevan
        boxes["box6"] = discharge_daily["05NB001"].sum().sum() * CMS_TO_DAM3days
        # * 1.3.3 Estevan Pipeline
        # boxes["box7"] = 0  # box 7 is obsolete as of 2021
        # * 1.3.4 Diversion Canal
        boxes["box8"] = discharge_daily["05NB038"].sum().sum() * CMS_TO_DAM3days
        # * 1.3.5 Boundary Reservoir Total Outflow
        boxes["box9"] = boxes["box6"] + boxes["box8"]
        # * 1.3.6	Boundary Reservoir Diversion
        boxes["box10"] = (boxes["box5a"] + reported_flows.box_5b) - boxes["box9"]
        # * 1.6 Total Diversion Long Creek
        boxes["box13"] = boxes["box3"] + boxes["box10"] + reported_flows.box_11 + reported_flows.box_12
        # * 2.1.1 Nickle Lake Reservoir Storage Change
        boxes["box14"] = reservoir_sacs_daily["05NB020"]["capacity_dam3"].iloc[-1] - reservoir_sacs_daily["05NB020"]["capacity_dam3"].iloc[0]
        # * 2.1.2 Nickle Lake Reservoir Net Evaporation & Seepage
        boxes["box15"] = (reservoir_sacs_monthly["05NB020"]["area_dam2"] * roughbark_loss).sum()
        # * 2.1.4 Nickle Lake Reservoir Diversion
        boxes["box17"] = boxes["box14"] + boxes["box15"] + reported_flows.box_16
        # * 2.3.1 Roughbark Reservoir Storage Change
        boxes["box19"] = reservoir_sacs_daily["05NB016"]["capacity_dam3"].iloc[-1] - reservoir_sacs_daily["05NB016"]["capacity_dam3"].iloc[0]
        # * 2.3.2 Roughbark Reservoir Net Evaporation & Seepage
        boxes["box20"] = (reservoir_sacs_monthly["05NB016"]["area_dam2"] * roughbark_loss).sum()
        # * 2.3 Roughbark Reservoir Depletion, box20_roughbark_netloss includes seepage calculation
        boxes["box21"] = boxes["box19"] + boxes["box20"]
        """
        Rafferty inflow is the summation of volumes from:
        Jewel Creek near Goodwater: 05NB014
        Cooke Creek near Goodwater: 05NB035
        Boundary Reservoir Diversion Canal: 05NB038
        Souris River near Ralph: 05NB040
        Roughbark Creek above Rafferty Res.: 05NB041

        AND three ungaged stations with estimated flows as follows:
        One ungaged tributary estimation is based on Mosley Creek: 05NB033
        Two ungaged tributary estimations are based on Cook Creek near Goodwater: 05NB035

        The total inflow can be calulated with the following equation from page 15:
        Rafferty inflow = 05NB014 + 05NB038 + 05NB039 + 05NB040 + 05NB041 + 2*05NB033 + 3*05NB035
        """
        normal_staids = ["05NB014", "05NB038", "05NB039", "05NB040", "05NB041"]
        # * 2.4 Rafferty Reservoir Depletion
        boxes["box22"] = 0
        for station in normal_staids:
            boxes["box22"] += discharge_daily[station].sum().sum()

        """Estimate the three ungaged tributaries with Mosley and Cook
        discharge data and convert all to dam3"""
        boxes["box22"] += discharge_daily["05NB033"].sum().sum() * 2
        boxes["box22"] += discharge_daily["05NB035"].sum().sum() * 3
        boxes["box22"] *= CMS_TO_DAM3days

        # * 2.4.2 Rafferty Reservoir Outflow
        if reported_flows.wateryear == 2023:
            # Special values for 2023 comuputation.  Flush line = 63 DAM3, Rafferty -> Estevan pipeline = 1468 DAM3
            boxes["box23a"] = discharge_daily["05NB036"].sum().sum() * CMS_TO_DAM3days + 63 + 1468
        else:
            boxes["box23a"] = discharge_daily["05NB036"].sum().sum() * CMS_TO_DAM3days

        # * 2.4.3 Rafferty Reservoir Diversion
        boxes["box24"] = boxes["box22"] - (boxes["box23a"] + reported_flows.box_5b)
        # * 2.6 Total Diversion Upper Souris River
        boxes["box26"] = boxes["box17"] - reported_flows.box_18 + boxes["box21"] + boxes["box24"] + reported_flows.box_25

        # * 3.4 Total Diversion Lower Souris River
        if reported_flows.wateryear == 2023:
            # Special values for 2023 comuputation.  Duck pond release = 345 DAM3
            reported_flows.box_27 = reported_flows.box_27 - 345
        else:
            reported_flows.box_27 = reported_flows.box_27

        boxes["box30"] = reported_flows.box_27 + reported_flows.box_28 + reported_flows.box_29
        # * 4.1.1 Moose Mountain Lake Storage Change
        boxes["box31"] = reservoir_sacs_daily["05NC002"]["capacity_dam3"].iloc[-1] - reservoir_sacs_daily["05NC002"]["capacity_dam3"].iloc[0]
        # * 4.1.2 Moose Mountain Lake Net Evaporation & Seepage
        boxes["box32"] = (reservoir_sacs_monthly["05NC002"]["area_dam2"] * handsworth_loss).sum()
        # * 4.1.3 Moose Mountain Lake Diversion
        boxes["box33"] = boxes["box31"] + boxes["box32"]
        # * 4.2.1 Grant Devine Reservoir Storage Change
        boxes["box34"] = reservoir_sacs_daily["05ND012"]["capacity_dam3"].iloc[-1] - reservoir_sacs_daily["05ND012"]["capacity_dam3"].iloc[0]
        # * 4.2.2 Grant Devine Reservoir Net Evaporation & Seepage
        boxes["box35"] = (reservoir_sacs_monthly["05ND012"]["area_dam2"] * oxbow_loss).sum()
        # * 4.2 Grant Devine Reservoir
        boxes["box36"] = boxes["box34"] + boxes["box35"]
        # * 4.4 Total Diversions Moose Mountain Creek Basin
        boxes["box38"] = boxes["box33"] + boxes["box36"] + reported_flows.box_37
        # * 5.1 Yellow Grass Ditch
        boxes["box39"] = discharge_daily["05NB011"].sum().sum() * CMS_TO_DAM3days
        # * 5.2 Tatagwa Lake Drain
        boxes["box40"] = discharge_daily["05NB018"].sum().sum() * CMS_TO_DAM3days
        # * 5.3 Total Additions
        boxes["box41"] = boxes["box39"] + boxes["box40"]
        # * 6.1 Total Diversion Souris River Basin
        boxes["box42"] = boxes["box13"] + boxes["box26"] + boxes["box30"] + boxes["box38"]
        # * 6.2 Recorded Flow at Sherwood
        boxes["box43"] = discharge_daily["05114000"].sum().sum() * CMS_TO_DAM3days
        # * 6.3 Natural Flow at Sherwood
        boxes["box44"] = boxes["box42"] + boxes["box43"] - boxes["box41"]
        darling_condition = rcap.lake_darling_condition(start_date=souris_dates.start_apportion, sherwood=boxes["box44"])
        # * 6.4 U.S. Share at Sherwood – 50% vs 40% Note: True=1, False=0
        boxes["box45a"] = 0.4 * boxes["box44"] if darling_condition else 0
        boxes["box45b"] = 0 if darling_condition else 0.5 * boxes["box44"]
        boxes["box46"] = reported_flows.box_12 + reported_flows.box_28 + boxes["box43"]
        # * 6.6 Surplus or Deficit to U.S.
        boxes["box47a"] = boxes["box46"] - boxes["box45a"] if boxes["box45a"] else 0
        boxes["box47b"] = boxes["box46"] - boxes["box45b"] if boxes["box45b"] else 0
        # * 7.1 Recorded Flow at Western Crossing
        boxes["box48"] = discharge_daily["05NA003"].sum().sum() * CMS_TO_DAM3days
        # * 7.2 Recorded Flow at Eastern Crossing
        boxes["box49"] = discharge_daily["05113600"].sum().sum() * CMS_TO_DAM3days
        """If the box50 difference is positive,
        then more water was delivered annually from the U.S. than consumed and Recommendation 2 is met."""
        # * 7.3 Surplus or Deficit from U.S.
        boxes["box50"] = boxes["box49"] - boxes["box48"]

        boxes = {key: int(item) for key, item in boxes.items()}

        ############################################################################################
        #                                  End Box Calculations                                    #
        ############################################################################################

        # -----------------------------------------------------------------------------------------#
        #                                  Process data for Report                                 #
        # -----------------------------------------------------------------------------------------#
        """All this can probably go"""
        # Combine all daily dischage
        daily_idx = pd.date_range(souris_dates.start_apportion, souris_dates.end_apportion, freq="D")
        master_daily_df = pd.DataFrame(index=daily_idx, columns=["temp"])

        reservoir_elevation_daily = {staid: dataframe.rename(columns={"value": f"{staid}_elevation"}) for staid, dataframe in reservoir_elevation_daily.items()}
        discharge_daily = {staid: dataframe.rename(columns={"value": f"{staid}_discharge"}) for staid, dataframe in discharge_daily.items()}
        reservoir_elevations_monthly = {staid: dataframe.rename(columns={"value": f"{staid}_elevation"}) for staid, dataframe in reservoir_sacs_monthly.items()}
        reservoir_elevations_monthly = {staid: dataframe[[f"{staid}_elevation"]].copy() for staid, dataframe in reservoir_elevations_monthly.items()}

        for dataframe in discharge_daily.values():
            dataframe = dataframe * CMS_TO_DAM3days
            master_daily_df = master_daily_df.join(dataframe)

        for dataframe in reservoir_elevation_daily.values():
            master_daily_df = master_daily_df.join(dataframe)
        del master_daily_df["temp"]

        monthly_idx = pd.date_range(souris_dates.start_apportion, souris_dates.end_apportion, freq="ME")
        master_monthly_df = pd.DataFrame(index=monthly_idx, columns=["temp"])
        master_monthly_df = master_monthly_df.set_index(monthly_idx.strftime("%Y-%m"))

        for dataframe in reservoir_elevations_monthly.values():
            master_monthly_df = master_monthly_df.join(dataframe.round(3))
        del master_monthly_df["temp"]

        # Combine all meteo station data into dict to send to report
        roughbark_meteo_daily = roughbark_meteo_daily.join(precip_daily["05NB016_precip"])
        handsworth_meteo_daily = handsworth_meteo_daily.join(precip_daily["05NCM01_precip"])
        precip_daily = {staid: dataframe.rename(columns={"value": staid}) for staid, dataframe in precip_daily.items()}
        master_meteo_dict = {
            "05NB016": roughbark_meteo_daily,
            "05NCM01": handsworth_meteo_daily,
            "oxbow": precip_daily["oxbow_precip"],
        }

        # -----------------------------------------------------------------------------------------#
        #                                  Reporting                                               #
        # -----------------------------------------------------------------------------------------#
        logger.info("Apportionment Calculations Complete")

        logger.info("Writing Data to Excel Workbook...")
        report = util.souris_excel_writer(
            reported_flows=reported_flows,
            dates=souris_dates,
            boxes=boxes,
            daily_data=master_daily_df,
            monthly_elev_data=reservoir_elevations_monthly,
            daily_meteo_data=master_meteo_dict,
            approval_dict=approval_dict,
            report_template=TEMPLATE_PATH,
        )

        logger.info("Apportionment complete!")
        dt_now = dt.now().strftime("%Y-%m-%d %H:%M:%S.%f")
        logger.info(f"Program completed at {dt_now}")
        return report
        ############################################################################################
        #                                  End Reporting                                           #
        ############################################################################################


if __name__ == "__main__":
    exit(main())
