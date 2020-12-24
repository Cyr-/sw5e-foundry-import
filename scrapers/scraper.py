import json
import requests

r = requests.get("https://sw5eapi.azurewebsites.net/api/equipment")
data = json.loads(r.text)

out = []

# whatever you need to scrape, just sling it in here
for e in data:
    if e["equipmentCategory"] == "Kit":
        out.append(e)

with open("out.txt", "w") as file:
    for line in out:
        file.write(str(line) + "\n")
