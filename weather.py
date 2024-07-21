import requests

API_KEY = '1bec01f8248a76771f8906b4590de8fe'

# List of African cities to get weather information for
cities = ["Cairo", "Lagos", "Nairobi", "Johannesburg", "Accra", "Kinshasa", "Addis Ababa", "Khartoum", "Algiers", "Casablanca"]

def get_weather_data(city):
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = base_url + "q=" + city + "&appid=" + API_KEY + "&units=metric"
    response = requests.get(complete_url)
    return response.json()

def print_weather_info(city, weather_data):
    if weather_data['cod'] == 200:
        main = weather_data['main']
        wind = weather_data['wind']
        weather_desc = weather_data['weather'][0]['description']
        
        temperature = main['temp']
        feels_like = main['feels_like']
        humidity = main['humidity']
        wind_speed = wind['speed']
        
        print(f"Weather in {city}:")
        print(f"  Temperature: {temperature}°C")
        print(f"  Feels Like: {feels_like}°C")
        print(f"  Humidity: {humidity}%")
        print(f"  Wind Speed: {wind_speed} m/s")
        print(f"  Description: {weather_desc.capitalize()}")
        print()
    else:
        print(f"Could not retrieve weather data for {city}")

def main():
    for city in cities:
        weather_data = get_weather_data(city)
        print_weather_info(city, weather_data)

if __name__ == "__main__":
    main()
