import re

from adventuringGear.template import ammoTemplate
from adventuringGear.template import explosiveTemplate
from adventuringGear.template import utilityTemplate
from adventuringGear.template import kitTemplate
from adventuringGear.template import medicalTemplate
from adventuringGear.template import instrumentTemplate
from utilities.paths import ag_path
from utilities.SW5e_ID_Mgmt import getID
from scrapers.scrapeDBs import getName


def getBasicInfo(item):
    item["name"] = getName(item)
    item["_id"] = getID(item["name"], ag_path)
    if item["description"]:
        item["description"] = "<p>" + str(item["description"]).replace("\r", "").replace("\n", " ") + "</p>"
    else:
        item["description"] = ""
    item["img"] = "systems/sw5e/packs/Icons/" + item["equipmentCategory"] + "/" + item["contentSource"] + "/" + item["name"].replace(" ", "%20").replace(",", "") + ".webp"
    return item


def generateAmmoEntry(item):
    item = getBasicInfo(item)
    return ammoTemplate.render(item=item) + "\n"


def generateUtilityEntry(item):
    item = getBasicInfo(item)
    return utilityTemplate.render(item=item) + "\n"


def generateExplosiveEntry(item):
    item = getBasicInfo(item)
    gren_mine_regex = r"Each creature within (\d+) feet [of it]* must make a DC (\d+) (\w+) saving throw. A creature takes (\d+d\d) (\w+) damage"
    charge_regex = r"(\d+)-foot cone. Each creature within the cone must make a DC (\d+) (\w+) saving throw, taking (\d+d\d) (\w+) damage"
    match = re.search(gren_mine_regex, item["description"], re.IGNORECASE)
    if not match:
        match = re.search(charge_regex, item["description"])
    if match:
        item["damageRadius"] = match.group(1)
        item["saveDC"] = match.group(2)  # in case they change it again
        item["saveType"] = abilityDict[match.group(3).title()]
        item["damageRoll"] = match.group(4)
        item["damageType"] = match.group(5).lower()
    # special case(s)
    if item["name"] == "Mine, Stun":
        item["damageRadius"] = 15
        item["saveDC"] = 14
        item["saveType"] = "con"
    elif item["name"] == "Charge, Plasma" or item["name"] == "Charge, Fragmentation":
        item["damageShape"] = "cone"

    return explosiveTemplate.render(item=item) + "\n"


def generateKitEntry(item):
    item = getBasicInfo(item)
    return kitTemplate.render(item=item) + "\n"


def generateMedicalEntry(item):
    item = getBasicInfo(item)
    actionRegex = r"as an action"
    actionMatch = re.search(actionRegex, item["description"], re.IGNORECASE)
    if actionMatch:
        item["activation"] = {
            "type": "action",
            "cost": 1,
            "condition": ""
        }
        item["range"] = {
            "value": 5,
            "units": "ft"
        }
    else:
        item["activation"] = {
            "type": "",
            "cost": 0,
            "condition": ""
        }
    durationRegex = r"for (\d+) ([hour|hours|minute|minutes|day|days|round|rounds|turn|turns])"
    durationMatch = re.search(durationRegex, item["description"])
    if durationMatch:
        item["duration"] = {
            "value": durationMatch.group(1),
            "units": durationMatch.group(2)
        }
    # I was going to do this via regex, but the descriptions aren't unique enough..
    if item["name"] == "Antitoxkit" or "Medpac" or "Poison" or "Traumakit":
        item["target"] = {
            "value": 1,
            "units": "",
            "type": "creature"
        }
    elif item["name"] == "Emergency Battery" or "Repair Kit":
        item["target"] = {
            "value": 1,
            "units": "",
            "type": "droid"
        }
    chargesRegex = r"has (\d+) charges"
    usesRegex = r"has (\d+) uses"
    timesRegex = r"stabalizes (\d+) times"
    usesMatch = re.search(chargesRegex, item["description"])
    if not usesMatch:
        usesMatch = re.search(usesRegex, item["description"])
    if not usesMatch:
        usesMatch = re.search(timesRegex, item["description"])
    if usesMatch:
        item["uses"] = {
            "value": usesMatch.group(1),
            "max": usesMatch.group(1)
        }
    return medicalTemplate.render(item=item) + "\n"


def generateInstrumentEntry(item):
    item = getBasicInfo(item)
    return instrumentTemplate.render(item=item) + "\n"


def generateAdventuringGearDbFile(items, fileName):
    db = []

    for item in items:
        if item["equipmentCategory"] == "Ammunition":
            db.append(generateAmmoEntry(item))
        elif item["equipmentCategory"] == "Explosive":
            db.append(generateExplosiveEntry(item))
        elif item["equipmentCategory"] == "Utility" or "Tool":
            db.append(generateUtilityEntry(item))
        elif item["equipmentCategory"] == "Kit":
            db.append(generateKitEntry(item))
        elif item["equipmentCategory"] == "Medical":
            db.append(generateMedicalEntry(item))
        elif item["equipmentCategory"] == "MusicalInstrument":
            db.append(generateInstrumentEntry(item))

    # db.sort(key=lambda item: item["_id"])
    db = sorted(db)

    with open("output/" + fileName, "w") as file:
        for line in db:
            file.write(line)


abilityDict = {
    "Strength": "str",
    "Dexterity": "dex",
    "Constitution": "con",
    "Intelligence": "int",
    "Wisdom": "wis"
}
