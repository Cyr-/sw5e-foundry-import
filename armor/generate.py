import json
from jinja2 import Environment, PackageLoader, Template


def generateArmorDbFile(armors, fileName):
    db = []

    env = Environment(loader=PackageLoader('armor', '/'))
    env.filters['jsonify'] = json.dumps
    
    template = env.get_template('template.json')

    for armor in armors:
        item = {
            '_id': '',
            'name': armor['name'].title(),
            'activation': {},
            'target': {},
            'range': {},
            'action': {},
            'damage': {},
            'armor': {},
            'properties': {},
        }

        db.append(template.render(item = item))

    print(db)


#     entries.map((entry) => {
#         // Uncomment for debugging to display all of the api entries
#         // console.log(entry);

#         const titleCaseName = entry.name === entry.name.toUpperCase() ? entry.name : toTitleCase(entry.name);

#         // Id
#         templateParameters._id = armorIds[titleCaseName];

#         // Name
#         templateParameters.name = titleCaseName;

#         // Description
#         templateParameters.descriptionValue = description(entry);

#         // Source
#         templateParameters.source = entry.contentSource;

#         // Weight
#         templateParameters.weight = parseInt(entry.weight);

#         // Price
#         templateParameters.price = entry.cost;

#         // Activation
#         if (entry.propertiesMap.hasOwnProperty("Spiked")) {
#             templateParameters.activationType = "special";
#             templateParameters.activationCost = 1;
#         } else {
#             templateParameters.activationType = "";
#             templateParameters.activationCost = 0;
#         }

#         // Targets
#         if (entry.propertiesMap.hasOwnProperty("Spiked")) {
#             templateParameters.targetValue = 1;
#             templateParameters.targetType = "enemy";
#         } else {
#             templateParameters.targetValue = null;
#             templateParameters.targetType = "";
#         }

#         // Range
#         if (entry.propertiesMap.hasOwnProperty("Spiked")) {
#             templateParameters.rangeValue = 5;
#             templateParameters.rangeUnits = "ft";
#         } else {
#             templateParameters.rangeValue = null;
#             templateParameters.rangeUnits = "";
#         }

#         // Action Type
#         if (entry.propertiesMap.hasOwnProperty("Spiked")) {
#             templateParameters.actionType = "other";
#         } else {
#             templateParameters.actionType = "";
#         }

#         // Damage
#         if (entry.propertiesMap.hasOwnProperty("Spiked")) {
#             templateParameters.damageParts = [[`${entry.propertiesMap.Spiked.match(/\d+d\d+/g)[0]} + @mod`, "kinetic"]];
#         } else {
#             templateParameters.damageParts = [];
#         }

#         // Armor
#         const acValues = entry.ac.match(/\d+/g);
#         templateParameters.armorType = entry.armorClassification.toLowerCase();
#         templateParameters.armorValue = parseInt(acValues[0]);

#         if (acValues[1]) {
#             templateParameters.armorDex = parseInt(acValues[1]);
#         } else if (entry.ac.match(/\+ Dex modifier/g) || entry.armorClassification.toLowerCase() === "shield") {
#             templateParameters.armorDex = null;
#         } else {
#             templateParameters.armorDex = 0;
#         }

#         // Strength
#         templateParameters.strength = entry.propertiesMap.Strength
#             ? parseInt(entry.propertiesMap.Strength.match(/\d+/g)[0])
#             : 0;

#         // Stealth
#         templateParameters.stealth =
#             entry.stealthDisadvantage || entry.properties.map((s) => s.toLowerCase()).includes("obtrusive");

#         // Properties
#         templateParameters.propertyAbsorptive = entry.propertiesMap.hasOwnProperty("Absorptive");
#         templateParameters.propertyAgile = entry.propertiesMap.hasOwnProperty("Agile");
#         templateParameters.propertyAvoidant = entry.propertiesMap.hasOwnProperty("Avoidant");
#         templateParameters.propertyBulky = entry.propertiesMap.hasOwnProperty("Bulky");
#         templateParameters.propertyCharging = entry.propertiesMap.hasOwnProperty("Charging");
#         templateParameters.propertyConcealing = entry.propertiesMap.hasOwnProperty("Concealing");
#         templateParameters.propertyCumbersome = entry.propertiesMap.hasOwnProperty("Cumbersome");
#         templateParameters.propertyImbalanced = entry.propertiesMap.hasOwnProperty("Imbalanced");
#         templateParameters.propertyImpermeable = entry.propertiesMap.hasOwnProperty("Impermeable");
#         templateParameters.propertyInsulated = entry.propertiesMap.hasOwnProperty("Insulated");
#         templateParameters.propertyObscured = entry.propertiesMap.hasOwnProperty("Obscured");
#         templateParameters.propertyObtrusive = entry.properties.map((s) => s.toLowerCase()).includes("obtrusive");
#         templateParameters.propertyReactive = entry.propertiesMap.hasOwnProperty("Reactive");
#         templateParameters.propertyRegulated = entry.propertiesMap.hasOwnProperty("Regulated");
#         templateParameters.propertyReinforced = entry.propertiesMap.hasOwnProperty("Reinforced");
#         templateParameters.propertyRigid = entry.propertiesMap.hasOwnProperty("Rigid");
#         templateParameters.propertySilent = entry.propertiesMap.hasOwnProperty("Silent");
#         templateParameters.propertySpiked = entry.propertiesMap.hasOwnProperty("Spiked");
#         templateParameters.propertyStrength = entry.propertiesMap.hasOwnProperty("Strength");

#         // Image
#         templateParameters.img = `systems/sw5e/packs/Icons/Armor/${entry.contentSource}/${titleCaseName
#             .split(" ")
#             .join("%20")}.webp`;

#         db.push(armorTemplate.template(templateParameters));
#     });

#     db.sort((a, b) => (a._id > b._id ? 1 : -1));

#     let dbString = "";
#     db.map((line) => (dbString += JSON.stringify(line) + "\n"));

#     fs.writeFile(`./output/${filename}`, dbString, function (err) {
#         if (err) {
#             throw err;
#         }

#         console.log(`Saved ${filename}.`);
#     });
# }

def description(item):
    description_value = ""

    # propertiesValue = [
    #     entry.propertiesMap.Absorptive && toTitleCase(entry.propertiesMap.Absorptive),
    #     entry.propertiesMap.Agile && toTitleCase(entry.propertiesMap.Agile),
    #     entry.propertiesMap.Avoidant && toTitleCase(entry.propertiesMap.Avoidant),
    #     entry.propertiesMap.Charging && toTitleCase(entry.propertiesMap.Charging),
    #     entry.propertiesMap.Insulated && toTitleCase(entry.propertiesMap.Insulated),
    #     entry.propertiesMap.Reactive && toTitleCase(entry.propertiesMap.Reactive),
    #     entry.propertiesMap.Spiked && toTitleCase(entry.propertiesMap.Spiked),
    #     entry.propertiesMap.Strength && toTitleCase(entry.propertiesMap.Strength)
    # ]
    #     .filter(Boolean)
    #     .join(", ");

    # if (propertiesValue) {
    #     descriptionValue += `<p>${propertiesValue}</p>`;
    # }

    # if (entry.description) {
    #     descriptionValue += `<p>${entry.description}</p>`;
    # }

    return description_value
