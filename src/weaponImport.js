const fs = require("fs");
const weaponIds = require("./weaponIds");
const weaponTemplate = require("./weaponTemplate");

function generateWeaponDbFile(entries, filename) {
    let db = [];
    let templateParameters = weaponTemplate.template.parameters;

    generateUnarmedStrike(templateParameters, db);

    entries.map((entry) => {
        // Uncomment for debugging to display all of the api entries
        // console.log(entry);

        const titleCaseName = entry.name === entry.name.toUpperCase() ? entry.name : toTitleCase(entry.name);

        // Id
        templateParameters._id = weaponIds[titleCaseName];

        // Name
        templateParameters.name = titleCaseName;

        // Description
        templateParameters.descriptionValue = description(entry);

        // Source
        templateParameters.source = entry.contentSource;

        // Weight
        templateParameters.weight = parseInt(entry.weight);

        // Price
        templateParameters.price = entry.cost;

        // Range
        const rangeString =
            (entry.propertiesMap.Ammunition && entry.propertiesMap.Ammunition.match(/\d+\/\d+/g)) ||
            (entry.propertiesMap.Range &&
                (entry.propertiesMap.Range.match(/\d+\/\d+/g) || entry.propertiesMap.Range.match(/\d+/g)));

        if (rangeString) {
            const rangeSplit = rangeString[0].split("/");

            templateParameters.rangeValue = parseInt(rangeSplit[0]);
            templateParameters.rangeLong = parseInt(rangeSplit[1]);
        } else if (entry.propertiesMap.hasOwnProperty("Reach")) {
            templateParameters.rangeValue = 10;
            templateParameters.rangeLong = null;
        } else {
            templateParameters.rangeValue = 5;
            templateParameters.rangeLong = null;
        }

        // Consume
        templateParameters.consumeType = entry.weaponClassification.includes("Blaster") ? "ammo" : "";
        templateParameters.consumeAmount = entry.weaponClassification.includes("Blaster") ? 1 : null;

        // Action Type
        if (entry.description && entry.description.match(/DC \d+ \w+/g) && entry.damageDieType === 0) {
            templateParameters.actionType = "save";
        } else {
            templateParameters.actionType =
                (entry.propertiesMap.Ammunition && entry.propertiesMap.Ammunition.match(/range/g)) ||
                (entry.propertiesMap.Range && entry.propertiesMap.Range.match(/range/g))
                    ? "rwak"
                    : "mwak";
        }

        // Damage
        const versatileValue = entry.propertiesMap.Versatile && entry.propertiesMap.Versatile.match(/\d+d\d+/g);

        templateParameters.damageParts = entry.damageNumberOfDice
            ? [[`${entry.damageNumberOfDice}d${entry.damageDieType} + @mod`, entry.damageType.toLowerCase()]]
            : [];
        templateParameters.damageVersatile = versatileValue ? `${versatileValue[0]} + @mod` : "";

        // Save
        const dcValue = entry.description && entry.description.match(/DC \d+ \w+/g);

        if (dcValue) {
            const dcValuesSplit = dcValue[0].split(" ");

            templateParameters.saveAbility = dcValuesSplit[2].substring(0, 3).toLowerCase();
            templateParameters.saveDc = parseInt(dcValuesSplit[1]);
            templateParameters.saveScaling = "flat";
        } else {
            templateParameters.saveAbility = "";
            templateParameters.saveDc = null;
            templateParameters.saveScaling = "power";
        }

        // Weapon Type
        switch (entry.weaponClassification) {
            case "SimpleBlaster":
                templateParameters.weaponType = "simpleB";
                break;

            case "MartialBlaster":
                templateParameters.weaponType = "martialB";
                break;

            case "SimpleVibroweapon":
                templateParameters.weaponType = "simpleVW";
                break;

            case "MartialVibroweapon":
                templateParameters.weaponType = "martialVW";
                break;

            case "SimpleLightweapon":
                templateParameters.weaponType = "simpleLW";
                break;

            case "MartialLightweapon":
                templateParameters.weaponType = "martialLW";
                break;

            default:
                break;
        }

        // Properties
        templateParameters.propertyAmmunition = entry.propertiesMap.hasOwnProperty("Ammunition");
        templateParameters.propertyAuto = entry.propertiesMap.hasOwnProperty("Auto");
        templateParameters.propertyBurst = entry.propertiesMap.hasOwnProperty("Burst");
        templateParameters.propertyDefensive = entry.propertiesMap.hasOwnProperty("Defensive");
        templateParameters.propertyDexterityRqmt = entry.propertiesMap.hasOwnProperty("Dexterity");
        templateParameters.propertyDire = entry.propertiesMap.hasOwnProperty("Dire");
        templateParameters.propertyDisarming = entry.propertiesMap.hasOwnProperty("Disarming");
        templateParameters.propertyDisguised = entry.propertiesMap.hasOwnProperty("Disguised");
        templateParameters.propertyDisintegrate = entry.propertiesMap.hasOwnProperty("Disintegrate");
        templateParameters.propertyDisruptive = entry.propertiesMap.hasOwnProperty("Disruptive");
        templateParameters.propertyDouble = entry.propertiesMap.hasOwnProperty("Double");
        templateParameters.propertyFinesse = entry.propertiesMap.hasOwnProperty("Finesse");
        templateParameters.propertyFixed = entry.propertiesMap.hasOwnProperty("Fixed");
        templateParameters.propertyFocus = entry.propertiesMap.hasOwnProperty("Focus");
        templateParameters.propertyHeavy = entry.propertiesMap.hasOwnProperty("Heavy");
        templateParameters.propertyHidden = entry.propertiesMap.hasOwnProperty("Hidden");
        templateParameters.propertyKeen = entry.propertiesMap.hasOwnProperty("Keen");
        templateParameters.propertyLight = entry.propertiesMap.hasOwnProperty("Light");
        templateParameters.propertyLuminous = entry.propertiesMap.hasOwnProperty("Luminous");
        templateParameters.propertyMighty = entry.propertiesMap.hasOwnProperty("Mighty");
        templateParameters.propertyPiercing = entry.propertiesMap.hasOwnProperty("Piercing");
        templateParameters.propertyRapid = entry.propertiesMap.hasOwnProperty("Rapid");
        templateParameters.propertyReach = entry.propertiesMap.hasOwnProperty("Reach");
        templateParameters.propertyReload = entry.propertiesMap.hasOwnProperty("Reload");
        templateParameters.propertyReturning = entry.propertiesMap.hasOwnProperty("Returning");
        templateParameters.propertyShocking = entry.propertiesMap.hasOwnProperty("Shocking");
        templateParameters.propertySilent = entry.propertiesMap.hasOwnProperty("Silent");
        templateParameters.propertySpecial = entry.propertiesMap.hasOwnProperty("Special");
        templateParameters.propertyStrengthRqmt = entry.propertiesMap.hasOwnProperty("Strength");
        templateParameters.propertyThrown = entry.propertiesMap.hasOwnProperty("Thrown");
        templateParameters.propertyTwoHanded = entry.propertiesMap.hasOwnProperty("Two-Handed");
        templateParameters.propertyVersatile = entry.propertiesMap.hasOwnProperty("Versatile");
        templateParameters.propertyVicious = entry.propertiesMap.hasOwnProperty("Vicious");

        // Image
        templateParameters.img = `systems/sw5e/packs/Icons/${entry.weaponClassification
            .split(/(?=[A-Z])/)
            .join("%20")}s/${titleCaseName.split(" ").join("%20")}.webp`;

        db.push(weaponTemplate.template(templateParameters));
    });

    db.sort((a, b) => (a._id > b._id ? 1 : -1));

    let dbString = "";
    db.map((line) => (dbString += JSON.stringify(line) + "\n"));

    fs.writeFile(`./output/${filename}`, dbString, function (err) {
        if (err) {
            throw err;
        }

        console.log(`Saved ${filename}.`);
    });
}

function toTitleCase(str) {
    return str.replace(/\b\w+/g, function (txt) {
        return txt.charAt(0).toUpperCase() + txt.substr(1).toLowerCase();
    });
}

function description(entry) {
    let descriptionValue = "";

    const propertiesValue = [
        entry.propertiesMap.Burst && toTitleCase(entry.propertiesMap.Burst),
        entry.propertiesMap.Dexterity && toTitleCase(entry.propertiesMap.Dexterity),
        entry.propertiesMap.Double && toTitleCase(entry.propertiesMap.Double),
        entry.propertiesMap.Rapid && toTitleCase(entry.propertiesMap.Rapid),
        entry.propertiesMap.Reload && toTitleCase(entry.propertiesMap.Reload),
        entry.propertiesMap.Strength && toTitleCase(entry.propertiesMap.Strength)
    ]
        .filter(Boolean)
        .join(", ");

    if (propertiesValue) {
        descriptionValue += `<p>${propertiesValue}</p>`;
    }

    if (entry.description) {
        descriptionValue += `<p>${entry.description}</p>`;
    }

    return descriptionValue;
}

function generateUnarmedStrike(templateParameters, db) {
    // Id
    templateParameters._id = weaponIds["Unarmed Strike"];

    // Name
    templateParameters.name = "Unarmed Strike";

    // Description
    templateParameters.descriptionValue = "";

    // Source
    templateParameters.source = "PHB";

    // Weight
    templateParameters.weight = 0;

    // Price
    templateParameters.price = 0;

    // Range
    templateParameters.rangeValue = 5;
    templateParameters.rangeLong = null;

    // Consume
    templateParameters.consumeType = "";
    templateParameters.consumeAmount = null;

    // Action Type
    templateParameters.actionType = "mwak";

    // Damage
    templateParameters.damageParts = [["1 + @mod", "kinetic"]];
    templateParameters.damageVersatile = "";

    // Save
    templateParameters.saveAbility = "";
    templateParameters.saveDc = null;
    templateParameters.saveScaling = "power";

    // Weapon Type
    templateParameters.weaponType = "natural";

    // Properties
    templateParameters.propertyAmmunition = false;
    templateParameters.propertyAuto = false;
    templateParameters.propertyBurst = false;
    templateParameters.propertyDefensive = false;
    templateParameters.propertyDexterityRqmt = false;
    templateParameters.propertyDire = false;
    templateParameters.propertyDisarming = false;
    templateParameters.propertyDisguised = false;
    templateParameters.propertyDisintegrate = false;
    templateParameters.propertyDisruptive = false;
    templateParameters.propertyDouble = false;
    templateParameters.propertyFinesse = false;
    templateParameters.propertyFixed = false;
    templateParameters.propertyFocus = false;
    templateParameters.propertyHeavy = false;
    templateParameters.propertyHidden = false;
    templateParameters.propertyKeen = false;
    templateParameters.propertyLight = false;
    templateParameters.propertyLuminous = false;
    templateParameters.propertyMighty = false;
    templateParameters.propertyPiercing = false;
    templateParameters.propertyRapid = false;
    templateParameters.propertyReach = false;
    templateParameters.propertyReload = false;
    templateParameters.propertyReturning = false;
    templateParameters.propertyShocking = false;
    templateParameters.propertySilent = false;
    templateParameters.propertySpecial = false;
    templateParameters.propertyStrengthRqmt = false;
    templateParameters.propertyThrown = false;
    templateParameters.propertyTwoHanded = false;
    templateParameters.propertyVersatile = false;
    templateParameters.propertyVicious = false;

    // Image
    templateParameters.img = "icons/svg/mystery-man.svg";

    db.push(weaponTemplate.template(templateParameters));
}

exports.generateWeaponDbFile = generateWeaponDbFile;
