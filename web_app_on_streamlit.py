import streamlit as st 
import pandas

track_of_study={
    "week_1":3*4+3,
    "week_2":12,
    "week_3":4*8+3,
    "week_4":5*4+1+(2*9),
    "week_5":4*4+12
}

dataframe=pandas.DataFrame(track_of_study)

st.title("1st StreaLit app")
st.subheader("A lot of stuff to learn")
st.write("""No worries!
We'll get there sooner or later!
""")
st.write("""P.S.Enjoy!
""")
st.write(dataframe)

# to run this app add in terminal this command - streamlit run web_app_on_streamlit.py
# https://share.streamlit.io/ hoste this app on streamlit 

