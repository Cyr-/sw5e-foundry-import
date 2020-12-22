import json
import re

from weapon.weaponIds import weapon_IDs
from weapon.template import template


def generateWeaponDbFile(weapons, fileName):
    db = []

    for weapon in weapons:
        item = weapon
        item["name"] = item["name"] if item["name"].upper() == item["name"] else item["name"].title()
        item["_id"] = weapon_IDs[item["name"]]
        item["description"] = generateDescription(item)
        
        if "Ammunition" in item["propertiesMap"]:
            rangeString = re.findall('\d+\/\d+', item["propertiesMap"]["Ammunition"])
            if len(rangeString) == 1 and len(rangeString[0].split("/")) == 2:
                item["range"] = {
                    "value": rangeString[0].split("/")[0],
                    "long": rangeString[0].split("/")[1],
                    "units": "ft"
                }
            else: 
                item["range"] = {
                    "value": "null",
                    "long": "null",
                    "units": "spec"
                }
        elif "Range" in item["propertiesMap"]:
            rangeString = re.findall('\d+\/\d+', item["propertiesMap"]["Range"])
            if len(rangeString) == 1 and len(rangeString[0].split("/")) == 2:
                item["range"] = {
                    "value": rangeString[0].split("/")[0],
                    "long": rangeString[0].split("/")[1],
                    "units": "ft"
                }
            else:
                rangeString = re.findall('\d+', item["propertiesMap"]["Range"])
                item["range"] = {
                    "value": rangeString[0],
                    "long": "null",
                    "units": "ft"
                }
        elif "Reach" in item["propertiesMap"]:
            item["range"] = {
                "value": 10,
                "long": "null",
                "units": "ft"
            }
        else:
            item["range"] = {
                "value": 5,
                "long": "null",
                "units": "ft"
            }

        item["save"] = {}
        
        if "DC" in item["description"] and item["damageDieType"] == 0:
            item["action"] = {
                "type": "save"
            }
            dcString = re.findall('DC \d+ \w+', item["description"])
            dcString = dcString[0].split(" ")
            item["save"] = {
                "ability": dcString[2][0:3].lower(),
                "dc": dcString[1],
                "scaling": "flat"
            }
        elif "Ammunition" in item["propertiesMap"] or "Range" in item["propertiesMap"]:
            item["action"] = {
                "type": "rwak"
            }
        else:
            item["action"] = {
                "type": "mwak"
            }
        
        if "Blaster" in item["weaponClassification"]:
            item["consume"] = {
                "type": "ammo",
                "amount": 1
            }
        else:
            item["consume"] = {}
        
        if "damageNumberOfDice" in item and item["damageNumberOfDice"] != 0:
            item["damageRoll"] = str(item["damageNumberOfDice"]) + "d" + str(item["damageDieType"]) + " + @mod"
            item["damageType"] = item["damageType"].lower()
        
        if "Versatile" in item["propertiesMap"]:
            item["versatileDamageRoll"] = item["propertiesMap"]["Versatile"].lower().replace("versatile (", "").replace(")", "") + " + @mod"

        if item["weaponClassification"] == "SimpleBlaster":
            item["weaponType"] = "simpleB";
        elif item["weaponClassification"] == "MartialBlaster":
            item["weaponType"] = "martialB";
        elif item["weaponClassification"] == "SimpleVibroweapon":
            item["weaponType"] = "simpleVW";
        elif item["weaponClassification"] == "MartialVibroweapon":
            item["weaponType"] = "martialVW";
        elif item["weaponClassification"] == "SimpleLightweapon":
            item["weaponType"] = "simpleLW";
        elif item["weaponClassification"] == "MartialLightweapon":
            item["weaponType"] = "martialLW";

        item["properties"] = {
            "amm": "true" if "Ammunition" in item["propertiesMap"] else "false",
            "aut": "true" if "Auto" in item["propertiesMap"] else "false",
            "bur": "true" if "Burst" in item["propertiesMap"] else "false",
            "def": "true" if "Defensive" in item["propertiesMap"] else "false",
            "dex": "true" if "Dexterity" in item["propertiesMap"] else "false",
            "dir": "true" if "Dire" in item["propertiesMap"] else "false",
            "drm": "true" if "Disarming" in item["propertiesMap"] else "false",
            "dgd": "true" if "Disguised" in item["propertiesMap"] else "false",
            "dis": "true" if "Disintegrate" in item["propertiesMap"] else "false",
            "dpt": "true" if "Disruptive" in item["propertiesMap"] else "false",
            "dou": "true" if "Double" in item["propertiesMap"] else "false",
            "fin": "true" if "Finesse" in item["propertiesMap"] else "false",
            "fix": "true" if "Fixed" in item["propertiesMap"] else "false",
            "foc": "true" if "Focus" in item["propertiesMap"] else "false",
            "hvy": "true" if "Heavy" in item["propertiesMap"] else "false",
            "hid": "true" if "Hidden" in item["propertiesMap"] else "false",
            "ken": "true" if "Keen" in item["propertiesMap"] else "false",
            "lgt": "true" if "Light" in item["propertiesMap"] else "false",
            "lum": "true" if "Luminous" in item["propertiesMap"] else "false",
            "mig": "true" if "Mighty" in item["propertiesMap"] else "false",
            "pic": "true" if "Piercing" in item["propertiesMap"] else "false",
            "rap": "true" if "Rapid" in item["propertiesMap"] else "false",
            "rch": "true" if "Reach" in item["propertiesMap"] else "false",
            "rel": "true" if "Reload" in item["propertiesMap"] else "false",
            "ret": "true" if "Returning" in item["propertiesMap"] else "false",
            "shk": "true" if "Shocking" in item["propertiesMap"] else "false",
            "sil": "true" if "Silent" in item["propertiesMap"] else "false",
            "spc": "true" if "Special" in item["propertiesMap"] else "false",
            "str": "true" if "Strength" in item["propertiesMap"] else "false",
            "thr": "true" if "Thrown" in item["propertiesMap"] else "false",
            "two": "true" if "Two-Handed" in item["propertiesMap"] else "false",
            "ver": "true" if "Versatile" in item["propertiesMap"] else "false",
            "vic": "true" if "Vicious" in item["propertiesMap"] else "false"
        }
        item["img"] = "systems/sw5e/packs/Icons/" + "%20".join(re.findall('[A-Z][^A-Z]*', item["weaponClassification"])) + "s/" + item["name"].replace(" ","%20") + ".webp"

        db.append(item)

    generateUnarmedStrike(db)

    db.sort(key=lambda item: item["_id"])

    with open("output/" + fileName, "w") as file:
        for line in db:
            file.write(template.render(item = line) + "\n")


def generateDescription(item):
    description = ""

    propertyValues = [
        "Burst" in item["propertiesMap"] and item["propertiesMap"]["Burst"],
        "Dexterity" in item["propertiesMap"] and item["propertiesMap"]["Dexterity"],
        "Double" in item["propertiesMap"] and item["propertiesMap"]["Double"],
        "Rapid" in item["propertiesMap"] and item["propertiesMap"]["Rapid"],
        "Reload" in item["propertiesMap"] and item["propertiesMap"]["Reload"],
        "Strength" in item["propertiesMap"] and item["propertiesMap"]["Strength"],
        item["properties"]["switch"] if "switch" in [property.lower() for property in item["properties"]] else False
    ]

    filteredPropertyValues = [property for property in propertyValues if property != False]

    if filteredPropertyValues:
        separator = ", "
        description += "<p>" + separator.join([property.title() for property in filteredPropertyValues]) + "</p>"

    if item["description"]:
        description += "<p>" + item["description"].replace("\r", "").replace("\n", " ") + "</p>"

    return description

def generateUnarmedStrike(db):
    item = {}
    item["name"] = "Unarmed Strike"
    item["_id"] = weapon_IDs[item["name"]]
    item["contentSource"] = "PHB"
    item["weight"] = 0
    item["cost"] = 0
    item["range"] = {
        "value": 5,
        "long": "null",
        "units": "ft"
    }
    item["save"] = {}
    item["action"] = {
        "type": "mwak"
    }
    item["consume"] = {}
    item["damageRoll"] = "1 + @mod"
    item["damageType"] = "kinetic"
    item["weaponType"] = "natural"
    item["properties"] = {
        "amm": "false",
        "aut": "false",
        "bur": "false",
        "def": "false",
        "dex": "false",
        "dir": "false",
        "drm": "false",
        "dgd": "false",
        "dis": "false",
        "dpt": "false",
        "dou": "false",
        "fin": "false",
        "fix": "false",
        "foc": "false",
        "hvy": "false",
        "hid": "false",
        "ken": "false",
        "lgt": "false",
        "lum": "false",
        "mig": "false",
        "pic": "false",
        "rap": "false",
        "rch": "false",
        "rel": "false",
        "ret": "false",
        "shk": "false",
        "sil": "false",
        "spc": "false",
        "str": "false",
        "thr": "false",
        "two": "false",
        "ver": "false",
        "vic": "false"
    }
    item["img"] = "icons/svg/mystery-man.svg"

    db.append(item)