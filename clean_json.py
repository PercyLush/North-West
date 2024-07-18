import re
import json

path = "C:\\Users\\Bheki Lushaba\\Desktop\\North-West\\output_law.json"

with open(path, "r", encoding="utf-8") as file1:
    data = json.load(file1)

    for item in data:
        if "Institution" in item:
            del item["Institution"]
            item["Institution"] = "North West University"

with open("C:\\Users\\Bheki Lushaba\\Desktop\\North-West\\output_law.json", "w", encoding="utf-8") as file2:
    json.dump(data, file2, indent=2)


def assessments():
    path = "C:\\Users\\Bheki Lushaba\\Desktop\\North-West\\output_law.json"

    with open(path, "r", encoding="utf-8") as file1:
        data = json.load(file1)

        for item in data:
            DATA = []

            if "Assessments" in item:
                assessments = item["Assessments"].split("\n")

                for assessment in assessments:
                    name_pattern = r"([A-z]+)"
                    weight_pattern = r"(\d+)"
                    name = re.search(name_pattern, assessment)
                    weight = re.search(weight_pattern, assessment)
                    new_assessment = {"Name": name.group(),"Type": "Coursework","Weight": weight.group()}
                    DATA.append(new_assessment)
            item["Assessments"] = DATA

    with open("C:\\Users\\Bheki Lushaba\\Desktop\\North-West\\output_law.json", "w", encoding="utf-8") as file2:
        json.dump(data, file2, indent=2)