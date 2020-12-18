const fs = require("fs");
const forcePowerIds = require("./forcePowerIds");
const forcePowerTemplate = require("./forcePowerTemplate");

function generateForcePowerDbFile(entries, filename) {
    let db = [];
    let templateParameters = forcePowerTemplate.template.parameters;

    entries.map((entry) => {
        // Uncomment for debugging to display all of the api entries
        // console.log(entry);

        const titleCaseName = entry.name === entry.name.toUpperCase() ? entry.name : toTitleCase(entry.name);

        // Id
        templateParameters._id = forcePowerIds[titleCaseName];

        // Name
        templateParameters.name = titleCaseName;

        // Description
        // templateParameters.descriptionValue = description(entry);

        // Source
        templateParameters.source = entry.contentSource;

        // Activation
        const castingPeriod = entry.castingPeriodText.split(" ");
        templateParameters.activationType = castingPeriod[1];
        templateParameters.activationCost = parseInt(castingPeriod[0]);

        // Duration
        const durationText = entry.duration.match(/\d+ \w+?(?=s)/g);
        if (entry.duration === "Instantaneous") {
            templateParameters.durationValue = null;
            templateParameters.durationUnits = "inst";
        } else if (durationText) {
            const durationTextSplit = durationText[0].split(" ");
            templateParameters.durationValue = parseInt(durationTextSplit[0]);
            templateParameters.durationUnits = durationTextSplit[1];
        }

        // Target
        templateParameters.targetValue;
        templateParameters.targetWidth;
        templateParameters.targetUnits;
        templateParameters.targetType;

        // Range
        templateParameters.rangeValue;
        templateParameters.rangeUnits;

        // Damage
        templateParameters.damageParts;

        // Save
        templateParameters.saveAbility;
        templateParameters.saveDc;

        // Level
        templateParameters.level = entry.level;

        // School
        templateParameters.school;

        // Components
        templateParameters.componentsConcentration = entry.concentration;

        // Scaling
        templateParameters.scalingMode;
        templateParameters.scalingFormula;

        // Image
        templateParameters.img = `systems/sw5e/packs/Icons/Force%20Powers/${titleCaseName.split(" ").join("%20")}.webp`;

        db.push(forcePowerTemplate.template(templateParameters));
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

    if (entry.description) {
        descriptionValue += `<p>${entry.description}</p>`;
    }

    return descriptionValue;
}

exports.generateForcePowerDbFile = generateForcePowerDbFile;
