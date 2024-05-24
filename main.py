import streamlit as st
import plotly.express as px
from weather import get_weather_data

st.title("Weather Forecast for Next Days")
place = st.text_input("Place: ")
days = st.slider("Forecast Days", min_value=1, max_value=5, help="Select the number of forecasted days.")
option = st.selectbox("Select data to view", ("Temperature", "Sky"))

st.subheader(f"{option} for the next {days} {'day' if days == 1 else 'days'} in {place}")

day,temp = get_weather_data(place,days,option)

figure = px.line(x=day, y=temp, labels={"x": "Dates", "y": "Temperature(C)"})
st.plotly_chart(figure)
