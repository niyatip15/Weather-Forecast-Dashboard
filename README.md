# Weather Forecast Dashboard

This Streamlit application allows users to view weather forecasts for different locations. Users can select a location, specify the number of forecasted days (up to 5 days), and choose the type of weather data they want to visualize (temperature).

## Features

- **Location Selection**: Users can input the name of the location for which they want to view the weather forecast.

- **Forecast Days Slider**: Users can use a slider to specify the number of days for which they want to see the weather forecast, up to 5 days.

- **Weather Data Visualization**: Users can choose to view temperature data for the selected location and forecasted days.

## Getting Started

To run the weather forecast dashboard locally, follow these steps:

1. Clone this repository to your local machine.

2. Install the required Python packages. You can do this by running:
   ```
   pip install -r requirements.txt
   ```

3. Run the Streamlit application using the following command:
   ```
   streamlit run main.py
   ```

4. Once the application is running, you can access it in your web browser.

## Usage

1. Input the name of the location for which you want to view the weather forecast in the provided text box.

2. Use the slider to specify the number of forecasted days (up to 5 days).

3. Select "Temperature" or "Sky" as the type of weather data to visualize.

4. Click the "Submit" button to view the weather forecast for the selected location and forecasted days.

## Technologies Used

- Python: The backend logic and data processing are implemented in Python.
- Streamlit: The web application framework used for building the user interface.
- Plotly: The library used for interactive data visualization.

## Directory Structure

- `main.py`: The main Python script containing the Streamlit application code.
- `requirements.txt`: A file listing the required Python packages and their versions
