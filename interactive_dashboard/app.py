import pandas as pd
import streamlit as st # pip3 install streamlit
import plotly.express as px # pip3 install plotly-express

# Setting up Web Page on Streamlit
st.set_page_config(page_title="Sales Data",
                   page_icon=':watermelon:',
                   layout='wide',
                   )

# getting and setting up the excel file

df=pd.read_excel(io='files/supermarkt_sales.xlsx',
    engine='openpyxl',
    sheet_name='Sales',
    skiprows=3, # since the headers starts from 4th row, 1st 3 just for decoration 
    usecols='B:R', # which columns to use, in this case A col is empty 
    nrows=1000 # how many rows 
    )
# pass that data
# st.dataframe(df)

# ---- SIDEBAR ----
st.sidebar.header('Filters:')

# --- Just displaying info BEGIN ---
# city col
city=st.sidebar.multiselect(
    "Select City:",
    options=df['City'].unique(),
    # One default city -> default='Mandalay'
    default=df['City'].unique()
)
#  customer_type col
customer_type=st.sidebar.multiselect(
    "Select client type:",
    options=df['Customer_type'].unique(),
    # Setting Member as default option for customer_type
    default='Member'
)
#  Gender col
gender=st.sidebar.multiselect(
    "Select gender:",
    options=df['Gender'].unique(),
    # Setting Member as default option for customer_type
    default='Male'
)
# --- Just displaying info END---

# Adding querry where the actual view changes based on the selection from Filter:
df_selection=df.query(
    "City==@city & Customer_type==@customer_type & Gender==@gender"
)
# we dataframe param from "dt", original info to "df_selection" what an user selected
st.dataframe(df_selection)


# ---- MAIN PAGE ----
