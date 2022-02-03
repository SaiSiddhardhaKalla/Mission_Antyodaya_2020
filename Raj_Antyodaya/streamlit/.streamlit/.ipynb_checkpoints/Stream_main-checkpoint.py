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
# print(df.head())

# Using gspread

client = gspread.authorize(credentials)
sheet = client.open_by_key(SAMPLE_SPREADSHEET_ID).sheet1


# Creating UI
st.header("TSIIC Data Source")
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
    name = st.text_input("Industry Name", sheet.cell(user_id+2, 2).value)
    sheet.update_cell(user_id+2, 2, str(name))

    address = st.text_input("Address", sheet.cell(user_id+2, 3).value)
    sheet.update_cell(user_id+2, 3, str(address))

    loa = st.text_input("Line of Activity", sheet.cell(user_id+2, 4).value)
    sheet.update_cell(user_id+2, 4, str(loa))


