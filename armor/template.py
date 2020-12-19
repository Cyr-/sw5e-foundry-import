from jinja2 import Template

template = Template('"{"_id":"{{item._id}}","name":"{{item.name}}","permission":{"default":0,"vXYkFWX6qzvOu2jc":3},"type":"equipment","data":{"description":{"value":"{{item.description}}","chat":"","unidentified":""},"source":"{{item.contentSource}}","quantity":1,"weight":"{{item.weight}}","price":"{{item.cost}}","attuned":false,"equipped":false,"rarity":"","identified":true,"activation":{"type":"{{item.activation.type}}","cost":"{{item.activation.cost}}","condition":""},"duration":{"value":null,"units":""},"target":{"value":"{{item.target.value}}","units":"","type":"{{item.target.type}}"},"range":{"value":"{{item.range.value}}","long":null,"units":"{{item.range.units}}"},"uses":{"value":0,"max":0,"per":null},"consume":{"type":"","target":null,"amount":null},"ability":null,"actionType":"{{item.action.type}}","attackBonus":0,"chatFlavor":"","critical":null,"damage":{"parts":"{{item.damage.parts}}","versatile":""},"formula":"","save":{"ability":"","dc":null,"scaling":"spell"},"armor":{"type":"{{item.armorClassification}}","value":"{{item.armorValue}}","dex":"{{item.armorDex}}"},"strength":"{{item.strengthRequirement}}","stealth":"{{item.stealthDisadvantage}}","proficient":false,"attributes":{"spelldc":10},"properties":{"Absorptive":"{{item.properties.absorptive}}","Agile":"{{item.properties.agile}}","Anchor":false,"Avoidant":"{{item.properties.avoidant}}","Barbed":false,"Bulky":"{{item.properties.bulky}}","Charging":"{{item.properties.charging}}","Concealing":"{{item.properties.concealing}}","Cumbersome":"{{item.properties.cumbersome}}","Gauntleted":false,"Imbalanced":"{{item.properties.imbalanced}}","Impermeable":"{{item.properties.impermeable}}","Insulated":"{{item.properties.insulated}}","Interlocking":false,"Lambent":false,"Lightweight":false,"Magnetic":false,"Obscured":"{{item.properties.obscured}}","Obtrusive":"{{item.properties.obtrusive}}","Powered":false,"Reactive":"{{item.properties.reactive}}","Regulated":"{{item.properties.regulated}}","Reinforced":"{{item.properties.reinforced}}","Responsive":false,"Rigid":"{{item.properties.rigid}}","Silent":"{{item.properties.silent}}","Spiked":"{{item.properties.spiked}}","Steadfast":false,"Strength":"{{item.properties.strength}}","Versatile":false},"cptooltipmode":"hid"},"flags":{"dynamiceffects":{"equipActive":false,"alwaysActive":false}}","effects":[],"img":"{{item.img}}"}"')
