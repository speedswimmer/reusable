# Script using openweathermap.org API to get basic weather data for specific cities!
import sys
import requests

API_KEY = "{your API Key}"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

if len(sys.argv) !=2:
    print("Please enter city name in front of the app-name")

city = sys.argv[1]
#city = input("Enter a city name: ")
request_url = f"{BASE_URL}?appid={API_KEY}&q={city}"
response = requests.get(request_url)

if response.status_code == 200:
    data = response.json()

#    print(data)
    country = data['sys']['country']
    city_plain = data['name']
    weather = data['weather'][0]['description']
    temperature = round(data["main"]["temp"] - 273.15, 1)
    print(f"Weather in {city_plain}/{country}:", weather)
    print("Temperature:", temperature, "°C")

else:
    print("An error occured.")