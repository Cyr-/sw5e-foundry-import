const parse = require("json-templates");

exports.template = parse({
    _id: "{{_id}}",
    name: "{{name}}",
    type: "power",
    data: {
        description: {
            value: "{{descriptionValue}}",
            chat: "",
            unidentified: ""
        },
        source: "{{source}}",
        activation: {
            type: "{{activationType}}",
            cost: "{{activationCost}}",
            condition: ""
        },
        duration: {
            value: "{{durationValue}}",
            units: "{{durationUnits}}"
        },
        target: {
            value: "{{targetValue}}",
            width: "{{targetWidth}}",
            units: "{{targetUnits}}",
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
            per: ""
        },
        consume: {
            type: "",
            target: "",
            amount: null
        },
        ability: "",
        actionType: "",
        attackBonus: 0,
        chatFlavor: "",
        critical: null,
        damage: {
            parts: "{{damageParts}}",
            versatile: ""
        },
        formula: "",
        save: {
            ability: "{{saveAbility}}",
            dc: "{{saveDc}}",
            scaling: "power"
        },
        level: "{{level}}",
        school: "{{school}}",
        components: {
            value: "",
            vocal: false,
            somatic: false,
            material: false,
            ritual: false,
            concentration: "{{componentsConcentration}}"
        },
        materials: {
            value: "",
            consumed: false,
            cost: 0,
            supply: 0
        },
        preparation: {
            mode: "prepared",
            prepared: false
        },
        scaling: {
            mode: "{{scalingMode}}",
            formula: "{{scalingFormula}}"
        },
        armorproperties: {
            parts: []
        },
        weaponproperties: {
            parts: []
        }
    },
    effects: [],
    img: "{{img}}"
});
