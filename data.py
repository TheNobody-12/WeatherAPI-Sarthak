""" 
Author: Sarthak Kapaliya
Github Username: TheNobody-12
Description:
Weather Forecasting Tool -  a command line tool that 
accepts a city's name and returns the current weather forecast. 
Leveraging OpenWeatherMap API to fetch weather data and parse it
using Python.
"""
import requests
import os

from dotenv import load_dotenv
from os import path

# load dotenv in the base root
APP_ROOT = os.path.join(os.path.dirname(__file__), '.')   # refers to application_top
dotenv_path = os.path.join(APP_ROOT, '.env')
load_dotenv(dotenv_path)
API_key = os.getenv('API_KEY')

def index(city_name, API_key):
    
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&appid={}'
    # Here we use Copilot to generate the code to fetch the weather data from the API.
    response = requests.get(url.format(city_name,API_key)).json() # Fetching the weather data from the API

    country = response['sys']['country'] # Extracting the country from the API response
    temp = response['main']['temp'] # Extracting the temperature from the API response
    weather = response['weather'][0]['main'] # Extracting the weather from the API response
    min_temp = response['main']['temp_min'] # Extracting the minimum temperature from the API response
    max_temp = response['main']['temp_max'] # Extracting the maximum temperature from the API response
    humidity = response['main']['humidity'] # Extracting the humidity from the API response
    wind_speed = response['wind']['speed'] # Extracting the wind speed from the API response

    # return output in command line
    return print(f"Country: {country} \nTemperature: {temp}\nWeather: {weather}\nMinimum Temperature: {min_temp}\nMaximum Temperature: {max_temp}\nHumidity: {humidity}\nWind Speed: {wind_speed}")


city_name = input("Enter the city name: ")
print("Fetching weather data...")
try:
    print("Weather data fetched successfully!")
    print("Here is the weather forecast for", city_name)
    index(city_name, API_key)
except:
    print("Error! Please try again.")
        




