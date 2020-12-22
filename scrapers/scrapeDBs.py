import os
import json
import glob


def getName(item):
    if item["name"]:
        return item["name"].title()
    else:
        return ""


def getId(item):
    if item["_id"]:
        return item["_id"]
    else:
        return ""


path = r"C:\Users\William\AppData\Local\FoundryVTT\Data\systems\sw5e - original\packs\packs"
db = "*.db"

for filename in glob.glob(os.path.join(path, db)):
    if os.path.basename(filename) == "tables.db":
        continue
    outputFileName = os.path.basename(filename.replace(".db", "_Ids.py"))

    output_file = open(outputFileName, "w")

    PHB = []
    WH = []

    with open(os.path.join(os.getcwd(), filename), 'r', encoding="utf-8") as f:
        lines = f.readlines()
        for line in lines:
            try:
                item = json.loads(line)
                # do stuff
                if "source" in item["data"] and item["data"]["source"] == "PHB":
                    PHB.append("\"" + getName(item) + "\": \"" + getId(item) + "\"")
                elif "source" in item["data"] and item["data"]["source"] == "WH":
                    WH.append("\"" + getName(item) + "\": \"" + getId(item) + "\"")
            except(ValueError):
                # we got a None and it breaks json for some reason..
                # continue
                print("Encountered 'None', ignoring..")
        f.close()

    # sort the arrays
    PHB = sorted(PHB)
    WH = sorted(WH)

    # Generate output file
    output_file.write(outputFileName.replace(".py", "") + " = {\n    # PHB\n")
    for i, e in enumerate(PHB):
        if i > 0:
            output_file.write(",\n    " + str(e))
        else:
            output_file.write("    " + str(e))
    if len(WH) > 0:
        output_file.write(",\n\n    # WH\n")
        for i, e in enumerate(WH):
            if i > 0:
                output_file.write(",\n    " + str(e))
            else:
                output_file.write("    " + str(e))
    output_file.write("\n}\n")
    output_file.close()
