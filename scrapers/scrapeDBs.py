import pathlib
import json

for path in pathlib.Path("/Users/williamweir10/GitHub/sw5e-foundry-import").iterdir():
    if path.is_file():
        current_file = open(path, "a")
        lines = current_file.read()
        data = json.loads(lines)
        for e in data:
            if e["equipmentCategory"] == "Ammunition":
                print(e)
    current_file.close()
