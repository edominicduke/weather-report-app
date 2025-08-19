import requests
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("WEATHER_API_KEY") # Retrieve the API key

def get_city_name_and_state_code():
    """
    Prompt the user for the US city whose weather they want to check and return the city name and state code.
    
    Parameters:
    - None
    
    Returns:
    - city_name (str): The name of the US city.
    - state_code (str): The state code of the US city.
    """
    print("Welcome to the Weather Report App! This program provides the current weather information of any city in the U.S.")
    city_info = input("Please enter the U.S. city you want to check the weather for (city name, state code): ")
    city_name, state_code = city_info.split(", ")
    return city_name, state_code

def get_geocoding_data(city_name, state_code):
    """
    Return a dictionary containing the data returned by OpenWeather's Geocoding API for the given city and state code.
    
    Parameters:
    - city_name (str): The name of the US city.
    - state_code (str): The state code of the US city.
    
    Returns:
    - geocoding_response (dict): A dictionary containing the geocoding data returned by OpenWeather's Geocoding API.
    """
    geocoding_response = requests.get(f"http://api.openweathermap.org/geo/1.0/direct?q={city_name},{state_code},{1}&limit={1}&appid={api_key}")
    return geocoding_response.json()

def get_weather_data(latitude, longitude):
    """
    Return a dictionary containing the data returned by the OpenWeather's Current Weather API for the given latitude and longitude.
    
    Parameters:
    - latitude (float): The latitude of the city.
    - longitude (float): The longitude of the city.
    
    Returns:
    - weather_response (dict): A dictionary containing the current weather data returned by OpenWeather's Current Weather API.
    """
    weather_response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={api_key}")
    return weather_response.json()

def report_weather(temperature_celsius, humidity, description):
    """
    Print the weather report for the given temperature, humidity, and description.
    
    Parameters:
    - temperature_celsius (float): The temperature in Celsius.
    - humidity (int): The humidity percentage.
    - description (str): A description of the weather conditions.
    
    Returns:
    - None
    """
    print(f"Weather report for {city_name}, {state_code}: ")
    print(f"Temperature: {temperature_celsius:.2f}°C")
    print(f"Humidity: {humidity}%")
    print(f"Description: {description}")

# Main program execution
city_name, state_code = get_city_name_and_state_code()

geocoding_data = get_geocoding_data(city_name, state_code)

latitude = geocoding_data[0]['lat']
longitude = geocoding_data[0]['lon']

weather_data = get_weather_data(latitude, longitude)

temperature_kelvin = weather_data['main']['temp']
temperature_celsius = temperature_kelvin - 273.15 # Convert the temperature from Kelvin to Celsius
humidity = weather_data['main']['humidity']
description = weather_data['weather'][0]['description']

report_weather(temperature_celsius, humidity, description)