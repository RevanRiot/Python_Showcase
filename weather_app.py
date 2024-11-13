# File: weather_app.py

import requests

def get_weather(city):
    """Fetches weather data for a given city using OpenWeatherMap API."""
    api_key = "your_api_key"  # Replace with your OpenWeatherMap API key
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    
    try:
        params = {"q": city, "appid": api_key, "units": "metric"}
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        weather_data = response.json()
        
        # Display the weather data
        print(f"City: {weather_data['name']}")
        print(f"Temperature: {weather_data['main']['temp']}°C")
        print(f"Weather: {weather_data['weather'][0]['description'].capitalize()}")
    except requests.exceptions.RequestException as e:
        print(f"Error fetching weather data: {e}")

if __name__ == "__main__":
    city_name = input("Enter the city name: ")
    get_weather(city_name)
