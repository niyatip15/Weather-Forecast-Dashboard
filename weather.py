import requests

API_KEY = "b8588eac7583f51f2360e949a0dced05"

def get_weather_data(place,forecasted_days=None):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()
    filtered_data = data["list"]
    number_values = 8 * forecasted_days 
    filtered_data = filtered_data[:number_values]
    return filtered_data

if __name__ =="__main__":
    print(get_weather_data(place='Ahmedabad',forecasted_days=3))