import requests
import os
import json
lat = -33.865143
lon = 151.209900
apikey = os.getenv('48_API_KEY')

response = requests.get(f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={apikey}')
if response.status_code == 200:
    data = json.loads(response.content)
else:
    print('Data not found')

kelvin_temp = data['main']['temp']

print(f"Weather in {data['name']}:")
print(f"{kelvin_temp - 273.15:.2f} degrees celcius.")