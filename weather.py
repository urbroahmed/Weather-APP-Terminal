import requests


banner = r"""
    ██╗  ██╗███████╗██████╗ ████████╗██╗  ██╗███████╗██████╗    █████╗ ██████╗ ██████╗ 
    ██║  ██║██╔════╝██╔══██╗╚══██╔══╝██║  ██║██╔════╝██╔══██╗  ██╔══██╗██╔══██╗██╔══██╗
    ██║  ██║█████╗  ██████╔╝   ██║   ███████║█████╗  ██████╔╝  ███████║██████╔╝██████╔╝
    ██║██║██║██╔══╝  ██╔══██╗   ██║   ██╔══██║██╔══╝  ██╔══██╗  ██╔══██║██╔═══╝ ██╔═══╝ 
    █████╗██║███████╗██║  ██║   ██║   ██║  ██║███████╗██║  ██║  ██║  ██║██║     ██║     
    ╚════╝╚═╝╚══════╝╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝  ╚═╝  ╚═╝╚═╝     ╚═╝   ☼
        Weather App - Check the current weather in any city around the world!
                Just enter the city name and get the current temperature in Celsius.
"""
print(banner)

while True:
    city = input("Enter the city name: ")
    geo_url = f"https://geocoding-api.open-meteo.com/v1/search?name={city}&count=1"
    geo_data = requests.get(url=geo_url).json()

    if 'results' not in geo_data or not geo_data['results']:
        print("City not found. Please try again. \n")
        continue

    lon = geo_data['results'][0]['longitude']
    lat = geo_data['results'][0]['latitude']



    weather_url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
    weather_data = requests.get(url=weather_url).json()


    if 'current_weather' in weather_data:
        data = weather_data
        print(f"Temperature in  {city.capitalize()}: {data['current_weather']['temperature']}°C")
    else:
        print("Error fetching weather data.")