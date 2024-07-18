import re
import json

path = "C:\\Users\\Bheki Lushaba\\Desktop\\North-West\\NaturalScienceFinal.json"

with open(path, "r", encoding="utf-8") as file1:
    data = json.load(file1)

    for item in data:
        if "Description" in item:

            for num in range(284, 604):
                pattern = re.escape(f"{num}")

                item["Description"] = re.sub(pattern, r"", item["Description"])

with open(path, "w", encoding="utf-8") as file2:
    json.dump(data, file2, indent=2)