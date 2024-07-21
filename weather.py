import requests
import os
from dotenv import load_dotenv
import pyttsx3

# Load environment variables from .env file
load_dotenv()

# Retrieve API key from environment variable
API_KEY = os.getenv('OPENWEATHERMAP_API_KEY')

# Initialize the TTS engine
engine = pyttsx3.init()

# List of African cities to get weather information for
cities = ["Cairo", "Lagos", "Nairobi", "Johannesburg", "Accra", "Kinshasa", "Addis Ababa", "Khartoum", "Algiers", "Casablanca"]

def get_weather_data(city):
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = base_url + "q=" + city + "&appid=" + API_KEY + "&units=metric"
    response = requests.get(complete_url)
    return response.json()

def speak_weather_info(city, weather_data):
    if weather_data['cod'] == 200:
        main = weather_data['main']
        wind = weather_data['wind']
        weather_desc = weather_data['weather'][0]['description']
        
        temperature = main['temp']
        feels_like = main['feels_like']
        humidity = main['humidity']
        wind_speed = wind['speed']
        
        weather_info = (
            f"Weather in {city}: "
            f"Temperature is {temperature} degrees Celsius. "
            f"It feels like {feels_like} degrees Celsius. "
            f"Humidity is {humidity} percent. "
            f"Wind speed is {wind_speed} meters per second. "
            f"Description: {weather_desc.capitalize()}."
        )
        
        print(weather_info)
        engine.say(weather_info)
        engine.runAndWait()
    else:
        error_message = f"Could not retrieve weather data for {city}"
        print(error_message)
        engine.say(error_message)
        engine.runAndWait()

def main():
    for city in cities:
        weather_data = get_weather_data(city)
        speak_weather_info(city, weather_data)

if __name__ == "__main__":
    main()
