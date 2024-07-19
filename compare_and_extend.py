import json

path2 = "C:\\Users\\Bheki Lushaba\\course-data\\CourseData_Final\\North West University.json"
path1 = "C:\\Users\\Bheki Lushaba\\Desktop\\North-West\\NaturalScienceFinal.json"

with open(path1, "r", encoding="utf-8") as file1, open(path2, "r", encoding="utf-8") as file2:
    data1 = json.load(file1)
    data2 = json.load(file2)

    # Create a set of codes from data2 for quick lookup
    codes_in_data2 = {item["Code"] for item in data2}

    # Append items from data1 to data2 if their code is not already present in data2
    for item1 in data1:
        if "Code" in item1:
            if item1["Code"] not in codes_in_data2:
                data2.append(item1)

# Save the merged data to a new file or overwrite the existing one
merged_path = "C:\\Users\\Bheki Lushaba\\course-data\\CourseData_Final\\North West University.json"
with open(merged_path, "w", encoding="utf-8") as merged_file:
    json.dump(data2, merged_file, ensure_ascii=False, indent=2)
