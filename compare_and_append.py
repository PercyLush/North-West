import json

Courses = "C:\\Users\\Bheki Lushaba\\Desktop\\North-West\\NaturalScienceFinal.json"
credits = "C:\\Users\\Bheki Lushaba\\Desktop\\North-West\\CreditsFinal.json"

with open(Courses, "r", encoding="utf-8") as file1, open(credits, "r", encoding="utf-8") as file2:
    data1 = json.load(file1)
    data2 = json.load(file2)

    for item1 in data1:
        for item2 in data2:
            for key in ["Code"]:
                if key in item1 and key in item2:
                    if item1[key] == item2[key]:
                        for keys in ["Credit", "Prerequisite"]:
                            if keys in item2:
                                item1[keys] = item2.get(keys)
with open(Courses, "w", encoding="utf-8") as file:
    json.dump(data1, file, indent=2)