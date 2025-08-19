# Weather Report App

This weather report app, developed for my AIPI 503 - Python Bootcamp class at Duke University, is intended
to report the weather information of any US city that the user prompts for by leveraging OpenWeather's Current Weather API and OpenWeather's Geocoding API. The reported information includes the current temperature, humidity, and a brief description (cloudy, clear, etc). This app is for anyone interested in checking the current weather of one or more US cities.

## Getting Started

### Prerequisites
- Python 3.10+
- Git

### Installation
'''bash

git clone https://github.com/edominicduke/weather-report-app.git

cd weather-report-app

python3 -m venv .venv

source .venv/bin/activate

pip install -r requirements.txt

### Usage
python3 report_weather.py

### Additional Resources
[OpenWeather's Current Weather API](https://openweathermap.org/current)

[OpenWeather's Geocoding API](https://openweathermap.org/current#geocoding)