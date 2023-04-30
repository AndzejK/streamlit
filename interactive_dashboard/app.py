import pandas as pd
import streamlit as st # pip3 install streamlit
import plotly.express as px # pip3 install plotly-express

# Setting up Web Page on Streamlit
st.set_page_config(page_title="Sales Data",
                   page_icon=':watermelon:',
                   layout='wide',
                   )

# getting and setting up the excel file
@st.cache_resource #st.cache is deprecated. Please use one of Streamlit's new caching commands, st.cache_data or st.cache_resource
def get_data_from_excel():
    df=pd.read_excel(io='files/supermarkt_sales.xlsx',
        engine='openpyxl',
        sheet_name='Sales',
        skiprows=3, # since the headers starts from 4th row, 1st 3 just for decoration 
        usecols='B:R', # which columns to use, in this case A col is empty 
        nrows=1000 # how many rows 
        )
    return df
df=get_data_from_excel()

# Add "hour" column to dataframe 
df["hour"]=pd.to_datetime(df["Time"], format="%H:%M:%S").dt.hour

# passing the data
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
st.title(":eyes: Sales Dashboard")
st.markdown("##")

# TOP KPI
total_sales=int(df_selection["Total"].sum())
avg_rating=round(df_selection["Rating"].mean(),2)
star_rating=":star:"*int(round(avg_rating,0)/2)
avg_sale_by_trans=round(df_selection['Total'].mean(),2)

left_column,middle_column,right_column=st.columns(3)

with left_column:
    st.subheader("Total Sales:")
    st.subheader(f"${total_sales:,}") # instead 76076 is 76,076
with middle_column:
    st.subheader("Average Raiting:")
    st.subheader(f"{avg_rating} {star_rating}")
with right_column:
    st.subheader("Average Sales Per Transaction:")
    st.subheader(f'${avg_sale_by_trans}')

st.markdown("---")

# ------- Not working getting TypeError: datetime64 type does not support sum operations ------- 

#  SALES BY Product Line [BAR CHAR]
sales_by_product_line=df_selection.groupby(["Product line"])["Total"].sum()

fig_product_sales=px.bar(
    sales_by_product_line,
    x="Total",
    y=sales_by_product_line.index,
    orientation="h",
    title="<b>Sales by Product Lines</b>",
    color_discrete_sequence=["#0083B8"],
    template="plotly_white"
)
fig_product_sales.update_layout(
    plot_bgcolor="rgba(0,0,0,0)",
    xaxis=dict(showgrid=False)
)

# Display the SALES BY Product Line on the WEB
# st.plotly_chart(fig_product_sales)

# sales_by_product_line=df_selection.groupby(by=["Product line"]).sum()[["Total"]].sort_values(by="Total")

# test=df_selection.groupby(["Product line"])["Total"].sum()
# print(test)

# ------- Not working getting TypeError: datetime64 type does not support sum operations ------- 

# SALES BY HOUR [BAR CHAR] groupby(["Product line"])["Total"].sum()
sales_by_hour=df_selection.groupby("hour")["Total"].sum()
fig_hourly_sales = px.bar(
    sales_by_hour,
    x=sales_by_hour.index,
    y="Total",
    title="Sales by Hour",
    color_discrete_sequence=["#0083B8"],
    template="plotly_white"
)
fig_hourly_sales.update_layout(
    plot_bgcolor="rgba(0,0,0,0)",
    xaxis=dict(tickmode="linear"),
    yaxis=dict(showgrid=False)
)
# Display/plot the chat by hour sales
# st.plotly_chart(fig_hourly_sales)

# reorganising BAR CHARs, displaying in one row as two columns 
left_column_2,right_column_2=st.columns(2)
left_column_2.plotly_chart(fig_hourly_sales,use_container_width=True)
right_column_2.plotly_chart(fig_product_sales,use_container_width=True)

# ---- HIDE STREAMLIT STYLE ----
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

# The Link to Internet :)
# https://andzejk-streamlit-interactive-dashboardapp-z3y2nv.streamlit.app/