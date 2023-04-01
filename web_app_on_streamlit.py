import streamlit as st 
import pandas

#https://share.streamlit.io/

track_of_study={
    "week_1":[(3*4+3)*25],
    "week_2":[12*25],
    "week_3":[(4*8+3)*25],
    "week_4":[25*(5*4+1+(2*9))],
    "week_5":[(4*4+12)*25]
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
st.line_chart(dataframe) # adding the graph
st.area_chart(dataframe) # diff type of graph

# Simple coverter from C to F but in intaractive way
my_slider=st.slider("Celsius")
st.write(my_slider, "In Fahrenheit is:",my_slider*9/5+2)


