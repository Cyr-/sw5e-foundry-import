import re

from weapons.template import template
from utilities.paths import weap_path
from utilities.SW5e_ID_Mgmt import getID


def generateWeaponDbFile(weapons, fileName):
    db = []

    for weapon in weapons:
        item = weapon
        item["name"] = item["name"] if item["name"].upper() == item["name"] else item["name"].title()
        item["_id"] = getID(item["name"], weap_path)
        item["description"] = generateDescription(item)

        if item["weight"] == "1/4":
            item["weight"] = "0.25"

        if item["name"] == "Bo-Rifle":
            generateBoRifle(db, item)
            continue
        elif item["name"] == "IWS":
            generateIWS(db, item)
            continue

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
        elif (
            item["name"] == "Flechette Cannon" or
            item["name"] == "Grenade Launcher" or
            item["name"] == "Rocket Launcher" or
            item["name"] == "Vapor Projector" or
            item["name"] == "Wrist Launcher" or
            item["name"] == "Torpedo Launcher"
        ):
            item["action"] = {}
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

    switch = re.search('switch \(\d+d\d+ [\w/]+\)', item["propertiesJson"], re.IGNORECASE)

    propertyValues = [
        "Burst" in item["propertiesMap"] and item["propertiesMap"]["Burst"],
        "Defensive" in item["propertiesMap"] and item["propertiesMap"]["Defensive"],
        "Dexterity" in item["propertiesMap"] and item["propertiesMap"]["Dexterity"],
        "Dire" in item["propertiesMap"] and item["propertiesMap"]["Dire"],
        "Disintegrate" in item["propertiesMap"] and item["propertiesMap"]["Disintegrate"],
        "Double" in item["propertiesMap"] and item["propertiesMap"]["Double"],
        "Keen" in item["propertiesMap"] and item["propertiesMap"]["Keen"],
        "Piercing" in item["propertiesMap"] and item["propertiesMap"]["Piercing"],
        "Rapid" in item["propertiesMap"] and item["propertiesMap"]["Rapid"],
        "Reload" in item["propertiesMap"] and item["propertiesMap"]["Reload"],
        "Shocking" in item["propertiesMap"] and item["propertiesMap"]["Shocking"],
        "Strength" in item["propertiesMap"] and item["propertiesMap"]["Strength"],
        switch.group(0) if switch is not None else False,
        "Vicious" in item["propertiesMap"] and item["propertiesMap"]["Vicious"]
    ]

    filteredPropertyValues = [property for property in propertyValues if property]

    if filteredPropertyValues:
        separator = ", "
        description += "<p>" + separator.join([property.title() for property in filteredPropertyValues]) + "</p>"

    if item["description"]:
        description += "<p>" + item["description"].replace("\r", "").replace("\n", " ") + "</p>"

    return description

def generateUnarmedStrike(db):
    item = {}
    item["name"] = "Unarmed Strike"
    item["_id"] = getID(item["name"], weap_path)
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

def generateBoRifle(db, item):
    # Rifle
    rifle = {}
    rifle["name"] = item["name"] + " (Rifle)"
    rifle["_id"] = getID(rifle["name"], weap_path)
    rifle["description"] = item["description"]
    rifle["contentSource"] = item["contentSource"]
    rifle["weight"] = item["weight"]
    rifle["cost"] = item["cost"]
    rifle["range"] = {
        "value": 100,
        "long": 400,
        "units": "ft"
    }
    rifle["save"] = {}
    rifle["action"] = {
        "type": "rwak"
    }
    rifle["consume"] = {}
    rifle["damageRoll"] = "1d8 + @mod"
    rifle["damageType"] = "energy"
    rifle["weaponType"] = "martialB"
    rifle["properties"] = {
        "amm": "true",
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
        "rel": "true",
        "ret": "false",
        "shk": "false",
        "sil": "false",
        "spc": "true",
        "str": "false",
        "thr": "false",
        "two": "true",
        "ver": "false",
        "vic": "false"
    }
    rifle["img"] = "systems/sw5e/packs/Icons/" + "%20".join(re.findall('[A-Z][^A-Z]*', item["weaponClassification"])) + "s/" + item["name"].replace(" ","%20") + ".webp"

    db.append(rifle)

    # Staff
    staff = {}
    staff["name"] = item["name"] + " (Staff)"
    staff["_id"] = getID(staff["name"], weap_path)
    staff["description"] = item["description"]
    staff["contentSource"] = item["contentSource"]
    staff["weight"] = 0
    staff["cost"] = 0
    staff["range"] = {
        "value": 5,
        "long": "null",
        "units": "ft"
    }
    staff["save"] = {}
    staff["action"] = {
        "type": "mwak"
    }
    staff["consume"] = {}
    staff["damageRoll"] = "1d8 + @mod"
    staff["damageType"] = "kinetic"
    staff["weaponType"] = "martialVW"
    staff["properties"] = {
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
        "dou": "true",
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
        "shk": "true",
        "sil": "false",
        "spc": "true",
        "str": "false",
        "thr": "false",
        "two": "true",
        "ver": "false",
        "vic": "false"
    }
    staff["img"] = "systems/sw5e/packs/Icons/" + "%20".join(re.findall('[A-Z][^A-Z]*', item["weaponClassification"])) + "s/" + item["name"].replace(" ","%20") + ".webp"

    db.append(staff)

def generateIWS(db, item):
    # Blaster
    blaster = {}
    blaster["name"] = item["name"] + " (Blaster)"
    blaster["_id"] = getID(blaster["name"], weap_path)
    blaster["description"] = item["description"]
    blaster["contentSource"] = item["contentSource"]
    blaster["weight"] = item["weight"]
    blaster["cost"] = item["cost"]
    blaster["range"] = {
        "value": 80,
        "long": 320,
        "units": "ft"
    }
    blaster["save"] = {}
    blaster["action"] = {
        "type": "rwak"
    }
    blaster["consume"] = {}
    blaster["damageRoll"] = "1d8 + @mod"
    blaster["damageType"] = "energy"
    blaster["weaponType"] = "martialB"
    blaster["properties"] = {
        "amm": "true",
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
        "rel": "true",
        "ret": "false",
        "shk": "false",
        "sil": "false",
        "spc": "true",
        "str": "true",
        "thr": "false",
        "two": "true",
        "ver": "false",
        "vic": "false"
    }
    blaster["img"] = "systems/sw5e/packs/Icons/" + "%20".join(re.findall('[A-Z][^A-Z]*', item["weaponClassification"])) + "s/" + item["name"].replace(" ","%20") + ".webp"

    db.append(blaster)

    # Sniper
    sniper = {}
    sniper["name"] = item["name"] + " (Sniper)"
    sniper["_id"] = getID(sniper["name"], weap_path)
    sniper["description"] = item["description"]
    sniper["contentSource"] = item["contentSource"]
    sniper["weight"] = 0
    sniper["cost"] = 0
    sniper["range"] = {
        "value": 120,
        "long": 480,
        "units": "ft"
    }
    sniper["save"] = {}
    sniper["action"] = {
        "type": "rwak"
    }
    sniper["consume"] = {}
    sniper["damageRoll"] = "1d12 + @mod"
    sniper["damageType"] = "energy"
    sniper["weaponType"] = "martialB"
    sniper["properties"] = {
        "amm": "true",
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
        "rel": "true",
        "ret": "false",
        "shk": "false",
        "sil": "false",
        "spc": "true",
        "str": "true",
        "thr": "false",
        "two": "true",
        "ver": "false",
        "vic": "false"
    }
    sniper["img"] = "systems/sw5e/packs/Icons/" + "%20".join(re.findall('[A-Z][^A-Z]*', item["weaponClassification"])) + "s/" + item["name"].replace(" ","%20") + ".webp"

    db.append(sniper)

    # Antiarmor
    antiarmor = {}
    antiarmor["name"] = item["name"] + " (Antiarmor)"
    antiarmor["_id"] = getID(antiarmor["name"], weap_path)
    antiarmor["description"] = item["description"]
    antiarmor["contentSource"] = item["contentSource"]
    antiarmor["weight"] = 0
    antiarmor["cost"] = 0
    antiarmor["range"] = {
        "value": 60,
        "long": 240,
        "units": "ft"
    }
    antiarmor["save"] = {}
    antiarmor["action"] = {}
    antiarmor["consume"] = {}
    antiarmor["weaponType"] = "martialB"
    antiarmor["properties"] = {
        "amm": "true",
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
        "rel": "true",
        "ret": "false",
        "shk": "false",
        "sil": "false",
        "spc": "true",
        "str": "true",
        "thr": "false",
        "two": "true",
        "ver": "false",
        "vic": "false"
    }
    antiarmor["img"] = "systems/sw5e/packs/Icons/" + "%20".join(re.findall('[A-Z][^A-Z]*', item["weaponClassification"])) + "s/" + item["name"].replace(" ","%20") + ".webp"

    db.append(antiarmor)