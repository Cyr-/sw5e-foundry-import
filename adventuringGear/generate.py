from adventuringGear.template import ammoTemplate
from adventuringGear.template import explosiveTemplate
from adventuringGear.template import utilityTemplate
from utilities.paths import ag_path
from utilities.SW5e_ID_Mgmt import getID
import re


def getBasicInfo(item):
    item["_id"] = getID(item["name"], ag_path)
    item["name"] = item["name"].title()
    if item["description"]:
        item["description"] = "<p>" + str(item["description"]).replace("\r", "").replace("\n", " ") + "</p>"
    else:
        item["description"] = ""
    item["img"] = "systems/sw5e/packs/Icons/" + item["equipmentCategory"] + "/" + item["contentSource"] + "/" + item["name"].title().replace(" ", "%20").replace(",", "") + ".webp"
    return item


def generateAmmoEntry(item):
    item = getBasicInfo(item)
    return ammoTemplate.render(item=item) + "\n"


def generateUtilityEntry(item):
    item = getBasicInfo(item)
    return utilityTemplate.render(item=item) + "\n"


def generateExplosiveEntry(item):
    item = getBasicInfo(item)
    gren_mine_regex = r"ach creature within (\d+) feet [of it]* must make a DC (\d+) (\w+) saving throw. A creature takes (\d+d\d) (\w+) damage"
    charge_regex = r"(\d+)-foot cone. Each creature within the cone must make a DC (\d+) (\w+) saving throw, taking (\d+d\d) (\w+) damage"
    match = re.search(gren_mine_regex, item["description"])
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


def generateAdventuringGearDbFile(items, fileName):
    db = []

    for item in items:
        if item["equipmentCategory"] == "Ammunition":
            db.append(generateAmmoEntry(item))
        elif item["equipmentCategory"] == "Explosive":
            db.append(generateExplosiveEntry(item))
        elif item["equipmentCategory"] == "Utility":
            db.append(generateUtilityEntry(item))

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
