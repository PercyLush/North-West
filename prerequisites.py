import json

path = "C:\\Users\\Bheki Lushaba\\Desktop\\North-West\\NaturalScienceFinal.json"

with open(path, "r", encoding="utf-8") as file1:
    data = json.load(file1)

    for item in data:
        if "Prerequisite" in item:
            Prerequisites = item["Prerequisite"]

            if len(Prerequisites) > 1:
                Codes = []
                for prerequisite in Prerequisites:
                    Codes.append({"Code": prerequisite})
                code = {"$and": Codes}
            else:
                code = {"Code": Prerequisites[0]}
            item["Prerequisite"] = code

with open(path, "w", encoding="utf-8") as file2:
    json.dump(data, file2, indent=2)