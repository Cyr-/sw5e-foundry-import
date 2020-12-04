const axios = require("axios");
const weaponIds = require("./weaponIds");

function toTitleCase(str) {
    return str.replace(/\b\w+/g, function (txt) {
        return txt.charAt(0).toUpperCase() + txt.substr(1).toLowerCase();
    });
}

let db = "";

axios
    .get("https://sw5eapi.azurewebsites.net/api/equipment")
    .then((response) => response.data)
    .then((data) => {
        data.filter((entry) => entry.equipmentCategory === "Weapon" && entry.contentSource === "PHB").map((entry) => {
            const dbObject = {};

            // Uncomment for debugging to display all of the api entries
            // console.log(entry);

            const titleCaseName = toTitleCase(entry.name);

            // Id
            dbObject._id = weaponIds[titleCaseName];

            // Name
            dbObject.name = titleCaseName;

            // Permission
            dbObject.permission = { default: 0, vXYkFWX6qzvOu2jc: 3 };

            // Type
            dbObject.type = "weapon";

            // Data

            dbObject.data = {};

            // Description
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

            dbObject.data.description = {
                value: descriptionValue,
                chat: "",
                unidentified: ""
            };

            // Source
            dbObject.data.source = entry.contentSource;

            // Quantity
            dbObject.data.quantity = 1;

            // Weight
            dbObject.data.weight = parseInt(entry.weight);

            // Price
            dbObject.data.price = entry.cost;

            // Attuned
            dbObject.data.attuned = false;

            // Equipped
            dbObject.data.equipped = false;

            // Rarity
            dbObject.data.rarity = "";

            // Identified
            dbObject.data.identified = true;

            // Activation
            dbObject.data.activation = {
                type: "action",
                cost: 1,
                condition: ""
            };

            // Duration
            dbObject.data.duration = {
                value: null,
                units: ""
            };

            // Target
            dbObject.data.target = {
                value: 1,
                width: null,
                units: "",
                type: "enemy"
            };

            // Range
            const rangeString =
                (entry.propertiesMap.Ammunition && entry.propertiesMap.Ammunition.match(/\d+\/\d+/g)) ||
                (entry.propertiesMap.Range && entry.propertiesMap.Range.match(/\d+\/\d+/g));
            let rangeValues = { value: null, long: null, units: "" };

            if (rangeString) {
                const rangeSplit = rangeString[0].split("/");

                rangeValues = { value: rangeSplit[0], long: rangeSplit[1], units: "ft" };
            }

            dbObject.data.range = {
                ...rangeValues
            };

            // Uses
            dbObject.data.uses = {
                value: 0,
                max: 0,
                per: ""
            };

            // Consume
            if (entry.weaponClassification.includes("Blaster")) {
                dbObject.data.consume = {
                    type: "ammo",
                    target: "",
                    amount: 1
                };
            } else {
                dbObject.data.consume = {
                    type: "",
                    target: "",
                    amount: null
                };
            }

            // Ability
            dbObject.data.ability = "";

            // Action Type
            if (entry.description && entry.description.match(/DC \d+ \w+/g) && entry.damageDieType === 0) {
                dbObject.data.actionType = "save";
            } else {
                dbObject.data.actionType =
                    (entry.propertiesMap.Ammunition && entry.propertiesMap.Ammunition.match(/range/g)) ||
                    (entry.propertiesMap.Range && entry.propertiesMap.Range.match(/range/g))
                        ? "rwak"
                        : "mwak";
            }

            // Attack Bonus
            dbObject.data.attackBonus = "";

            // Chat Flavor
            dbObject.data.chatFlavor = "";

            // Critical
            dbObject.data.critical = null;

            // Damage
            const versatileValue = entry.propertiesMap.Versatile && entry.propertiesMap.Versatile.match(/\d+d\d+/g);

            dbObject.data.damage = {
                parts: entry.damageNumberOfDice
                    ? [[`${entry.damageNumberOfDice}d${entry.damageDieType} + @mod`, entry.damageType.toLowerCase()]]
                    : [],
                versatile: versatileValue ? `${versatileValue[0]} + @mod` : ""
            };

            // Formula
            dbObject.data.formula = "";

            // Save
            const dcValue = entry.description && entry.description.match(/DC \d+ \w+/g);

            if (dcValue) {
                const dcValuesSplit = dcValue[0].split(" ");

                dbObject.data.save = {
                    ability: dcValuesSplit[2].substring(0, 3).toLowerCase(),
                    dc: parseInt(dcValuesSplit[1]),
                    scaling: "flat"
                };
            } else {
                dbObject.data.save = {
                    ability: "",
                    dc: null,
                    scaling: "power"
                };
            }

            // Weapon Type
            switch (entry.weaponClassification) {
                case "SimpleBlaster":
                    dbObject.data.weaponType = "simpleB";
                    break;

                case "MartialBlaster":
                    dbObject.data.weaponType = "martialB";
                    break;

                case "SimpleVibroweapon":
                    dbObject.data.weaponType = "simpleVW";
                    break;

                case "MartialVibroweapon":
                    dbObject.data.weaponType = "martialVW";
                    break;

                case "SimpleLightweapon":
                    dbObject.data.weaponType = "simpleLW";
                    break;

                case "MartialLightweapon":
                    dbObject.data.weaponType = "martialLW";
                    break;

                default:
                    break;
            }

            // Properties
            dbObject.data.properties = {
                amm: entry.propertiesMap.hasOwnProperty("Ammunition"),
                aut: entry.propertiesMap.hasOwnProperty("Auto"),
                bur: entry.propertiesMap.hasOwnProperty("Burst"),
                def: entry.propertiesMap.hasOwnProperty("Defensive"),
                dex: entry.propertiesMap.hasOwnProperty("Dexterity"),
                dir: entry.propertiesMap.hasOwnProperty("Dire"),
                drm: entry.propertiesMap.hasOwnProperty("Disarming"),
                dgd: entry.propertiesMap.hasOwnProperty("Disguised"),
                dis: entry.propertiesMap.hasOwnProperty("Disintegrate"),
                dpt: entry.propertiesMap.hasOwnProperty("Disruptive"),
                dou: entry.propertiesMap.hasOwnProperty("Double"),
                fin: entry.propertiesMap.hasOwnProperty("Finesse"),
                fix: entry.propertiesMap.hasOwnProperty("Fixed"),
                foc: entry.propertiesMap.hasOwnProperty("Focus"),
                hvy: entry.propertiesMap.hasOwnProperty("Heavy"),
                hid: entry.propertiesMap.hasOwnProperty("Hidden"),
                ken: entry.propertiesMap.hasOwnProperty("Keen"),
                lgt: entry.propertiesMap.hasOwnProperty("Light"),
                lum: entry.propertiesMap.hasOwnProperty("Luminous"),
                mig: entry.propertiesMap.hasOwnProperty("Mighty"),
                pic: entry.propertiesMap.hasOwnProperty("Piercing"),
                rap: entry.propertiesMap.hasOwnProperty("Rapid"),
                rch: entry.propertiesMap.hasOwnProperty("Reach"),
                rel: entry.propertiesMap.hasOwnProperty("Reload"),
                ret: entry.propertiesMap.hasOwnProperty("Returning"),
                shk: entry.propertiesMap.hasOwnProperty("Shocking"),
                sil: entry.propertiesMap.hasOwnProperty("Silent"),
                spc: entry.propertiesMap.hasOwnProperty("Special"),
                str: entry.propertiesMap.hasOwnProperty("Strength"),
                thr: entry.propertiesMap.hasOwnProperty("Thrown"),
                two: entry.propertiesMap.hasOwnProperty("Two-Handed"),
                ver: entry.propertiesMap.hasOwnProperty("Versatile"),
                vic: entry.propertiesMap.hasOwnProperty("Vicious"),
                mgc: false,
                nodam: false,
                faulldam: false
            };

            // Proficient
            dbObject.data.proficient = false;

            // CP Tooltip Mode
            dbObject.data.cptooltipmode = "hid";

            // Flags
            dbObject.flags = {
                dynamiceffects: {
                    equipActive: false,
                    alwaysActive: false
                }
            };

            // Effects
            dbObject.effects = [];

            // Image
            dbObject.img = `systems/sw5e/packs/Icons/${entry.weaponClassification
                .split(/(?=[A-Z])/)
                .join("%20")}s/${dbObject.name.replace(" ", "%20")}.webp`;

            db += JSON.stringify(dbObject);
            db += "\n";
        });

        console.log(db);
    });
