import streamlit as st
import plotly.express as px

st.title("Weather Forecast for Next Days")
place = st.text_input("Place: ")
days = st.slider("Forecast Days", min_value=1, max_value=5, help="Select the number of forecasted days.")
option = st.selectbox("Select data to view", ("Temperature", "Sky"))

st.subheader(f"{option} for the next {days} {'day' if days == 1 else 'days'} in {place}")

def get_data(days):
    dates = ["2022-25-10", "2022-26-10", "2022-27-10"]
    temperatures = [10, 11, 12]
    temperatures = [days * i for i in temperatures]
    return dates, temperatures

day, temp = get_data(days)

figure = px.line(x=day, y=temp, labels={"x": "Dates", "y": "Temperature(C)"})
st.plotly_chart(figure)
