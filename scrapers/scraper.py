import json
import requests

r = requests.get("https://sw5eapi.azurewebsites.net/api/equipment")
data = json.loads(r.text)

out = []

# whatever you need to scrape, just sling it in here
for e in data:
    if e["equipmentCategory"] == "Explosive":
        out.append(e)

with open("out.txt", "a") as file:
    for line in out:
        file.write(str(line) + "\n")
