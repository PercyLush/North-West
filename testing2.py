import re
import json

path = "C:\\Users\\Bheki Lushaba\\Desktop\\North-West\\Credits.json"

with open(path, "r", encoding="utf-8") as file1:
    data = json.load(file1)
    
    for item in data:
        if "Code" in item:
            code = item["Code"]

            pattern_codes = r"([A-Z]+\s*\d+)"
            Codes = re.findall(pattern_codes, code)   
            if Codes:
                item["Code"] = Codes[0]
                item["Prerequisite"] = Codes[1:]


            pattern_credit = r"(\d+\s*MC|\d+\s*VC|\d+\s*PC)"
            credit = re.search(pattern_credit, code)
            if credit:
                item["Credit"] = credit.group()

with open("C:\\Users\\Bheki Lushaba\\Desktop\\North-West\\CreditsFinal.json", "w", encoding="utf-8") as file2:
    json.dump(data, file2, indent=2)