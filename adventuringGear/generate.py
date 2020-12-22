from adventuringGear.template import ammoTemplate
from utilities.paths import ag_path
from utilities.SW5e_ID_Mgmt import getID


def generateAmmoEntry(item):
    item["_id"] = getID(item["name"], ag_path)
    item["name"] = item["name"].title()
    item["description"] = str(item["description"]).replace("\r", "").replace("\n", " ")
    item["img"] = "systems/sw5e/packs/Icons/Armor/" + item["contentSource"] + "/" + item["name"].title().replace(" ", "%20").replace(",", "") + ".webp"

    return ammoTemplate.render(item=item) + "\n"


def generateAdventuringGearDbFile(items, fileName):
    db = []

    for item in items:
        if item["equipmentCategory"] == "Ammunition":
            db.append(generateAmmoEntry(item))

    # db.sort(key=lambda item: item["_id"])
    db = sorted(db)

    with open("output/" + fileName, "w") as file:
        for line in db:
            file.write(line)
