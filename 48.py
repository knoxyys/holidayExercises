import requests
import os
import json
apikey = os.getenv('48_API_KEY')

loc = input("Where are you? (Name of city) ")
locapi = requests.get(f'http://api.openweathermap.org/geo/1.0/direct?q={loc}&limit=5&appid={apikey}') # uses other api to get coordinates from name
if locapi.status_code == 200:
    locdata = json.loads(locapi.content)
    lat = locdata[0]['lat']
    lon = locdata[0]['lon']
else:
    print('Coordinate data not found')



weatherapi = requests.get(f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={apikey}')
if weatherapi.status_code == 200:
    weather_data = json.loads(weatherapi.content)
else:
    print('Weather data not found')

kelvin_temp = weather_data['main']['temp']

print(f"Weather in {weather_data['name']}:")
print(f"{kelvin_temp - 273.15:.2f} degrees celcius.")