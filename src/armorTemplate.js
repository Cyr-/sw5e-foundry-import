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
            type: "{{activationType}}",
            cost: "{{activationCost}}",
            condition: ""
        },
        duration: {
            value: null,
            units: ""
        },
        target: {
            value: "{{targetValue}}",
            units: "",
            type: "{{targetType}}"
        },
        range: {
            value: "{{rangeValue}}",
            long: null,
            units: "{{rangeUnits}}"
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
        actionType: "{{actionType}}",
        attackBonus: 0,
        chatFlavor: "",
        critical: null,
        damage: {
            parts: "{{damageParts}}",
            versatile: ""
        },
        formula: "",
        save: {
            ability: "",
            dc: null,
            scaling: "spell"
        },
        armor: {
            type: "{{armorType}}",
            value: "{{armorValue}}",
            dex: "{{armorDex}}"
        },
        strength: "{{strength}}",
        stealth: "{{stealth}}",
        proficient: false,
        attributes: {
            spelldc: 10
        },
        properties: {
            Absorptive: "{{propertyAbsorptive}}",
            Agile: "{{propertyAgile}}",
            Anchor: false,
            Avoidant: "{{propertyAvoidant}}",
            Barbed: false,
            Bulky: "{{propertyBulky}}",
            Charging: "{{propertyCharging}}",
            Concealing: "{{propertyConcealing}}",
            Cumbersome: "{{propertyCumbersome}}",
            Gauntleted: false,
            Imbalanced: "{{propertyImbalanced}}",
            Impermeable: "{{propertyImpermeable}}",
            Insulated: "{{propertyInsulated}}",
            Interlocking: false,
            Lambent: false,
            Lightweight: false,
            Magnetic: false,
            Obscured: "{{propertyObscured}}",
            Obtrusive: "{{propertyObtrusive}}",
            Powered: false,
            Reactive: "{{propertyReactive}}",
            Regulated: "{{propertyRegulated}}",
            Reinforced: "{{propertyReinforced}}",
            Responsive: false,
            Rigid: "{{propertyRigid}}",
            Silent: "{{propertySilent}}",
            Spiked: "{{propertySpiked}}",
            Steadfast: false,
            Strength: "{{propertyStrength}}",
            Versatile: false
        },
        cptooltipmode: "hid"
    },
    flags: {
        dynamiceffects: {
            equipActive: false,
            alwaysActive: false
        }
    },
    effects: [],
    img: "{{img}}"
});
