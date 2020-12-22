import json
import requests
import pickle

from utilities.paths import pickle_to_dict

# generate imports
from armor.generate import generateArmorDbFile
from weapons.generate import generateWeaponDbFile

r = requests.get("https://sw5eapi.azurewebsites.net/api/equipment")
equipment = json.loads(r.text)

weapons = [item for item in equipment if item['equipmentCategory'] == 'Weapon']
armors = [item for item in equipment if item['equipmentCategory'] == 'Armor']
weaponOrArmorAccessories = [item for item in equipment if item['equipmentCategory'] == 'WeaponOrArmorAccessory']
spice = [item for item in equipment if item['equipmentCategory'] == 'Spice']
medicals = [item for item in equipment if item['equipmentCategory'] == 'Medical']
lifeSupports = [item for item in equipment if item['equipmentCategory'] == 'LifeSupport']
kits = [item for item in equipment if item['equipmentCategory'] == 'Kit']
tools = [item for item in equipment if item['equipmentCategory'] == 'Tool']
storages = [item for item in equipment if item['equipmentCategory'] == 'Storage']
musicalInstruments = [item for item in equipment if item['equipmentCategory'] == 'MusicalInstrument']
utilities = [item for item in equipment if item['equipmentCategory'] == 'Utility']
gamingSets = [item for item in equipment if item['equipmentCategory'] == 'GamingSet']
clothings = [item for item in equipment if item['equipmentCategory'] == 'Clothing']
dataRecordingAndStorages = [item for item in equipment if item['equipmentCategory'] == 'DataRecordingAndStorage']
communications = [item for item in equipment if item['equipmentCategory'] == 'Communications']
ammunitions = [item for item in equipment if item['equipmentCategory'] == 'Ammunition']
alcoholicBeverages = [item for item in equipment if item['equipmentCategory'] == 'AlcoholicBeverage']
explosives = [item for item in equipment if item['equipmentCategory'] == 'Explosive']

# iterate through all the pickle paths
for path in pickle_to_dict.keys():
    if not path.exists():
        # pickle file does not exists, therefore this is the first time
        # this is being run on this system
        pickle.dump(pickle_to_dict[path], open(path, "wb"))

generateWeaponDbFile(weapons, 'weapons.db')
generateArmorDbFile(armors, 'armor.db')
