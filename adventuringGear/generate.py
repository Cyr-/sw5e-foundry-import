from armor.armorIds import armor_IDs
from armor.template import template


def generateAmmoDbFile(ammunitions, fileName):
    db = []

    for ammo in ammunitions:
        item = ammo
        item["_id"] = ammo_IDs[item["name"].title()]
        item["name"] = item["name"].title()
        item["description"] = generateDescription(item)
        item["activation"] = {
            "cost": 0
        }
        item["target"] = {}
        item["range"] = {}
        item["action"] = {}
        item["damage"] = {}
        item["armorClassification"] = item["armorClassification"].lower()
        item["ac"] = item["ac"].split(" ")
        item["armorValue"] = item["ac"][0].replace("+", "")
        if item["armorClassification"] == "light" or item["armorClassification"] == "shield":
            item["armorDex"] = None
        elif item["armorClassification"] == "medium":
            item["armorDex"] = 2
        elif item["armorClassification"] == "heavy":
            item["armorDex"] = 0
        if "Strength" in item["propertiesMap"]:
            item["strengthRequirement"] = item["propertiesMap"]["Strength"].lower().replace("strength ", "")
        else:
            item["strengthRequirement"] = 0
        if "obtrusive" in [property.lower() for property in item["properties"]]:
            item["stealthDisadvantage"] = "true"
        else:
            item["stealthDisadvantage"] = str(item["stealthDisadvantage"]).lower()
        item["properties"] = {
            "absorptive": "true" if "Absorptive" in item["propertiesMap"] else "false",
            "agile": "true" if "Agile" in item["propertiesMap"] else "false",
            "anchor": "true" if "Anchor" in item["propertiesMap"] else "false",
            "avoidant": "true" if "Avoidant" in item["propertiesMap"] else "false",
            "barbed": "true" if "Barbed" in item["propertiesMap"] else "false",
            "bulky": "true" if "Bulky" in item["propertiesMap"] else "false",
            "charging": "true" if "Charging" in item["propertiesMap"] else "false",
            "concealing": "true" if "Concealing" in item["propertiesMap"] else "false",
            "cumbersome": "true" if "Cumbersome" in item["propertiesMap"] else "false",
            "gauntleted": "true" if "Gauntleted" in item["propertiesMap"] else "false",
            "imbalanced": "true" if "Imbalanced" in item["propertiesMap"] else "false",
            "impermeable": "true" if "Impermeable" in item["propertiesMap"] else "false",
            "insulated": "true" if "Insulated" in item["propertiesMap"] else "false",
            "interlocking": "true" if "Interlocking" in item["propertiesMap"] else "false",
            "lambent": "true" if "Lambent" in item["propertiesMap"] else "false",
            "lightweight": "true" if "Lightweight" in item["propertiesMap"] else "false",
            "magnetic": "true" if "Magnetic" in item["propertiesMap"] else "false",
            "obscured": "true" if "Obscured" in item["propertiesMap"] else "false",
            "obtrusive": "true" if "obtrusive" in [property.lower() for property in item["properties"]] else "false",
            "powered": "true" if "Powered" in item["propertiesMap"] else "false",
            "reactive": "true" if "Reactive" in item["propertiesMap"] else "false",
            "regulated": "true" if "Regulated" in item["propertiesMap"] else "false",
            "reinforced": "true" if "Reinforced" in item["propertiesMap"] else "false",
            "responsive": "true" if "Responsive" in item["propertiesMap"] else "false",
            "rigid": "true" if "Rigid" in item["propertiesMap"] else "false",
            "silent": "true" if "Silent" in item["propertiesMap"] else "false",
            "spiked": "true" if "Spiked" in item["propertiesMap"] else "false",
            "steadfast": "true" if "Steadfast" in item["propertiesMap"] else "false",
            "strength": "true" if "Strength" in item["propertiesMap"] else "false"
        }
        item["img"] = "systems/sw5e/packs/Icons/Armor/" + item["contentSource"] + "/" + item["name"].title().replace(" ", "%20") + ".webp"

        # Possible saving throws and whatnot
        if "Spiked" in item["propertiesMap"]:
            # get damage die
            item["damageRoll"] = item["propertiesMap"]["Spiked"].split(" ")[1]
            # remove parens
            item["damageRoll"] = item["damageRoll"].replace("(", "").replace(")", "")
            item["damageRoll"] += " + @mod"
            item["damageType"] = "kinetic"
            item["action"] = {
                "type": "other"
            }
            item["activation"] = {
                "type": "special",
                "cost": 1,
                "condition": ""
            }
            item["duration"] = {
                "value": "",
                "units": ""
            }
            item["target"] = {
                "value": 1,
                "units": "",
                "type": "enemy"
            }
            item["range"] = {
                "value": 5,
                "long": "",
                "units": "ft"
            }

        db.append(item)

    db.sort(key=lambda item: item["_id"])

    with open("output/" + fileName, "w") as file:
        for line in db:
            file.write(template.render(item=line) + "\n")


def generateDescription(item):
    description = ""

    propertyValues = [
        "Absorptive" in item["propertiesMap"] and item["propertiesMap"]["Absorptive"],
        "Agile" in item["propertiesMap"] and item["propertiesMap"]["Agile"],
        "Avoidant" in item["propertiesMap"] and item["propertiesMap"]["Avoidant"],
        "Charging" in item["propertiesMap"] and item["propertiesMap"]["Charging"],
        "Insulated" in item["propertiesMap"] and item["propertiesMap"]["Insulated"],
        "Reactive" in item["propertiesMap"] and item["propertiesMap"]["Reactive"],
        "Spiked" in item["propertiesMap"] and item["propertiesMap"]["Spiked"],
        "Strength" in item["propertiesMap"] and item["propertiesMap"]["Strength"]
    ]

    filteredPropertyValues = [property for property in propertyValues if not property]  # same thing as != False

    if filteredPropertyValues:
        separator = ", "
        description += "<p>" + separator.join([property.title() for property in filteredPropertyValues]) + "</p>"

    if item["description"]:
        description += "<p>" + item["description"].replace("\r", "").replace("\n", " ") + "</p>"

    return description
