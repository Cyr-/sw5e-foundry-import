import json
import requests

r = requests.get("https://sw5eapi.azurewebsites.net/api/equipment")
data = json.loads(r.text)

for e in data:
    print(e["equipmentCategory"])