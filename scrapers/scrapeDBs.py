import os
import json
import glob


def getName(item):
    if item["name"]:
        return item["name"]
    else:
        return ""


def getId(item):
    if item["_id"]:
        return item["_id"]
    else:
        return ""


path = r"C:\Users\William\AppData\Local\FoundryVTT\Data\systems\sw5e - original\packs\packs"
db = "adventuringGear.db"

output_file = open("adventuringGearIds.py", "w")

PHB = []
WH = []

for filename in glob.glob(os.path.join(path, db)):
    with open(os.path.join(os.getcwd(), filename), 'r', encoding="utf-8") as f:
        lines = f.readlines()
        for line in lines:
            try:
                item = json.loads(line)
                # do stuff
                if "source" in item["data"] and item["data"]["source"] == "PHB":
                    PHB.append("\"" + getName(item) + "\": \"" + getId(item) + "\",\n")
                elif "source" in item["data"] and item["data"]["source"] == "WH":
                    WH.append("\"" + getName(item) + "\": \"" + getId(item) + "\",\n")
            except(ValueError):
                # we got a None and it breaks json for some reason..
                continue
        f.close()

output_file.write("adventuringGear_IDs = {\n\t# PHB\n")
for e in PHB:
    output_file.write("\t" + str(e))
output_file.write("\n\t# WH\n")
for e in WH:
    output_file.write("\t" + str(e))
# don't forget to remove the comma on the last entry
output_file.write("}")
output_file.close()
