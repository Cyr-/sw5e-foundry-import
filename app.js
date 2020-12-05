const axios = require("axios");
const weaponImport = require("./src/weaponImport");

axios
    .get("https://sw5eapi.azurewebsites.net/api/equipment")
    .then((response) => response.data)
    .then((data) => {
        weaponImport.generateWeaponDbFile(
            data.filter((entry) => entry.equipmentCategory === "Weapon" && entry.contentSource === "PHB"),
            "weapons.db"
        );

        weaponImport.generateWeaponDbFile(
            data.filter((entry) => entry.equipmentCategory === "Weapon" && entry.contentSource === "EC"),
            "weapons-ec.db"
        );

        weaponImport.generateWeaponDbFile(
            data.filter((entry) => entry.equipmentCategory === "Weapon" && entry.contentSource === "WH"),
            "weapons-wh.db"
        );
    });
