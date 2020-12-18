import json
import requests

from armor.generate import generateArmorDbFile

# r = requests.get("https://sw5eapi.azurewebsites.net/api/equipment")
# equipment = json.loads(r.text)

# weapons = [item for item in equipment if item['equipmentCategory'] == 'Weapon']

# armors = [item for item in equipment if item['equipmentCategory'] == 'Armor']

generateArmorDbFile()