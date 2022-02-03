# streamlit_app.py

import streamlit as st
import pandas as pd
import gspread

from googleapiclient.discovery import build


from google.oauth2 import service_account

# Create a connection object.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

credentials = service_account.Credentials.from_service_account_info(
    st.secrets["gcp_service_account"],
    scopes=SCOPES,
)


# The ID spreadsheet.
SAMPLE_SPREADSHEET_ID = '11bjSwciaPNMnDUKg68cuOkQ1qBGjcePBQRzlgjpiyaE'


service = build('sheets', 'v4', credentials=credentials)

# Call the Sheets API and creating dataset
sheet = service.spreadsheets()
result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                            range="Sheet1!A1:DB544").execute()
values = result.get('values', [])
df = pd.DataFrame(values[2:], columns=values[0])

# For map
# map_df = df.copy()
# map_df = map_df[['Name', 'latitude', 'longitude']]
# map_df.dropna(inplace=True)
# map_df['latitude'] = pd.to_numeric(map_df['latitude'], errors="ignore")
# map_df['longitude'] = pd.to_numeric(map_df['longitude'], errors="ignore")
# map_df.dropna(inplace=True)

# print(df.head())

# Using gspread

client = gspread.authorize(credentials)
sheet = client.open_by_key(SAMPLE_SPREADSHEET_ID).sheet1


# Creating UI
st.header("TSIIC Data Source")
# st.map(map_df)
#st.write(df)


# Sidebar
st.sidebar.header("Industry ID")
user_id = st.sidebar.number_input("Enter Industry ID", 0, 542)

if user_id != 0:
    st.write(df.loc[df['Industry ID'] == str(user_id)])
else:
    st.write(df)



# Filter according to sidebar
if user_id != 0:
    groups = ['select group', 'Unit Details', 'Emissions', 'Inputs', 'Waste', 'Waste Water']
    group = st.selectbox("Select a group", groups)

    if group == 'select group':
        pass


    elif group == 'Unit Details':

        name = st.text_input("Industry Name", sheet.cell(user_id + 2, 2).value)
        sheet.update_cell(user_id + 2, 2, str(name))

        address = st.text_input("Address", sheet.cell(user_id + 2, 3).value)
        sheet.update_cell(user_id + 2, 3, str(address))

        loa = st.text_input("Line of Activity", sheet.cell(user_id + 2, 4).value)
        sheet.update_cell(user_id + 2, 4, str(loa))

        Area = st.text_input("Area", sheet.cell(user_id + 2, 6).value)
        sheet.update_cell(user_id + 2, 6, str(Area))

        District = st.text_input("District", sheet.cell(user_id + 2, 7).value)
        sheet.update_cell(user_id + 2, 7, str(District))

        Latitude = st.text_input("Latitude", sheet.cell(user_id + 2, 8).value)
        sheet.update_cell(user_id + 2, 8, str(Latitude))

        Longitude = st.text_input("Longitude", sheet.cell(user_id + 2, 9).value)
        sheet.update_cell(user_id + 2, 9, str(Longitude))

        E_mail = st.text_input("E- mail", sheet.cell(user_id + 2, 10).value)
        sheet.update_cell(user_id + 2, 10, str(E_mail))

        Nature_of_product = st.text_input("Nature of product", sheet.cell(user_id + 2, 11).value)
        sheet.update_cell(user_id + 2, 11, str(Nature_of_product))

        Park_proposed = st.text_input("Park proposed", sheet.cell(user_id + 2, 12).value)
        sheet.update_cell(user_id + 2, 12, str(Park_proposed))

        Operational_Status = st.text_input("Operational Status", sheet.cell(user_id + 2, 13).value)
        sheet.update_cell(user_id + 2, 13, str(Operational_Status))

        Category_of_Industries = st.text_input("Category of Industries", sheet.cell(user_id + 2, 14).value)
        sheet.update_cell(user_id + 2, 14, str(Category_of_Industries))

        APCE = st.text_input("APCE", sheet.cell(user_id + 2, 15).value)
        sheet.update_cell(user_id + 2, 15, str(APCE))

        Water_Treatment = st.text_input("Water Treatment", sheet.cell(user_id + 2, 16).value)
        sheet.update_cell(user_id + 2, 16, str(Water_Treatment))

        Current_Foot_Print = st.text_input("Current Foot Print (Total area of the unit in Acres)",
                                           sheet.cell(user_id + 2, 17).value)
        sheet.update_cell(user_id + 2, 17, str(Current_Foot_Print))

        Area_for_Utilities = st.text_input("Area for Utilities", sheet.cell(user_id + 2, 18).value)
        sheet.update_cell(user_id + 2, 18, str(Area_for_Utilities))

        Area_required_in_HPC = st.text_input("Area that will be required in HPC for housing these companies",
                                             sheet.cell(user_id + 2, 19).value)
        sheet.update_cell(user_id + 2, 19, str(Area_required_in_HPC))

        Large_MSME = st.text_input("Large / MSME", sheet.cell(user_id + 2, 39).value)
        sheet.update_cell(user_id + 2, 39, str(Large_MSME))

        Boiler_TPH_1 = st.text_input("Boiler (TPH).1", sheet.cell(user_id + 2, 85).value)
        sheet.update_cell(user_id + 2, 85, str(Boiler_TPH_1))

        Height_of_Stack_in_m = st.text_input("Height of Stack in m", sheet.cell(user_id + 2, 86).value)
        sheet.update_cell(user_id + 2, 86, str(Height_of_Stack_in_m))

        Flow_Rate_in_m3_hr = st.text_input("Flow Rate in m3/hr", sheet.cell(user_id + 2, 87).value)
        sheet.update_cell(user_id + 2, 87, str(Flow_Rate_in_m3_hr))



    elif group == 'Emissions':

        Total_Air_Emission = st.text_input(
            "Total Air Emission - Fugitive (For loading and unloading Chemical Solvent) [Kg/day]",
            sheet.cell(user_id + 2, 20).value)
        sheet.update_cell(user_id + 2, 20, str(Total_Air_Emission))

        Type_of_Monitoring = st.text_input("Type of Monitoring Equipment for Air Emission",
                                           sheet.cell(user_id + 2, 21).value)
        sheet.update_cell(user_id + 2, 21, str(Type_of_Monitoring))

        Fuel_Emission = st.text_input("Fuel Emission in Ton/day", sheet.cell(user_id + 2, 22).value)
        sheet.update_cell(user_id + 2, 22, str(Fuel_Emission))

        Process_Emission = st.text_input("Process Emission of VOC (kg/day) (VOC)", sheet.cell(user_id + 2, 23).value)
        sheet.update_cell(user_id + 2, 23, str(Process_Emission))

        Fugitive_Emission_For_Loading_and_unloading_chemical_sovent_kg_day = st.text_input(
            "Fugitive Emission (For Loading and unloading chemical sovent) (kg/day)", sheet.cell(user_id + 2, 82).value)
        sheet.update_cell(user_id + 2, 82, str(Fugitive_Emission_For_Loading_and_unloading_chemical_sovent_kg_day))

        Air_emission_Type_of_monitoring_equipment = st.text_input("Air emission (Type of monitoring equipment)",
                                                                  sheet.cell(user_id + 2, 83).value)
        sheet.update_cell(user_id + 2, 83, str(Air_emission_Type_of_monitoring_equipment))

        SPM_Ton_Day = st.text_input("SPM (Ton/Day)", sheet.cell(user_id + 2, 88).value)
        sheet.update_cell(user_id + 2, 88, str(SPM_Ton_Day))

        Fuel_Emission_in_Ton_Day_NO2 = st.text_input("Fuel Emission in Ton/Day NO2", sheet.cell(user_id + 2, 89).value)
        sheet.update_cell(user_id + 2, 89, str(Fuel_Emission_in_Ton_Day_NO2))

        Fuel_Emission_in_Ton_Day_NO2_2 = st.text_input("Fuel Emission in Ton/Day (NO2)",
                                                       sheet.cell(user_id + 2, 90).value)
        sheet.update_cell(user_id + 2, 90, str(Fuel_Emission_in_Ton_Day_NO2_2))

        Fuel_Emission_in_Ton_Day_SO2 = st.text_input("Fuel Emission in Ton/Day (SO2)",
                                                     sheet.cell(user_id + 2, 91).value)
        sheet.update_cell(user_id + 2, 91, str(Fuel_Emission_in_Ton_Day_SO2))

        Fuel_Emission_in_Ton_Day_SO2_emission_per_Boiler_emission_kg_hr = st.text_input(
            "Fuel Emission in Ton/Day (SO2 emission per Boiler emission kg/hr)", sheet.cell(user_id + 2, 92).value)
        sheet.update_cell(user_id + 2, 92, str(Fuel_Emission_in_Ton_Day_SO2_emission_per_Boiler_emission_kg_hr))

        Fuel_Emission_in_Ton_Day_HC = st.text_input("Fuel Emission in Ton/Day (HC)", sheet.cell(user_id + 2, 93).value)
        sheet.update_cell(user_id + 2, 93, str(Fuel_Emission_in_Ton_Day_HC))

        Fuel_Emission_in_Ton_Day_HC_emissionper_Boiler_emission_kg_hr = st.text_input(
            "Fuel Emission in Ton/Day ( HC emissionper Boiler emission (kg/hr)", sheet.cell(user_id + 2, 94).value)
        sheet.update_cell(user_id + 2, 94, str(Fuel_Emission_in_Ton_Day_HC_emissionper_Boiler_emission_kg_hr))

        Fuel_Emission_in_Ton_Day_CO = st.text_input("Fuel Emission in Ton/Day ( CO)", sheet.cell(user_id + 2, 95).value)
        sheet.update_cell(user_id + 2, 95, str(Fuel_Emission_in_Ton_Day_CO))

        Fuel_Emission_in_Ton_Day_CO_emissionper_Boiler_emission_kg_hr = st.text_input(
            "Fuel Emission in Ton/Day ( CO emissionper Boiler emission (kg/hr))", sheet.cell(user_id + 2, 96).value)
        sheet.update_cell(user_id + 2, 96, str(Fuel_Emission_in_Ton_Day_CO_emissionper_Boiler_emission_kg_hr))

        Fuel_Emission_in_Ton_Day_CO2 = st.text_input("Fuel Emission in Ton/Day ( CO2 )",
                                                     sheet.cell(user_id + 2, 97).value)
        sheet.update_cell(user_id + 2, 97, str(Fuel_Emission_in_Ton_Day_CO2))

        Fuel_Emission_in_Ton_Day_cCO2_emissionper_Boiler_emission_kg_hr = st.text_input(
            "Fuel Emission in Ton/Day (cCO2 emissionper Boiler emission (kg/hr)", sheet.cell(user_id + 2, 98).value)
        sheet.update_cell(user_id + 2, 98, str(Fuel_Emission_in_Ton_Day_cCO2_emissionper_Boiler_emission_kg_hr))

        Process_Emission_of_VOC_kg_day_VOC_1 = st.text_input("Process Emission of VOC (kg/day) (VOC) .1",
                                                             sheet.cell(user_id + 2, 99).value)
        sheet.update_cell(user_id + 2, 99, str(Process_Emission_of_VOC_kg_day_VOC_1))

        Process_Emission_of_VOC_kg_day_VOC_per_Boiler_emission_kg_hr = st.text_input(
            "Process Emission of VOC (kg/day) ( VOC per Boiler emission (g/hr)", sheet.cell(user_id + 2, 100).value)
        sheet.update_cell(user_id + 2, 100, str(Process_Emission_of_VOC_kg_day_VOC_per_Boiler_emission_kg_hr))

        Process_Emission_of_VOC_kg_day_SOX = st.text_input("Process Emission of VOC (kg/day) (SOX)",
                                                           sheet.cell(user_id + 2, 101).value)
        sheet.update_cell(user_id + 2, 101, str(Process_Emission_of_VOC_kg_day_SOX))

        Process_Emission_of_VOC_kg_day_NOX = st.text_input("Process Emission of VOC (kg/day) (NOX)",
                                                           sheet.cell(user_id + 2, 102).value)
        sheet.update_cell(user_id + 2, 102, str(Process_Emission_of_VOC_kg_day_NOX))

        Process_Emission_of_VOC_kg_day_CO = st.text_input("Process Emission of VOC (kg/day) (CO)",
                                                          sheet.cell(user_id + 2, 103).value)
        sheet.update_cell(user_id + 2, 103, str(Process_Emission_of_VOC_kg_day_CO))


    elif group == "Inputs":
        Product_in_kg_day = st.text_input("Product in kg/day", sheet.cell(user_id + 2, 24).value)
        sheet.update_cell(user_id + 2, 24, str(Product_in_kg_day))

        Raw_Materials_Kg_day = st.text_input("Raw Materials Kg/day", sheet.cell(user_id + 2, 25).value)
        sheet.update_cell(user_id + 2, 25, str(Raw_Materials_Kg_day))

        Total_quantity_of_solvents_Kg_day = st.text_input(
            "Total quantity of solvents Kg/day (Captive solvents, Recovery solvents, and            contaminated)",
            sheet.cell(user_id + 2, 26).value)
        sheet.update_cell(user_id + 2, 26, str(Total_quantity_of_solvents_Kg_day))

        Water_Consumption_in_KLD = st.text_input("Water Consumption in KLD", sheet.cell(user_id + 2, 27).value)
        sheet.update_cell(user_id + 2, 27, str(Water_Consumption_in_KLD))

        Boiler_TPH = st.text_input("Boiler (TPH)", sheet.cell(user_id + 2, 36).value)
        sheet.update_cell(user_id + 2, 36, str(Boiler_TPH))

        Fuel_Quantity_Ton_Day_Coal = st.text_input("Fuel Quantity (Ton/Day) [Coal]", sheet.cell(user_id + 2, 37).value)
        sheet.update_cell(user_id + 2, 37, str(Fuel_Quantity_Ton_Day_Coal))

        Fuel_quantiy_Ton_day_others = st.text_input("Fuel quantiy Ton/day (others)", sheet.cell(user_id + 2, 38).value)
        sheet.update_cell(user_id + 2, 38, str(Fuel_quantiy_Ton_day_others))

        Raw_Materials_Kg_day_1 = st.text_input("Raw Materials Kg/day.1", sheet.cell(user_id + 2, 49).value)
        sheet.update_cell(user_id + 2, 49, str(Raw_Materials_Kg_day_1))

        Raw_Materials_Kg_day_Acre = st.text_input("Raw Materials Kg/day/Acre ", sheet.cell(user_id + 2, 50).value)
        sheet.update_cell(user_id + 2, 50, str(Raw_Materials_Kg_day_Acre))

        Captive_Solvent_Capacity_kg_Day = st.text_input("Captive Solvent Capacity  (kg/Day)",
                                                        sheet.cell(user_id + 2, 51).value)
        sheet.update_cell(user_id + 2, 51, str(Captive_Solvent_Capacity_kg_Day))

        Captive_Solvent_Capacity_kg_Day__Raw_Materials_Kg_day = st.text_input(
            "Captive Solvent Capacity (kg/Day)/Raw Materials Kg/day", sheet.cell(user_id + 2, 52).value)
        sheet.update_cell(user_id + 2, 52, str(Captive_Solvent_Capacity_kg_Day__Raw_Materials_Kg_day))

        Recovery_Spent_Solvent_kg_Day_Raw_Materials_Kg_day = st.text_input(
            "Recovery Spent Solvent (kg/Day)/Raw Materials Kg/day", sheet.cell(user_id + 2, 53).value)
        sheet.update_cell(user_id + 2, 53, str(Recovery_Spent_Solvent_kg_Day_Raw_Materials_Kg_day))

        Recovery_Spent_Solvent_kg_Day = st.text_input("Recovery Spent Solvent (kg/Day)",
                                                      sheet.cell(user_id + 2, 54).value)
        sheet.update_cell(user_id + 2, 54, str(Recovery_Spent_Solvent_kg_Day))

        Contammited_sovent_sent_for_inceneration_Treatment_kg_Day = st.text_input(
            "Contammited solvent sent for inceneration/ Treatment (kg/Day)", sheet.cell(user_id + 2, 55).value)
        sheet.update_cell(user_id + 2, 55, str(Contammited_sovent_sent_for_inceneration_Treatment_kg_Day))

        Contammited_sovent_sent_for_inceneration_Treatment_kg_Day_Raw_Materials_Kg_day = st.text_input(
            "Contammited solvent sent for inceneration/ Treatment (kg/Day)/Raw Materials Kg/day",
            sheet.cell(user_id + 2, 56).value)
        sheet.update_cell(user_id + 2, 56,
                          str(Contammited_sovent_sent_for_inceneration_Treatment_kg_Day_Raw_Materials_Kg_day))

        Product_in_kg_day_1 = st.text_input("Product in kg/day.1", sheet.cell(user_id + 2, 57).value)
        sheet.update_cell(user_id + 2, 57, str(Product_in_kg_day_1))

        Product_in_kg_day_acre = st.text_input("Product in kg/day/acre", sheet.cell(user_id + 2, 58).value)
        sheet.update_cell(user_id + 2, 58, str(Product_in_kg_day_acre))

        Water_Consumption_in_KLD_1 = st.text_input("Water Consumption in KLD.1", sheet.cell(user_id + 2, 59).value)
        sheet.update_cell(user_id + 2, 59, str(Water_Consumption_in_KLD_1))

        Water_Consumption_in_KLD_kg_day_of_product = st.text_input("Water Consumption in KLD/kg/day of product",
                                                                   sheet.cell(user_id + 2, 60).value)
        sheet.update_cell(user_id + 2, 60, str(Water_Consumption_in_KLD_kg_day_of_product))

        Fuel_Quantity_Ton_Day_Coal_1 = st.text_input("Fuel Quantity (Ton/Day) [Coal].1",
                                                     sheet.cell(user_id + 2, 84).value)
        sheet.update_cell(user_id + 2, 84, str(Fuel_Quantity_Ton_Day_Coal_1))

        # AJ - 36
    elif group == "Waste":
        LTDS_facility = st.text_input("LTDS Facility", sheet.cell(user_id + 2, 40).value)
        sheet.update_cell(user_id + 2, 40, str(LTDS_facility))

        HTDS_facility = st.text_input("HTDS Facility", sheet.cell(user_id + 2, 41).value)
        sheet.update_cell(user_id + 2, 41, str(HTDS_facility))

        MONTHLY_PERMITTED_HTDS_QUANTITY = st.text_input("MONTHLY PERMITTED HTDS QUANTITY ",
                                                        sheet.cell(user_id + 2, 42).value)
        sheet.update_cell(user_id + 2, 42, str(MONTHLY_PERMITTED_HTDS_QUANTITY))

        MONTHLY_PERMITTED_LTDS_QUANTITY = st.text_input("MONTHLY PERMITTED LTDS QUANTITY ",
                                                        sheet.cell(user_id + 2, 43).value)
        sheet.update_cell(user_id + 2, 43, str(MONTHLY_PERMITTED_LTDS_QUANTITY))

        MONTHLY_PERMITTED_INORGANIC_HW_QUANTITY = st.text_input("MONTHLY PERMITTED INORGANIC HW QUANTITY",
                                                                sheet.cell(user_id + 2, 44).value)
        sheet.update_cell(user_id + 2, 44, str(MONTHLY_PERMITTED_INORGANIC_HW_QUANTITY))

        MONTHLY_PERMITTED_ORGANIC_HW_QUANTITY = st.text_input("MONTHLY PERMITTED ORGANIC HW QUANTITY",
                                                              sheet.cell(user_id + 2, 45).value)
        sheet.update_cell(user_id + 2, 45, str(MONTHLY_PERMITTED_ORGANIC_HW_QUANTITY))

        MONTHLY_PERMITTED_RECYCLABLE_HW_QUANTITY = st.text_input("MONTHLY PERMITTED RECYCLABLE HW QUANTITY",
                                                                 sheet.cell(user_id + 2, 46).value)
        sheet.update_cell(user_id + 2, 46, str(MONTHLY_PERMITTED_RECYCLABLE_HW_QUANTITY))

        HTDS_KL_MONTH = st.text_input("HTDS (KL/MONTH)", sheet.cell(user_id + 2, 47).value)
        sheet.update_cell(user_id + 2, 47, str(HTDS_KL_MONTH))

        LTDS_KL_MONTH = st.text_input("LTDS (KL/MONTH)", sheet.cell(user_id + 2, 48).value)
        sheet.update_cell(user_id + 2, 48, str(LTDS_KL_MONTH))

        Organic_Process_Residue_Waste = st.text_input("Organic (Process Residue/ Waste)",
                                                      sheet.cell(user_id + 2, 69).value)
        sheet.update_cell(user_id + 2, 69, str(Organic_Process_Residue_Waste))

        Organic_Spent_mixed_solvents = st.text_input("Organic (Spent mixed solvents)",
                                                     sheet.cell(user_id + 2, 70).value)
        sheet.update_cell(user_id + 2, 70, str(Organic_Spent_mixed_solvents))

        Organic_Spent_Carbon = st.text_input("Organic (Spent Carbon)", sheet.cell(user_id + 2, 71).value)
        sheet.update_cell(user_id + 2, 71, str(Organic_Spent_Carbon))

        Organic_Distillation_Bottom_Residue = st.text_input("Organic ( Distillation Bottom Residue)",
                                                            sheet.cell(user_id + 2, 72).value)
        sheet.update_cell(user_id + 2, 72, str(Organic_Distillation_Bottom_Residue))

        Inorganic_Residual_from_Evaporation_System = st.text_input("Inorganic (Residual from Evaporation System)",
                                                                   sheet.cell(user_id + 2, 73).value)
        sheet.update_cell(user_id + 2, 73, str(Inorganic_Residual_from_Evaporation_System))

        Inorganic_residue = st.text_input("Inorganic residue", sheet.cell(user_id + 2, 74).value)
        sheet.update_cell(user_id + 2, 74, str(Inorganic_residue))

        Inorganic_Mixed_salts_from_dryer_ATFD = st.text_input("Inorganic (Mixed salts from dryer/ ATFD)",
                                                              sheet.cell(user_id + 2, 75).value)
        sheet.update_cell(user_id + 2, 75, str(Inorganic_Mixed_salts_from_dryer_ATFD))

        Inorganic_Solid_liquid_waste_generated_form_APC_equipments_liquid_form_incinerator_scrubber = st.text_input(
            "Inorganic (Solid & liquid waste generated form APC equipments, liquid form incinerator/ scrubber)",
            sheet.cell(user_id + 2, 76).value)
        sheet.update_cell(user_id + 2, 76, str(
            Inorganic_Solid_liquid_waste_generated_form_APC_equipments_liquid_form_incinerator_scrubber))

        Inorganic_Biological_sludge = st.text_input("Inorganic (Biological sludge)", sheet.cell(user_id + 2, 77).value)
        sheet.update_cell(user_id + 2, 77, str(Inorganic_Biological_sludge))

        Inorganic_Incineration_Ash = st.text_input("Inorganic (Incineration Ash)", sheet.cell(user_id + 2, 78).value)
        sheet.update_cell(user_id + 2, 78, str(Inorganic_Incineration_Ash))

        Inorganic_ETP_Sludge = st.text_input("Inorganic (ETP Sludge)", sheet.cell(user_id + 2, 79).value)
        sheet.update_cell(user_id + 2, 79, str(Inorganic_ETP_Sludge))

        Hazardous_Waste_Disposal_Point_Organic = st.text_input("Hazardous Waste Disposal Point ( Organic )",
                                                               sheet.cell(user_id + 2, 80).value)
        sheet.update_cell(user_id + 2, 80, str(Hazardous_Waste_Disposal_Point_Organic))

        Hazardous_Waste_Disposal_Point_Inorganic = st.text_input("Hazardous Waste Disposal Point ( Inorganic )",
                                                                 sheet.cell(user_id + 2, 81).value)
        sheet.update_cell(user_id + 2, 81, str(Hazardous_Waste_Disposal_Point_Inorganic))


    elif group == "Waste Water":
        Total_Wastewater_Generation_in_KLD = st.text_input("Total Wastewater Generation in KLD",
                                                           sheet.cell(user_id + 2, 28).value)
        sheet.update_cell(user_id + 2, 28, str(Total_Wastewater_Generation_in_KLD))

        Wastewater_HTDS_Generation_in_KLD = st.text_input("Wastewater (HTDS) Generation in KLD",
                                                          sheet.cell(user_id + 2, 29).value)
        sheet.update_cell(user_id + 2, 29, str(Wastewater_HTDS_Generation_in_KLD))

        Waste_water_LTDS_Generation_in_KLD = st.text_input("Wastewater (LTDS) Generation in KLD",
                                                           sheet.cell(user_id + 2, 30).value)
        sheet.update_cell(user_id + 2, 30, str(Waste_water_LTDS_Generation_in_KLD))

        Wastewater_Toxic_Generation_in_KLD = st.text_input("Wastewater (Toxic) Generation in KLD",
                                                           sheet.cell(user_id + 2, 31).value)
        sheet.update_cell(user_id + 2, 31, str(Wastewater_Toxic_Generation_in_KLD))

        Waste_Water_Pre_Treatment_Generation_in_KLD = st.text_input("Waste Water Pre Treatment/ Generation in KLD",
                                                                    sheet.cell(user_id + 2, 32).value)
        sheet.update_cell(user_id + 2, 32, str(Waste_Water_Pre_Treatment_Generation_in_KLD))

        Hazardous_Waste_Generation_Kg_day_Organic_Inorganic = st.text_input(
            "Hazardous Waste Generation (Kg/day) (Organic & Inorganic)", sheet.cell(user_id + 2, 33).value)
        sheet.update_cell(user_id + 2, 33, str(Hazardous_Waste_Generation_Kg_day_Organic_Inorganic))

        Hazardous_Waste_Generation_Kg_day_Organic = st.text_input("Hazardous Waste Generation (Kg/day) - Organic",
                                                                  sheet.cell(user_id + 2, 34).value)
        sheet.update_cell(user_id + 2, 34, str(Hazardous_Waste_Generation_Kg_day_Organic))

        Hazardous_Waste_Generation_Kg_day_Inorganic = st.text_input("Hazardous Waste Generation (Kg/day) - Inorganic",
                                                                    sheet.cell(user_id + 2, 35).value)
        sheet.update_cell(user_id + 2, 35, str(Hazardous_Waste_Generation_Kg_day_Inorganic))

        Wastewater_Generation_in_KLD_HTDS = st.text_input("Wastewater Generation in KLD (HTDS)",
                                                          sheet.cell(user_id + 2, 61).value)
        sheet.update_cell(user_id + 2, 61, str(Wastewater_Generation_in_KLD_HTDS))

        Wastewater_Generation_in_KLD_HTDS_product_day = st.text_input(
            "Wastewater Generation in KLD (HTDS /product /day)",
            sheet.cell(user_id + 2, 62).value)
        sheet.update_cell(user_id + 2, 62, str(Wastewater_Generation_in_KLD_HTDS_product_day))

        Wastewater_Generation_in_KLD_LTDS = st.text_input("Wastewater Generation in KLD (LTDS)",
                                                          sheet.cell(user_id + 2, 63).value)
        sheet.update_cell(user_id + 2, 63, str(Wastewater_Generation_in_KLD_LTDS))

        Wastewater_Generation_in_KLD_LTDS_product_day = st.text_input("Wastewater Generation in KLD (LTDS/product/day)",
                                                                      sheet.cell(user_id + 2, 64).value)
        sheet.update_cell(user_id + 2, 64, str(Wastewater_Generation_in_KLD_LTDS_product_day))

        Wastewater_Generation_in_KLD_Toxic = st.text_input("Wastewater Generation in KLD (Toxic)",
                                                           sheet.cell(user_id + 2, 65).value)
        sheet.update_cell(user_id + 2, 65, str(Wastewater_Generation_in_KLD_Toxic))

        Toxic_product_day = st.text_input("Toxic/product/day", sheet.cell(user_id + 2, 66).value)
        sheet.update_cell(user_id + 2, 66, str(Toxic_product_day))

        Waste_Water_Pre_Treatment_Treatment_Facilities = st.text_input(
            "Waste Water Pre Treatment / Treatment Facilities", sheet.cell(user_id + 2, 67).value)
        sheet.update_cell(user_id + 2, 67, str(Waste_Water_Pre_Treatment_Treatment_Facilities))

        Pre_Treated_Treated_Waste_Water_Disposal_Point = st.text_input(
            "Pre Treated / Treated Waste Water Disposal Point", sheet.cell(user_id + 2, 68).value)
        sheet.update_cell(user_id + 2, 68, str(Pre_Treated_Treated_Waste_Water_Disposal_Point))


