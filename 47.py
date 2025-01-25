import requests
import json

response = requests.get('http://api.open-notify.org/astros.json')

if response.status_code == 200: # checks if response is good
    data = json.loads(response.content)
    print("Data retrieved")
else:
    print("Data not found")

print("Name                  | Craft")
print("----------------------|-----------")

for person in data['people']:
    print(f"{person['name']:<20}  | {person['craft']}")