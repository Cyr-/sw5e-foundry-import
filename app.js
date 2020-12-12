const axios = require("axios");
const weaponImport = require("./src/weaponImport");
const armorImport = require("./src/armorImport");

axios
    .get("https://sw5eapi.azurewebsites.net/api/equipment")
    .then((response) => response.data)
    .then((data) => {
        weaponImport.generateWeaponDbFile(
            data.filter((entry) => entry.equipmentCategory === "Weapon"),
            "weapons.db"
        );
    });

axios
    .get("https://sw5eapi.azurewebsites.net/api/equipment")
    .then((response) => response.data)
    .then((data) => {
        armorImport.generateArmorDbFile(
            data.filter((entry) => entry.equipmentCategory === "Armor"),
            "armor.db"
        );
    });

// axios
//     .get("https://sw5eapi.azurewebsites.net/api/enhancedItem")
//     .then((response) => response.data)
//     .then((data) => {
//         weaponImport.generateWeaponDbFile(
//             data.filter((entry) => entry.equipmentCategory === "Weapon"),
//             "enhancedItems.db"
//         );
//     });
