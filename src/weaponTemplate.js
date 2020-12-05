const parse = require("json-templates");

exports.template = parse({
    _id: "{{_id}}",
    name: "{{name}}",
    permission: {
        default: 0,
        vXYkFWX6qzvOu2jc: 3
    },
    type: "weapon",
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
            type: "action",
            cost: 1,
            condition: ""
        },
        duration: {
            value: null,
            units: ""
        },
        target: {
            value: 1,
            width: null,
            units: "",
            type: "enemy"
        },
        range: {
            value: "{{rangeValue}}",
            long: "{{rangeLong}}",
            units: "ft"
        },
        uses: {
            value: 0,
            max: 0,
            per: ""
        },
        consume: {
            type: "{{consumeType}}",
            target: "",
            amount: "{{consumeAmount}}"
        },
        ability: "",
        actionType: "{{actionType}}",
        attackBonus: 0,
        chatFlavor: "",
        critical: null,
        damage: {
            parts: "{{damageParts}}",
            versatile: "{{damageVersatile}}"
        },
        formula: "",
        save: {
            ability: "{{saveAbility}}",
            dc: "{{saveDc}}",
            scaling: "{{saveScaling}}"
        },
        weaponType: "{{weaponType}}",
        properties: {
            amm: "{{propertyAmmunition}}",
            aut: "{{propertyAuto}}",
            bur: "{{propertyBurst}}",
            def: "{{propertyDefensive}}",
            dex: "{{propertyDexterityRqmt}}",
            dir: "{{propertyDire}}",
            drm: "{{propertyDisarming}}",
            dgd: "{{propertyDisguised}}",
            dis: "{{propertyDisintegrate}}",
            dpt: "{{propertyDisruptive}}",
            dou: "{{propertyDouble}}",
            fin: "{{propertyFinesse}}",
            fix: "{{propertyFixed}}",
            foc: "{{propertyFocus}}",
            hvy: "{{propertyHeavy}}",
            hid: "{{propertyHidden}}",
            ken: "{{propertyKeen}}",
            lgt: "{{propertyLight}}",
            lum: "{{propertyLuminous}}",
            mig: "{{propertyMighty}}",
            pic: "{{propertyPiercing}}",
            rap: "{{propertyRapid}}",
            rch: "{{propertyReach}}",
            rel: "{{propertyReload}}",
            ret: "{{propertyReturning}}",
            shk: "{{propertyShocking}}",
            sil: "{{propertySilent}}",
            spc: "{{propertySpecial}}",
            str: "{{propertyStrengthRqmt}}",
            thr: "{{propertyThrown}}",
            two: "{{propertyTwoHanded}}",
            ver: "{{propertyVersatile}}",
            vic: "{{propertyVicious}}",
            mgc: false,
            nodam: false,
            faulldam: false
        },
        proficient: false,
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
