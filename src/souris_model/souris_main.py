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
from io import BytesIO

import pandas as pd
from loguru import logger

import souris_model.core.core_meteo as met
import souris_model.core.core_reservoirs as res
import souris_model.utils.excel_writer as excel
import souris_model.utils.reservoir_capacity as rcap
import souris_model.utils.utilities as util
import souris_model.core.boxes as bx
import souris_model.core.dates as dates
from modules.data_layer.model_inputs import SourisModelInputs


# TODO send script version num to excel
def main(
    model_inputs: SourisModelInputs,
) -> tuple[BytesIO, bx.Boxes]:
    CMS_TO_DAM3days = 86.4  # 0.001 * 86400
    MM_TO_METERS = 0.001
    M_TO_DAM = 0.1
    RESERVOIR_SEEPAGE = 0.015

    with logger.catch():
        dt_dt_now = dt.now()
        dt_now = dt_dt_now.strftime("%Y-%m-%d %H:%M:%S.%f")
        logger.info(f"Program starting at {dt_now}")
        logger.debug(f"CWD: {os.getcwd()}")

        discharge_stations = (
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
            "05113600",
            "05114000",
        )

        discharge = model_inputs.discharge
        reservoirs = model_inputs.reservoirs
        met_data = model_inputs.met

        # Adapter class for Dates.
        souris_dates = dates.Dates(
            wateryear=model_inputs.appor_year,
            start_apportion=model_inputs.appor_start,
            end_apportion=model_inputs.appor_end,
            evap_start_date=model_inputs.evap_start,
            evap_end_date=model_inputs.evap_end,
        )

        # Met data
        roughbark_meteo_daily = met_data[[col for col in met_data.columns if "05NB016" in col]]
        handsworth_meteo_daily = met_data[[col for col in met_data.columns if "05NCM01" in col]]
        oxbow_precip_daily = met_data[[col for col in met_data.columns if "oxbow" in col]]

        # Precip data only
        precip_daily = pd.concat([roughbark_meteo_daily["05NB016_precip"], handsworth_meteo_daily["05NCM01_precip"], oxbow_precip_daily["oxbow_precip"]], axis=1)
        precip_monthly = util.rename_monthly_index(precip_daily.resample("ME").sum())

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

        # ----------------------------------------------------------------------------------------#
        #                                  Reservoir Loss Calculations                            #
        # ----------------------------------------------------------------------------------------#
        """A constant monthly seepage value (RESERVOIR_SEEPAGE) of 0.015 m is assumed year-round
        Calculate the net evaporation:
        evap (m) - precip (m) and add seepage (m) then convert m to dam"""
        roughbark_loss = (roughbark_penman_monthly_sum["penman"] * MM_TO_METERS - precip_monthly["05NB016_precip"] * MM_TO_METERS + RESERVOIR_SEEPAGE) * M_TO_DAM
        handsworth_loss = (handsworth_penman_monthly_sum["penman"] * MM_TO_METERS - precip_monthly["05NCM01_precip"] * MM_TO_METERS + RESERVOIR_SEEPAGE) * M_TO_DAM
        oxbow_loss = (handsworth_penman_monthly_sum["penman"] * MM_TO_METERS - precip_monthly["oxbow_precip"] * MM_TO_METERS + RESERVOIR_SEEPAGE) * M_TO_DAM

        # -----------------------------------------------------------------------------------------#
        #                              Assign reservoir Stage-Area-Capacities                     #
        # -----------------------------------------------------------------------------------------#
        reservoir_sacs_daily, reservoir_sacs_monthly = res.process_reservoir_sacs(
            reservoirs,
            wateryear=souris_dates.wateryear,
        )

        # -----------------------------------------------------------------------------------------#
        #                              Reservoir Loss                                             #
        # -----------------------------------------------------------------------------------------#
        reservoir_losses = {
            # Larsen
            "05NA006": reservoir_sacs_monthly["05NA006"]["area_dam2"].mul(roughbark_loss).round(0).astype(int),
            # Nickle
            "05NB020": reservoir_sacs_monthly["05NB020"]["area_dam2"].mul(roughbark_loss).round(0).astype(int),
            # Roughbark
            "05NB016": reservoir_sacs_monthly["05NB016"]["area_dam2"].mul(roughbark_loss).round(0).astype(int),
            # Moose
            "05NC002": reservoir_sacs_monthly["05NC002"]["area_dam2"].mul(handsworth_loss).round(0).astype(int),
            # Grant Devine
            "05ND012": reservoir_sacs_monthly["05ND012"]["area_dam2"].mul(oxbow_loss).round(0).astype(int),
        }

        # -----------------------------------------------------------------------------------------#
        #                                  Box Calculations                                        #
        # -----------------------------------------------------------------------------------------#
        logger.info("Begin box calculations...")
        boxes = bx.Boxes(
            box_5b=0 if model_inputs.pipeline is None else model_inputs.pipeline,
            box_11=0 if model_inputs.long_creek_minor_project_diversion is None else model_inputs.long_creek_minor_project_diversion,
            box_12=0 if model_inputs.us_diversion is None else model_inputs.us_diversion,
            box_16=0 if model_inputs.weyburn_pumpage is None else model_inputs.weyburn_pumpage,
            box_18=0 if model_inputs.weyburn_return_flow is None else model_inputs.weyburn_return_flow,
            box_25=0 if model_inputs.upper_souris_minor_diversion is None else model_inputs.upper_souris_minor_diversion,
            box_27=0 if model_inputs.estevan_net_pumpage is None else model_inputs.estevan_net_pumpage,
            box_28=0 if model_inputs.short_creek_diversions is None else model_inputs.short_creek_diversions,
            box_29=0 if model_inputs.lower_souris_minor_diversion is None else model_inputs.lower_souris_minor_diversion,
            box_37=0 if model_inputs.moose_mountain_minor_diversion is None else model_inputs.moose_mountain_minor_diversion,
        )
        # * 1.1.1 Larsen Reservoir Storage Change
        boxes.box_1 = reservoir_sacs_daily["05NA006"]["capacity_dam3"].iloc[-1] - reservoir_sacs_daily["05NA006"]["capacity_dam3"].iloc[0]
        # * 1.1.2 Larsen Reservoir Net Evaporation & Seepage
        boxes.box_2 = reservoir_losses["05NA006"].sum().sum()
        # * 1.1.3 Larsen Reservoir Diversion
        boxes.box_3 = boxes.box_1 + boxes.box_2
        # * 1.2 Town of Radville Pumpage
        # boxes["box4"] = 0  # box 4 is obsolete as of 2017
        boxes.box_5a = int(discharge["05113600"].sum().sum() * CMS_TO_DAM3days)
        # * 1.3.2 Long Creek near Estevan
        boxes.box_6 = discharge["05NB001"].sum().sum() * CMS_TO_DAM3days
        # * 1.3.3 Estevan Pipeline
        # boxes["box7"] = 0  # box 7 is obsolete as of 2021
        # * 1.3.4 Diversion Canal
        boxes.box_8 = discharge["05NB038"].sum().sum() * CMS_TO_DAM3days
        # * 1.3.5 Boundary Reservoir Total Outflow
        boxes.box_9 = boxes.box_6 + boxes.box_8
        # * 1.3.6	Boundary Reservoir Diversion
        boxes.box_10 = (boxes.box_5a + boxes.box_5b) - boxes.box_9
        # * 1.6 Total Diversion Long Creek
        boxes.box_13 = boxes.box_3 + boxes.box_10 + boxes.box_11 + boxes.box_12
        # * 2.1.1 Nickle Lake Reservoir Storage Change
        boxes.box_14 = reservoir_sacs_daily["05NB020"]["capacity_dam3"].iloc[-1] - reservoir_sacs_daily["05NB020"]["capacity_dam3"].iloc[0]
        # * 2.1.2 Nickle Lake Reservoir Net Evaporation & Seepage
        boxes.box_15 = reservoir_losses["05NB020"].sum()
        # * 2.1.4 Nickle Lake Reservoir Diversion
        boxes.box_17 = boxes.box_14 + boxes.box_15 + boxes.box_16
        # * 2.3.1 Roughbark Reservoir Storage Change
        boxes.box_19 = reservoir_sacs_daily["05NB016"]["capacity_dam3"].iloc[-1] - reservoir_sacs_daily["05NB016"]["capacity_dam3"].iloc[0]
        # * 2.3.2 Roughbark Reservoir Net Evaporation & Seepage
        boxes.box_20 = reservoir_losses["05NB016"].sum()
        # * 2.3 Roughbark Reservoir Depletion, box20_roughbark_netloss includes seepage calculation
        boxes.box_21 = boxes.box_19 + boxes.box_20
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
        boxes.box_22 = 0
        for station in normal_staids:
            boxes.box_22 += discharge[station].sum().sum()

        """Estimate the three ungaged tributaries with Mosley and Cook
        discharge data and convert all to dam3"""
        boxes.box_22 += discharge["05NB033"].sum().sum() * 2
        boxes.box_22 += discharge["05NB035"].sum().sum() * 3
        boxes.box_22 *= CMS_TO_DAM3days

        # * 2.4.2 Rafferty Reservoir Outflow
        if souris_dates.wateryear == 2023:
            # Special values for 2023 comuputation.  Flush line = 63 DAM3, Rafferty -> Estevan pipeline = 1468 DAM3
            boxes.box_23a = discharge["05NB036"].sum().sum() * CMS_TO_DAM3days + 63 + 1468
        else:
            boxes.box_23a = discharge["05NB036"].sum().sum() * CMS_TO_DAM3days

        # * 2.4.3 Rafferty Reservoir Diversion
        boxes.box_24 = boxes.box_22 - (boxes.box_23a + boxes.box_5b)
        # * 2.6 Total Diversion Upper Souris River
        boxes.box_26 = boxes.box_17 - boxes.box_18 + boxes.box_21 + boxes.box_24 + boxes.box_25

        # * 3.4 Total Diversion Lower Souris River
        if souris_dates.wateryear == 2023:
            # Special values for 2023 comuputation.  Duck pond release = 345 DAM3
            boxes.box_27 = boxes.box_27 - 345
        else:
            boxes.box_27 = boxes.box_27

        boxes.box_30 = boxes.box_27 + boxes.box_28 + boxes.box_29
        # * 4.1.1 Moose Mountain Lake Storage Change
        boxes.box_31 = reservoir_sacs_daily["05NC002"]["capacity_dam3"].iloc[-1] - reservoir_sacs_daily["05NC002"]["capacity_dam3"].iloc[0]
        # * 4.1.2 Moose Mountain Lake Net Evaporation & Seepage
        boxes.box_32 = reservoir_losses["05NC002"].sum()
        # * 4.1.3 Moose Mountain Lake Diversion
        boxes.box_33 = boxes.box_31 + boxes.box_32
        # * 4.2.1 Grant Devine Reservoir Storage Change
        boxes.box_34 = reservoir_sacs_daily["05ND012"]["capacity_dam3"].iloc[-1] - reservoir_sacs_daily["05ND012"]["capacity_dam3"].iloc[0]
        # * 4.2.2 Grant Devine Reservoir Net Evaporation & Seepage
        boxes.box_35 = reservoir_losses["05ND012"].sum()
        # * 4.2 Grant Devine Reservoir
        boxes.box_36 = boxes.box_34 + boxes.box_35
        # * 4.4 Total Diversions Moose Mountain Creek Basin
        boxes.box_38 = boxes.box_33 + boxes.box_36 + boxes.box_37
        # * 5.1 Yellow Grass Ditch
        boxes.box_39 = discharge["05NB011"].sum() * CMS_TO_DAM3days
        # * 5.2 Tatagwa Lake Drain
        boxes.box_40 = discharge["05NB018"].sum() * CMS_TO_DAM3days
        # * 5.3 Total Additions
        boxes.box_41 = boxes.box_39 + boxes.box_40
        # * 6.1 Total Diversion Souris River Basin
        boxes.box_42 = boxes.box_13 + boxes.box_26 + boxes.box_30 + boxes.box_38
        # * 6.2 Recorded Flow at Sherwood
        boxes.box_43 = discharge["05114000"].sum() * CMS_TO_DAM3days
        # * 6.3 Natural Flow at Sherwood
        boxes.box_44 = boxes.box_42 + boxes.box_43 - boxes.box_41
        darling_condition = rcap.lake_darling_condition(start_date=souris_dates.start_apportion, sherwood=boxes.box_44)
        # * 6.4 U.S. Share at Sherwood – 50% vs 40% Note: True=1, False=0
        boxes.box_45a = 0.4 * boxes.box_44 if darling_condition else None
        boxes.box_45b = 0 if darling_condition else 0.5 * boxes.box_44
        boxes.box_46 = boxes.box_12 + boxes.box_28 + boxes.box_43
        # * 6.6 Surplus or Deficit to U.S.
        boxes.box_47a = boxes.box_46 - boxes.box_45a if boxes.box_45a else None
        boxes.box_47b = boxes.box_46 - boxes.box_45b if boxes.box_45b else None
        # * 7.1 Recorded Flow at Western Crossing
        boxes.box_48 = discharge["05NA003"].sum() * CMS_TO_DAM3days
        # * 7.2 Recorded Flow at Eastern Crossing
        boxes.box_49 = discharge["05113600"].sum() * CMS_TO_DAM3days
        """If the box50 difference is positive,
        then more water was delivered annually from the U.S. than consumed and Recommendation 2 is met."""
        # * 7.3 Surplus or Deficit from U.S.
        boxes.box_50 = boxes.box_49 - boxes.box_48

        # Round all boxes to integers for report.
        boxes.round_boxes(0)

        ############################################################################################
        #                                  End Box Calculations                                    #
        ############################################################################################

        # -----------------------------------------------------------------------------------------#
        #                                  Process data for Report                                 #
        # -----------------------------------------------------------------------------------------#
        # Fastest way to reorg columns without writing it all out.
        discharge_daily_dict = {staid: discharge[[staid, f"{staid}_approval"]] for staid in discharge_stations}
        discharge_daily_df = pd.concat(list(discharge_daily_dict.values()), axis=1)

        # Combine evap and precip data to send to report.
        roughbark_evap_precip = pd.concat([roughbark_penman_monthly_sum["penman"], precip_monthly["05NB016_precip"]], axis=1)
        handsworth_evap_precip = pd.concat([handsworth_penman_monthly_sum["penman"], precip_monthly["05NCM01_precip"]], axis=1)

        raw_discharge = pd.DataFrame(model_inputs.raw_discharge)
        raw_discharge.set_index("date", drop=True, inplace=True)
        raw_reservoirs = pd.DataFrame(model_inputs.raw_reservoirs)
        raw_reservoirs.set_index("date", drop=True, inplace=True)
        raw_discharge_reservoirs = pd.concat([raw_discharge, raw_reservoirs], axis=1)

        # -----------------------------------------------------------------------------------------#
        #                                  Reporting                                               #
        # -----------------------------------------------------------------------------------------#
        logger.info("Writing Data to Excel Workbook...")
        excel.souris_excel_writer(
            dates=souris_dates,
            boxes=boxes,
            daily_discharge=discharge_daily_df,
            daily_reservoir=reservoir_sacs_daily,
            daily_roughbark=roughbark_meteo_daily,
            daily_handsworth=handsworth_meteo_daily,
            daily_oxbow=oxbow_precip_daily,
            monthly_reservoir_SAC=reservoir_sacs_monthly,
            monthly_roughbark_evap_precip=roughbark_evap_precip,
            monthly_handsworth_evap_precip=handsworth_evap_precip,
            monthly_oxbow_precip=precip_monthly[["oxbow_precip"]],
            reservoir_losses=reservoir_losses,
            raw_discharge_reservoirs=raw_discharge_reservoirs,
        )

        logger.info("Apportionment complete!")
        return boxes
        ############################################################################################
        #                                  End Reporting                                           #
        ############################################################################################


if __name__ == "__main__":
    exit(main())
