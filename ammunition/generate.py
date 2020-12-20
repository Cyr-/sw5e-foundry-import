from ammunition.ammoIds import ammo_IDs
from ammunition.template import template


def generateArmorDbFile(armors, fileName):
    db = []

    for armor in armors:

        item = armor
        item["_id"] = ammo_IDs[item["name"].title()]
        item["name"] = item["name"].title()
        if item["description"]:
            item["description"] = item["description"].replace("\r\n", " ")
        else:
            item["description"] = ""
        item["description"] = "<p>" + str(item["properties"]).replace("[", "").replace("]", "").replace("'", "").title() + "</p><p>" + item["description"] + "</p>"
        item["activation"] = {}
        item["target"] = {}
        item["range"] = {}
        item["action"] = {}
        item["damage"] = {}
        item["armorClassification"] = item["armorClassification"].lower()
        item["ac"] = item["ac"].split(" ")
        item["armorValue"] = item["ac"][0]
        if item["armorClassification"] == "light":
            item["armorDex"] = ""
        elif item["armorClassification"] == "medium":
            item["armorDex"] = 2
        elif item["armorClassification"] == "heavy":
            item["armorDex"] = 0
        if "Strength" in item["propertiesMap"]:
            item["strengthRequirement"] = item["propertiesMap"]["Strength"]
        item["properties"] = {
            "Absorptive": "Absorptive" in item["propertiesMap"],
            "Agile": "Agile" in item["propertiesMap"],
            "Anchor": "Anchor" in item["propertiesMap"],
            "Avoidant": "Avoidant" in item["propertiesMap"],
            "Barbed": "Barbed" in item["propertiesMap"],
            "Bulky": "Bulky" in item["propertiesMap"],
            "Charging": "Charging" in item["propertiesMap"],
            "Concealing": "Concealing" in item["propertiesMap"],
            "Cumbersome": "Cumbersome" in item["propertiesMap"],
            "Gauntleted": "Gauntleted" in item["propertiesMap"],
            "Imbalanced": "Imbalanced" in item["propertiesMap"],
            "Impermeable": "Impermeable" in item["propertiesMap"],
            "Insulated": "Insulated" in item["propertiesMap"],
            "Interlocking": "Interlocking" in item["propertiesMap"],
            "Lambent": "Lambent" in item["propertiesMap"],
            "Lightweight": "Lightweight" in item["propertiesMap"],
            "Magnetic": "Magnetic" in item["propertiesMap"],
            "Obscured": "Obscured" in item["propertiesMap"],
            "Obtrusive": "Obtrusive" in item["propertiesMap"],
            "Powered": "Powered" in item["propertiesMap"],
            "Reactive": "Reactive" in item["propertiesMap"],
            "Regulated": "Regulated" in item["propertiesMap"],
            "Reinforced": "Reinforced" in item["propertiesMap"],
            "Responsive": "Responsive" in item["propertiesMap"],
            "Rigid": "Rigid" in item["propertiesMap"],
            "Silent": "Silent" in item["propertiesMap"],
            "Spiked": "Spiked" in item["propertiesMap"],
            "Steadfast": "Steadfast" in item["propertiesMap"],
            "Strength": "Strength" in item["propertiesMap"]
        }
        item["img"] = ""

        # Possible saving throws and whatnot
        if item["properties"]["Spiked"]:
            # get damage die
            item["damageRoll"] = item["propertiesMap"]["Spiked"].split(" ")[1]
            # remove parens
            item["damageRoll"] = item["damageRoll"].replace("(", "").replace(")", "")
            item["damageRoll"] += " + @mod"
            item["damageType"] = "kinetic"
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

        db.append(template.render(item=item))

    with open(fileName, "a") as file:
        for line in db:
            file.write(line + "\n")
