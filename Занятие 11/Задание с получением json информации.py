import requests
import json

url = "https://api.github.com/repos/Automattic/wp-calypso"
response = requests.get(url)
data = response.json()

with open('TOP_9.json', 'w') as f:
    json.dump(data, f, indent=4)