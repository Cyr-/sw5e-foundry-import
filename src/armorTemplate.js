const parse = require("json-templates");

exports.template = parse({
    _id: "{{_id}}",
    name: "{{name}}",
    permission: {
        default: 0,
        vXYkFWX6qzvOu2jc: 3
    },
    type: "equipment",
    data: {
        description: {
            value: "{{descriptionValue}}",
            chat: "",
            unidentified: ""
        },
        source: "{{source}}",
        quantity: 1,
        weight: "{{weight}}",
        price: "{{price}}",
        attuned: false,
        equipped: false,
        rarity: "",
        identified: true,
        activation: {
            type: "",
            cost: 0,
            condition: ""
        },
        duration: {
            value: null,
            units: ""
        },
        target: {
            value: null,
            units: "",
            type: ""
        },
        range: {
            value: null,
            long: null,
            units: ""
        },
        uses: {
            value: 0,
            max: 0,
            per: null
        },
        consume: {
            type: "",
            target: null,
            amount: null
        },
        ability: null,
        actionType: "",
        attackBonus: 0,
        chatFlavor: "",
        critical: null,
        damage: {
            parts: [],
            versatile: ""
        },
        formula: "",
        save: {
            ability: "",
            dc: null,
            scaling: "spell"
        },
        armor: {
            type: "heavy",
            value: 17,
            dex: 0
        },
        strength: 15,
        stealth: true,
        proficient: false,
        attributes: { spelldc: 10 },
        cptooltipmode: "hid"
    },
    flags: { dynamiceffects: { equipActive: false, alwaysActive: false, effects: [] } },
    img: "systems/sw5e/packs/Icons/Armor/PHB/Assault%20Armor.webp"
});
