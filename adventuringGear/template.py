from jinja2 import Template

ammoTemplate = Template('{"_id":"{{item._id}}","name":"{{item.name}}","permission":{"default":0,"vXYkFWX6qzvOu2jc":3},"type":"consumable","data":{"description":{"value":"{{item.description}}","chat":"","unidentified":""},"source":"{{item.contentSource}}","quantity":1,"weight":{{item.weight}},"price":{{item.cost}},"attuned":false,"equipped":false,"rarity":"","identified":true,"activation":{"type":"","cost":null,"condition":""},"duration":{"value":null,"units":""},"target":{"value":null,"units":"","type":""},"range":{"value":null,"long":null,"units":""},"uses":{"value":0,"max":0,"per":"","autoDestroy":false},"consume":{"type":"","target":"","amount":null},"ability":null,"actionType":"","attackBonus":0,"chatFlavor":"","critical":null,"damage":{"parts":[],"versatile":""},"formula":"","save":{"ability":"","dc":null,"scaling":"spell"},"consumableType":"ammunition","attributes":{"spelldc":10}},"flags":{"dynamiceffects":{"equipActive":false,"alwaysActive":false,"effects":[]}},"img":"{{item.img}}"}')

explosiveTemplate = Template('{"_id":"{{item._id}}","name":"{{item.name}}","permission":{"default":0,"vXYkFWX6qzvOu2jc":3},"type":"weapon","data":{"description":{"value":"{{item.description}}","chat":"","unidentified":""},"source":"{{item.contentSource}}","quantity":1,"weight":{{item.weight}},"price":{{item.cost}},"attuned":false,"equipped":false,"rarity":"","identified":true,"activation":{"type":"action","cost":1,"condition":""},"duration":{"value":null,"units":""},"target":{"value":{% if "damageRadius" in item %}{{item.damageRadius}}{% else %}null{% endif %},"units":"ft","type":"{% if "damageShape" in item %}{{item.damageShape}}{% else %}radius{% endif %}"},"range":{"value":null,"long":null,"units":""},"uses":{"value":1,"max":1,"per":"charges"},"consume":{"type":"","target":"","amount":null},"ability":"","actionType":"save","attackBonus":0,"chatFlavor":"","critical":null,"damage":{"parts":{% if "damageRoll" in item %}[["{{item.damageRoll}}","{{item.damageType}}"]]{% else %}[]{% endif %},"versatile":""},"formula":"","save":{"ability":"{% if "saveType" in item %}{{item.saveType}}{% else %}null{% endif %}","dc":{% if "saveDC" in item %}{{item.saveDC}}{% else %}null{% endif %},"scaling":"flat"},"weaponType":"improv","properties":{"amm":false,"fin":false,"fir":false,"foc":false,"hvy":false,"lgt":false,"lod":false,"rch":false,"rel":false,"ret":false,"spc":false,"thr":false,"two":false,"ver":false},"proficient":false,"attributes":{"spelldc":10}},"flags":{"dynamiceffects":{"equipActive":false,"alwaysActive":false,"effects":[]}},"img":"{{item.img}}"}')

utilityTemplate = Template('{"_id":"{{item._id}}","name":"{{item.name}}","permission":{"default":0,"vXYkFWX6qzvOu2jc":3},"type":"loot","data":{"description":{"value":"{{item.description}}","chat":"","unidentified":""},"source":"{{item.contentSource}}","quantity":1,"weight":{{item.weight}},"price":{{item.cost}},"attuned":false,"equipped":false,"rarity":"","identified":true,"damage":{"parts":[]},"attributes":{"spelldc":10}},"flags":{},"img":"{{item.img}}"}')

kitTemplate = Template('{"_id":"{{item._id}}","name":"{{item.name}}","permission":{"default":0,"vXYkFWX6qzvOu2jc":3},"type":"tool","data":{"description":{"value":"{{item.description}}","chat":"","unidentified":""},"source":"{{item.contentSource}}","quantity":1,"weight":{{item.weight}},"price":{{item.cost}},"attuned":false,"equipped":false,"rarity":"","identified":true,"damage":{"parts":[]},"attributes":{"spelldc":10}},"flags":{},"img":"{{item.img}}"}')