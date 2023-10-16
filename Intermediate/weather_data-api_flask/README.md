# Weather Data API ⛈️

The Flask Weather Data API is a Python-based web application created using Flask. This API serves weather data to users and offers several endpoints for retrieving information about weather stations, weather data by station and date, all data for a station, and yearly data for a station.

## Installation 🏗️

### Prerequisites
* Python 3.7+
* Flask
* pandas

### Setup 
1. Data File: The API requires a data file that contains weather information. In this example, the data file is "data_small/stations.txt" and station-specific files like "TG_STAID000001.txt."
2. Application Configuration: The Flask application is initialized with routes for different endpoints, as seen in the provided code. You can customize the routes and data sources as needed.

### running the application
Run the application by executing the provided Python script, which initializes the Flask app and starts the development server:

https://github.com/MCdev92/python-projects/blob/master/Intermediate/weather_data-api_flask/main.py

### Using the API
The API provides endpoints for retrieving weather data. You can interact with the API by making HTTP requests to these endpoints using tools like Postman, cURL, or by building client applications.

## Endpoints
*  The API offers the following endpoints:

1. /api/v1/{station}/{date}
    Retrieves temperature data for a specific weather station on a given date.
    Example request: /api/v1/000001/20221025

2. /api/v1/{station}
    Retrieves all data for a specific weather station.
    Example request: /api/v1/000001

3. /api/v1/yearly/{station}/{year}
    Retrieves yearly data for a specific weather station for a given year.
    Example request: /api/v1/yearly/000001/2022
