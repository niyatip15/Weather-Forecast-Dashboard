import streamlit as st
import plotly.express as px
from weather import get_weather_data

st.title("Weather Forecast for Next Days")
place = st.text_input("Place: ")
days = st.slider("Forecast Days", min_value=1, max_value=5, help="Select the number of forecasted days.")
option = st.selectbox("Select data to view", ("Temperature", "Sky"))

st.subheader(f"{option} for the next {days} {'day' if days == 1 else 'days'} in {place}")

if place:
    try:
        filtered_data = get_weather_data(place,days)

        if option == "Temperature":
            temperatures = [weather_dict["main"]["temp"] / 10 for weather_dict in filtered_data]
            dates = [weather_dict["dt_txt"] for weather_dict in filtered_data]
            figure = px.line(x=dates, y=temperatures, labels={"x": "Dates", "y": "Temperature(C)"})
            st.plotly_chart(figure)
        elif option == "Sky":
            images = {"Clear": "images/clear.png","Clouds":"images/cloud.png",
                    "Rain":"images/rain.png","Snow":"images/snow.png"}
            filtered_data = [weather_dict["weather"][0]["main"] for weather_dict in filtered_data]
            image_paths = [images[condition] for condition in filtered_data]
            st.image(image_paths,width=115)
        else:
            option = None
    except KeyError:
        st.write("This place does not exist.")
