import requests

API_KEY = "b8588eac7583f51f2360e949a0dced05"

def get_weather_data(place,forecasted_days=None,type_of_view=None):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()
    filtered_data = data["list"]
    number_values = 8 * forecasted_days 
    filtered_data = filtered_data[:number_values]
    if type_of_view == 'Temperature':
        filtered_data = [dict["main"]["temp"] for dict in filtered_data]
    if type_of_view == 'Sky':
        filtered_data = [dict["weather"][0]["main"] for dict in filtered_data]
    return filtered_data

if __name__ =="__main__":
    print(get_weather_data(place='Ahmedabad',forecasted_days=3,type_of_view='Temperature'))