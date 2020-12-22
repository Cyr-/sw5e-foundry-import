import json
import requests

r = requests.get("https://sw5eapi.azurewebsites.net/api/equipment")
data = json.loads(r.text)

out = []

for e in data:
    if e["equipmentCategory"] == "Ammunition":
        out.append(e)

with open("out.txt", "a") as file:
    for line in out:
        file.write(str(line) + "\n")
